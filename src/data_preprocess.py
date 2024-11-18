import pandas as pd

def align_by_price(data: pd.DataFrame, prices: pd.DataFrame, 
                   index: str, columns: str, values: str, aggfunc: str = 'sum') -> pd.DataFrame:
    aligned_df = data.pivot_table(
        index = index, columns = columns, values = values, aggfunc=aggfunc
    ).reindex(index=prices.index, columns=prices.columns)
    return aligned_df

def annual_div_yield(prices: pd.DataFrame, dividends: pd.DataFrame, column = 'figi') -> pd.DataFrame:
    """
    prices: (n_days, n_assets)-shape df
    dividends: melted df
    """
    anual_dividends = (
        align_by_price(
        dividends, prices, 
        index="last_buy_date", 
        columns=column,
        values="dividend_net", 
        aggfunc='sum'
        )
        .sort_index(ascending=True)
        .fillna(0).rolling(252).sum()
    )
    return anual_dividends.div(prices).dropna(how='all')

def get_additively_adjusted_prices(
    prices: pd.DataFrame,
    dividends: pd.DataFrame,
) -> pd.DataFrame:
    """
    prices: (n_days, n_assets)-shape df
    dividends: melted df
    """
    cumulative_dividends = (
        align_by_price(
        dividends, prices, 
        index="last_buy_date", 
        columns="figi", 
        values="dividend_net", 
        aggfunc='sum'
        )
        .sort_index(ascending=False)
        .cumsum().ffill().fillna(0)
        .sort_index(ascending=True)
    )
    return prices.subtract(cumulative_dividends).dropna(how="all")


def get_multiplicatively_adjusted_prices(
    prices: pd.DataFrame,
    dividends: pd.DataFrame,
) -> pd.DataFrame:
    """
    prices: (n_days, n_assets)-shape df
    dividends: melted df
    """
    multiplicative_dividends = (
        align_by_price(
        dividends, prices, 
        index="last_buy_date", 
        columns="figi", 
        values="yield_value", 
        aggfunc='sum'
        )
        .reindex(index=prices.index, columns=prices.columns)
        .sort_index(ascending=False)
        .map(lambda x: (100 - x) / 100)
        .cumprod().ffill().fillna(1)
        .sort_index(ascending=True)
    )
    return prices.multiply(multiplicative_dividends).dropna(how="all")