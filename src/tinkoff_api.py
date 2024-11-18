# sync methods
import functools
import os
import warnings
import aiometer
import datetime
import uuid

import pandas as pd
from loguru import logger
from typing import List, Optional
from tinkoff.invest import (
    AsyncClient,
    CandleInterval,
    Client,
    Operation,
    OperationState,
    PortfolioResponse,
    PositionsResponse,
    OrderDirection,
    OrderState,
    OrderType,
)
from .logging import log_function_call
from .tinkoff_convert import _dataclasses_to_dict, _dataclass_to_dict
from tinkoff.invest.schemas import InstrumentStatus
from enum import IntEnum

warnings.filterwarnings("ignore", category=DeprecationWarning)
TOKEN = os.environ['TINVEST_READ']

#@log_function_call()
def get_close_prices_sync(
    figis: List[str],
    start_date: pd.Timestamp,
    end_date: pd.Timestamp,
    interval: CandleInterval = CandleInterval.CANDLE_INTERVAL_DAY,
    is_complete: bool = True,
    token: str = TOKEN,
) -> pd.DataFrame:
    prices = get_prices_sync(
        figis=[figi for figi in figis],
        start_date=start_date,
        end_date=end_date,
        interval=interval,
        is_complete=is_complete,
        token=token,
    )
    # please, check `pd.pivot` docs
    return (
        prices[["time", "close", "figi"]]
        .pivot(index="time", columns="figi", values="close")
    )

#@log_function_call()
def get_prices_sync(
    figis: List[str],
    start_date: pd.Timestamp,
    end_date: pd.Timestamp,
    interval: CandleInterval = CandleInterval.CANDLE_INTERVAL_DAY,
    is_complete: bool = True,
    token: str = TOKEN,
) -> pd.DataFrame:
    return pd.concat([
        get_prices_for_sync(
            figi,
            start_date,
            end_date,
            interval,
            is_complete,
            token,
        )
        for figi in figis]
    )


#@log_function_call()
def get_prices_for_sync(
    figi: str,
    start_date: pd.Timestamp,
    end_date: pd.Timestamp,
    interval: CandleInterval = CandleInterval.CANDLE_INTERVAL_DAY,
    is_complete: bool = True,
    token: str = TOKEN,
) -> pd.DataFrame:
    with Client(token) as client:
        raw_candles = _dataclasses_to_dict(
            client.get_all_candles(
                figi=figi,
                from_=start_date,
                to=end_date,
                interval=interval,
            )
        )

    # please, check `pd.assign` docs
    prices = pd.DataFrame(raw_candles).assign(figi=figi)
    if prices.empty:
        logger.warning(f"No candles for {figi} ({start_date}-{end_date})")
        return prices

    if "is_complete" in prices.columns and is_complete:
        prices = prices.query("is_complete").copy()

    if interval == CandleInterval.CANDLE_INTERVAL_DAY:
        prices.time = prices.time.map(pd.Timestamp.normalize)

    return prices

#@log_function_call()
async def get_max_requests_per_second(token: str = TOKEN) -> float:
    async with AsyncClient(token) as client:
        unary_limits = (await client.users.get_user_tariff()).unary_limits
    max_per_second = [
        unary_limit.limit_per_minute
        for unary_limit in unary_limits
        for method in unary_limit.methods
        if "GetCandles" in method
    ][0] / 60
    return max_per_second

#@log_function_call()
async def get_prices_async(
    figis: List[str],
    start_date: pd.Timestamp,
    end_date: pd.Timestamp,
    max_per_second: Optional[float] = None,
    interval: CandleInterval = CandleInterval.CANDLE_INTERVAL_DAY,
    is_complete: bool = True,
    token: str = TOKEN,
) -> pd.DataFrame:
    if max_per_second is None:
        max_per_second = await get_max_requests_per_second()
    jobs = [
        functools.partial(
            get_prices_for_async,
            figi,
            start_date,
            end_date,
            interval,
            is_complete,
            token,
        )
        for figi in figis
    ]
    # please, check `aiometer.run_all` docs
    raw_prices = await aiometer.run_all(jobs, max_per_second=max_per_second)
    prices = pd.concat(raw_prices)
    return prices


