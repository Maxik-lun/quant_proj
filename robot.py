import duckdb
import datetime
import pandas as pd
import numpy as np
from src.skfolio_models import build_cdar_ratio
from sklearn import set_config
from src.data_preprocess import align_by_price, get_multiplicatively_adjusted_prices, annual_div_yield
from execution import MockManager
from typing import Optional

# def _get_mean_absolute_percentage_error(
#     y_true: np.ndarray, y_pred: np.ndarray
# ) -> float:
#     # or mae, mse, smape, etc.
#     epsilon = np.finfo(np.float64).eps
#     mape = np.abs(y_pred - y_true) / np.maximum(np.abs(y_true), epsilon)
#     output_errors = np.average(mape, axis=0)
#     return float(np.average(output_errors))

class PortfolioManager:
    def __init__(self, order_manager: MockManager, money = 0, path_db = 'data/main.duckdb') -> None:
        self.path_db = path_db
        self.money = money
        self._order_manager = order_manager
        self.weights = None
        with duckdb.connect(self.path_db) as conn:
            t_info = conn.sql("SELECT * FROM tinvest_shares_info").df()
            candle_figis = conn.sql("SELECT DISTINCT figi AS figi FROM tinvest_shares_candles").df()
        short_list = t_info[t_info['figi'].isin(candle_figis['figi'].tolist())]
        self.figi2ticker = dict(zip(short_list['figi'], short_list['ticker']))
        self.ticker2figi = {v: k for k, v in self.figi2ticker.items()}
        self.lot_dict = dict(zip(short_list['figi'], short_list['lot']))

    def allocate(self, now: datetime.datetime, window: int = 252, imoex_content: str = 'data/imoex_content.xlsx'):
        set_config(enable_metadata_routing=True, transform_output="pandas")
        end_date = str(now)[:10]
        # extract
        with duckdb.connect(self.path_db) as conn:
            div_data = conn.sql(f"SELECT * FROM tinvest_dividends WHERE record_date <= '{end_date}'").df()
            t_candles = conn.sql(f"SELECT * FROM tinvest_shares_candles WHERE is_complete AND time <= '{end_date}'").df()
        # transform
        price_data = t_candles.pivot(index = 'time', columns = 'figi', values = 'close')
        adj_prices = get_multiplicatively_adjusted_prices(price_data, div_data[div_data['figi'].isin(price_data.columns)])
        adj_prices = adj_prices.rename(columns = self.figi2ticker)
        div_data['ticker'] = div_data['figi'].map(self.figi2ticker)
        div_yield = annual_div_yield(adj_prices, div_data, column='ticker').fillna(0)
        returns = adj_prices.pct_change(fill_method=None).fillna(0)
        X_train = returns.iloc[-window:].copy()
        index_arr = []
        with pd.ExcelFile(imoex_content) as xl:
            for sheetname in xl.sheet_names:
                if sheetname == 'help': continue
                tmp = xl.parse(sheetname, skiprows=3)
                weight_col = tmp.columns[tmp.columns.str.startswith('Weight')][0]
                contituents_df = tmp[['Code', weight_col]].copy()
                contituents_df = contituents_df[contituents_df['Code'].isin(X_train.columns)]
                contituents_df['date'] = pd.to_datetime(sheetname, dayfirst=True)
                contituents_df['added'] = 1*(contituents_df[weight_col].fillna(0) > 0)
                index_arr.append(contituents_df[['Code', 'date', 'added']])
        imoex_contituents = pd.concat(index_arr, axis = 0)
        universe_mask = imoex_contituents.pivot_table(
            values='added', index='date', columns='Code',
        ).reindex(columns = returns.columns).replace(0, np.nan).ffill().fillna(0)
        model = build_cdar_ratio(returns, universe_mask, div_yield)
        model.fit(X_train)
        prediction = model.predict(X_train)
        # return model, X_train
        self.weights = prediction.weights_per_observation.iloc[-1] # type: ignore
        self.weights.index = self.weights.index.map(self.ticker2figi)
        return self.weights

    def get_last_price(self, figis, now = None):
        if now is None:
            now = datetime.datetime.now()
        with duckdb.connect(self.path_db) as conn:
            data = conn.sql(f"""
            SELECT figi, time, close FROM tinvest_shares_candles 
            WHERE time <= '{str(now)[:10]}' ORDER BY time DESC
            LIMIT 1000
            """).df()
            data = data[data['time'] == data['time'].max()].set_index('figi')
        return data.reindex(figis)['close']#.fillna(0)

    def prepare_positions(self,
        raw_positions: pd.DataFrame,
        target_weights: Optional[pd.Series] = None,
        now: Optional[datetime.datetime] = None,
        extra_info: Optional[pd.DataFrame] = None,
    ) -> pd.DataFrame:
        positions = raw_positions.set_index("figi")
        if target_weights is None:
            target_weights = self.weights
        index = positions.index.union(target_weights.index)
        positions = positions.reindex(index)#.fillna(0)
        positions['lot'] = positions.index.to_series().map(self.lot_dict).fillna(positions['lot'])
        positions["ticker"] = positions.index.map(self.figi2ticker)
        last_prices = self.get_last_price(index, None)
        positions["current_price"] = positions["current_price"].fillna(last_prices)
        positions["quantity"] = positions["quantity"].fillna(0)
        positions.loc["RUB000UTSTOM", "current_price"] = 1
        positions.loc["RUB000UTSTOM", "quantity"] = self.money
        if extra_info is not None:
            positions = positions.fillna(extra_info)
        # current_price is for lots
        positions["market_value"] = (
            positions["quantity"] * positions["current_price"]
        )
        positions["weight"] = (
            positions["market_value"] / positions["market_value"].sum()
        )
        positions["target_weight"] = target_weights.reindex(index).fillna(0)
        positions["delta_weight"] = (
            positions["target_weight"] - positions["weight"]
        )
        positions["target_market_value"] = (
            positions["target_weight"] * positions["market_value"].sum()
        )
        positions["delta_market_value"] = (
            positions["target_market_value"] - positions["market_value"]
        )
        positions = positions.drop(index=["RUB000UTSTOM"])
        positions["delta_quantity_for_order"] = (
            positions["delta_market_value"]
            / positions["current_price"]
            / positions["lot"]
        ).astype(int)
        positions = positions[
            positions["delta_quantity_for_order"] != 0
        ].sort_values("delta_market_value")
        return positions

    def manage_orders(self, positions_df: pd.DataFrame):
        positions = positions_df.reset_index().to_dict('records')
        order_list = []
        for position in positions:
            order = self._order_manager.place_limit_order(
                position['index'], 
                abs(position['delta_quantity_for_order']),
                position['current_price'], 
                position['delta_quantity_for_order'] > 0)
            order_list.append(order)
        return order_list

