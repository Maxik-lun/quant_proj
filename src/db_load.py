from zipfile import ZipFile
from .tinkoff_api import get_shares_info_sync, get_prices_sync, get_dividends_async
from .moex_api import get_moex_data
from typing import Optional
import pandas as pd
import glob
import duckdb
import asyncio
import os
import warnings

warnings.filterwarnings("ignore", category=DeprecationWarning)
TOKEN = os.environ['TINVEST_READ']

def _read_zipfile(name: str):
    archive_names = ['uid', 'utc', 'open', 'close', 'high', 'low', 'volume', 'other']
    with ZipFile(name) as f:
        df = pd.concat([
            pd.read_csv(f.open(csv_name), sep = ';', header = None, names = archive_names) for csv_name in sorted(f.namelist())
        ], axis = 0)
    return df

def load_1min_history(
        db_name: str = "tinvest_1min.duckdb", 
        history_path: str = "../data/archive/",
        table_name: str = 'candles_1min'):
    create_query = f"""
    CREATE TABLE IF NOT EXISTS {table_name} (
        uid UUID,
        utc TIMESTAMP,
        open FLOAT,
        close FLOAT,
        high FLOAT,
        low FLOAT,
        volume UINTEGER,
        PRIMARY KEY (uid, utc))
    """
    with duckdb.connect(db_name) as conn:
        conn.sql(create_query)
        for zip_name in sorted(glob.glob(history_path + "*.zip")):
            print(f"READING {zip_name}...", end = '')
            candles_df = _read_zipfile(zip_name)
            del candles_df['other']
            conn.sql("INSERT INTO candles_1min SELECT * FROM candles_df")
            print("ADDED TO", table_name)


def load_shares_data(start_date: pd.Timestamp, end_date: pd.Timestamp,
                token = TOKEN, db_path = 'data/main.duckdb'):
    # TODO ADD INDEXES
    shares_df = get_shares_info_sync(TOKEN)
    # universe
    short_list = (
        shares_df.query(
            'not for_qual_investor_flag and short_enabled_flag and api_trade_available_flag and real_exchange == 1'
            )[['figi', 'ticker', 'class_code', 'isin', 'lot', 'currency', 'name', 'exchange']]
    )
    figis = short_list['figi'].tolist()
    # tinvest candles
    tinvest_candles = get_prices_sync(figis, start_date, end_date, token=token)
    # moex data
    moex_info_df, moex_candles = asyncio.run(get_moex_data(str(start_date)[:10], str(end_date)[:10]))
    # dividends
    div_data = asyncio.run(get_dividends_async(figis, start_date, end_date, token=token))
    # short_list['figi'].to_csv('../figi.txt', index = False, header=False)
    create_tinvest_info = "CREATE TABLE IF NOT EXISTS tinvest_shares_info AS SELECT * FROM shares_df;"
    create_tinvest_data = "CREATE TABLE IF NOT EXISTS tinvest_shares_candles AS SELECT * FROM tinvest_candles;"
    create_div_data = "CREATE TABLE IF NOT EXISTS tinvest_dividends AS SELECT * FROM div_data;"
    create_moex_info = "CREATE TABLE IF NOT EXISTS moex_shares_info AS SELECT * FROM moex_info_df;"
    create_moex_data = "CREATE TABLE IF NOT EXISTS moex_shares_candles AS SELECT * FROM moex_candles;"
    with duckdb.connect(db_path) as conn:
        conn.sql(create_tinvest_info)
        # conn.sql("ALTER TABLE tinvest_shares_info ADD PRIMARY KEY (figi);")
        conn.sql(create_tinvest_data)
        # conn.sql("ALTER TABLE tinvest_shares_candles ADD PRIMARY KEY (figi, time);")
        conn.sql(create_div_data)
        # conn.sql("ALTER TABLE tinvest_dividends ADD PRIMARY KEY (figi, payment_date);")
        conn.sql(create_moex_info)
        # conn.sql("ALTER TABLE moex_shares_info ADD PRIMARY KEY (secid);")
        conn.sql(create_moex_data)
        # conn.sql("ALTER TABLE moex_shares_candles ADD PRIMARY KEY (secid, begin);")

def update_shares_data(figis, start_date: Optional[pd.Timestamp], end_date: Optional[pd.Timestamp],
                token = TOKEN, db_path = 'data/main.duckdb'):
    # TODO ADD LOGIC FOR TINVEST INFO DATA
    if start_date is None:
        with duckdb.connect(db_path) as conn:
            tinvest_last = conn.sql("SELECT MAX(time) AS last_dt FROM tinvest_candles").df().iloc[0, 0]
            moex_last = conn.sql("SELECT MAX(time) AS last_dt FROM moex_candles").df().iloc[0, 0]
    else:
        tinvest_last = start_date
        moex_last = start_date
    if end_date is None:
        end_date = pd.Timestamp.today().normalize()
    # tinvest candles
    tinvest_candles = get_prices_sync(figis, tinvest_last, end_date, token=token)
    div_data = asyncio.run(get_dividends_async(figis, tinvest_last, end_date, token=token))
    # moex data
    moex_info_df, moex_candles = asyncio.run(get_moex_data(str(moex_last)[:10], str(end_date)[:10]))
    insert_tinvest_data = "INSERT OR REPLACE INTO tinvest_shares_candles SELECT * FROM tinvest_candles"
    insert_div_data = "INSERT OR REPLACE INTO tinvest_dividends SELECT * FROM div_data"
    insert_moex_data = "INSERT OR REPLACE INTO moex_shares_candles SELECT * FROM moex_candles"
    inset_moex_info = "INSERT OR REPLACE INTO moex_shares_info SELECT * FROM moex_info_df"
    with duckdb.connect(db_path) as conn:
        conn.sql(insert_tinvest_data)
        conn.sql(insert_div_data)
        conn.sql(insert_moex_data)
        conn.sql(inset_moex_info)