#@log_function_call()
async def get_prices_for_async(
    figi: str,
    start_date: pd.Timestamp,
    end_date: pd.Timestamp,
    interval: CandleInterval = CandleInterval.CANDLE_INTERVAL_DAY,
    is_complete: bool = True,
    token: str = TOKEN,
):
    async with AsyncClient(token) as client:
        response = [
            candle
            async for candle in client.get_all_candles(
                figi=figi,
                from_=start_date,
                to=end_date,
                interval=interval,
            )
        ]
        raw_candles = _dataclasses_to_dict(response)
    prices = pd.DataFrame(raw_candles).assign(figi=figi)
    if prices.empty:
        logger.warning(f"No candles for {figi} ({start_date}-{end_date})")
        return prices
    if "is_complete" in prices.columns and is_complete:
        prices = prices.query("is_complete").copy()
    if interval == CandleInterval.CANDLE_INTERVAL_DAY:
        prices.time = prices.time.map(pd.Timestamp.normalize)
    return prices

#@log_function_call()
async def get_dividends_async(
    figis: List[str],
    start_date: pd.Timestamp,
    end_date: pd.Timestamp,
    max_per_second: Optional[float] = None,
    token: str = TOKEN,
) -> pd.DataFrame:
    if max_per_second is None:
        max_per_second = await get_max_requests_per_second()
    jobs = [
        functools.partial(
            get_dividends_for_async,
            figi,
            start_date,
            end_date,
            token,
        )
        for figi in figis
    ]
    raw_dividends = await aiometer.run_all(jobs, max_per_second=max_per_second)
    dividends = pd.concat(raw_dividends)
    return dividends


#@log_function_call()
def get_dividends_sync(
    figis: List[str],
    start_date: pd.Timestamp,
    end_date: pd.Timestamp,
    token: str = TOKEN,
) -> pd.DataFrame:
    return pd.concat([
        get_dividends_for_sync(
            figi, start_date, end_date, token
        )
        for figi in figis
    ])


#@log_function_call()
async def get_dividends_for_async(
    figi: str,
    start_date: pd.Timestamp,
    end_date: pd.Timestamp,
    token: str = TOKEN,
) -> pd.DataFrame:
    async with AsyncClient(token) as client:
        dividends = pd.json_normalize(
            _dataclasses_to_dict(
                (await client.instruments.get_dividends(
                    figi=figi,
                    from_=start_date,
                    to=end_date,
                )).dividends,
            )
        ).assign(figi=figi)
    if "dividend_type" in dividends.columns:
        dividends = dividends.query('dividend_type != "Cancelled"')
    if "payment_date" in dividends.columns:
        dividends = dividends.query("@end_date > payment_date > @start_date")
    return dividends


#@log_function_call()
def get_dividends_for_sync(
    figi: str,
    start_date: pd.Timestamp,
    end_date: pd.Timestamp,
    token: str = TOKEN,
) -> pd.DataFrame:
    with Client(token) as client:
        dividends = pd.json_normalize(
            _dataclasses_to_dict(
                client.instruments.get_dividends(
                    figi=figi,
                    from_=start_date,
                    to=end_date,
                ).dividends,
            )
        ).assign(figi=figi)
    if "dividend_type" in dividends.columns:
        dividends = dividends.query('dividend_type != "Cancelled"')
    if "payment_date" in dividends.columns:
        dividends = dividends.query("@end_date > payment_date > @start_date")
    return dividends


def get_shares_info_sync(token: str = TOKEN):
    with Client(token) as client:
        shares_resp = client.instruments.shares(instrument_status = InstrumentStatus.INSTRUMENT_STATUS_ALL)
    shares_df = pd.json_normalize(_dataclasses_to_dict(shares_resp.instruments))
    return shares_df

async def get_shares_info_async(token: str = TOKEN):
    async with AsyncClient(token) as client:
        shares_resp = await client.instruments.shares(instrument_status = InstrumentStatus.INSTRUMENT_STATUS_ALL)
    shares_df = pd.json_normalize(_dataclasses_to_dict(shares_resp.instruments))
    return shares_df

def get_raw_operations(
    account_id: str,
    token: str,
    from_: Optional[datetime.datetime] = None,
    to_: Optional[datetime.datetime] = None,
    state: OperationState = OperationState(0),
    figi: str = "",
) -> List[Operation]:
    """Get operations."""
    with Client(token) as client:
        operations = client.operations.get_operations(
            account_id=account_id,
            from_=from_,
            to=to_,
            state=state,
            figi=figi,
        ).operations
    return operations

def get_raw_positions(
    account_id: str,
    token: str,
) -> PositionsResponse:
    with Client(token) as client:
        positions = client.operations.get_positions(account_id=account_id)
    return positions

def get_raw_portfolio(
    account_id: str,
    token: str,
) -> PortfolioResponse:
    with Client(token) as client:
        portfolio = client.operations.get_portfolio(account_id=account_id)
    return portfolio
