# from tinvest.grpc.marketdata_pb2_grpc import MarketDataService
# import asyncio
# from src.moex_api import get_moex_data
# import pandas as pd
from src.db_load import load_shares_data
from src.moex_api import download_imoex_contituents
import pandas as pd

if __name__ == '__main__':
    # print(dir(MarketDataService))
    start_date = pd.Timestamp('2015-01-01')
    end_date = pd.Timestamp('2024-10-31')
    load_shares_data(start_date, end_date)
    download_imoex_contituents()
    