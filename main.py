from execution import MockManager
from robot import PortfolioManager
import pandas as pd
import duckdb
import datetime

def get_current_portfolio(path = './portfolio.csv'):
    portfolio_df = pd.read_csv(path)
    portfolio_df['lot'] = portfolio_df.eval('quantity/quantity_lots').astype('int')
    return portfolio_df

if __name__ == '__main__':
    portfolio_df = get_current_portfolio()
    portfolio_df = portfolio_df[['figi', 'instrument_type', 'quantity', 'current_price', 'lot']]
    order_manager = MockManager('data/operations.duckdb')
    main_manager = PortfolioManager(order_manager, path_db='data/main.duckdb')
    target_weights = main_manager.allocate(datetime.datetime.now(), imoex_content='data/imoex_content.xlsx')
    positions = main_manager.prepare_positions(portfolio_df, target_weights)
    orders = main_manager.manage_orders(positions)
    print(orders)
