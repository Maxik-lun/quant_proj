# orders service
import uuid
import datetime
import duckdb
from typing import List

from tinkoff.invest import (
    Client,
    OrderDirection,
    OrderState,
    OrderType,
)
from tinkoff.invest.typedefs import AccountId
from src.logging import log_function_call
from src.tinkoff_convert import _float_to_quotation, _dataclasses_to_dict, _money_value_to_float

class MockManager:
    def __init__(self, order_db = 'operations.duckdb', account_id: str = 'test') -> None:
        self.account_id = AccountId(account_id)
        self.order_db = order_db
        with duckdb.connect(self.order_db) as conn:
            conn.sql("""
                CREATE TABLE IF NOT EXISTS order_history (
                figi TEXT,
                quantity UINTEGER,
                price FLOAT,
                direction INTEGER,
                account_id TEXT,
                order_type INTEGER,
                order_id UUID,
                record_dtime TIMESTAMP
                );""")
    @log_function_call(level='INFO')
    def place_limit_order(self, figi: str, lots: int, price: float, is_buy: bool) -> dict:
        # TODO: check liquidity
        if is_buy:
            direction = OrderDirection.ORDER_DIRECTION_BUY
        else:
            direction = OrderDirection.ORDER_DIRECTION_SELL
        order_type = OrderType.ORDER_TYPE_LIMIT
        order_id = str(uuid.uuid4())
        record_dtime = datetime.datetime.now()
        # quotation = _float_to_quotation(price)
        order = dict(
            figi=figi,
            quantity=lots,
            price=price,
            direction=direction,
            account_id=self.account_id,
            order_type=order_type,
            order_id=order_id,
            record_dtime = record_dtime
            )
        with duckdb.connect(self.order_db) as conn:
            columns = ', '.join(order.keys())
            placeholders = ', '.join('?' * len(order))
            sql = 'INSERT INTO order_history ({}) VALUES ({})'.format(columns, placeholders)
            values = [int(x) if isinstance(x, bool) else x for x in order.values()]
            conn.execute(sql, values)
        return order


class SyncOrderManager:
    def __init__(self, account_id: str, token: str) -> None:
        self.account_id = AccountId(account_id)
        self.token = token

    @log_function_call(level='INFO')
    def _get_cash_on_account(self, currency: str) -> float:
        with Client(self.token) as client:
            positions = client.operations.get_positions(account_id=self.account_id)
        for money in positions.money:
            if money.currency == currency:
                return _money_value_to_float(money)
        return 0.0

    @log_function_call(level='INFO')
    def cancel_all_orders(self) -> None:
        with Client(self.token) as client:
            client.cancel_all_orders(account_id=self.account_id)
    
    @log_function_call(level='INFO')
    def place_limit_order(self, figi: str, lots: int, price: float, is_buy: bool) -> dict:
        # TODO: check liquidity
        if is_buy:
            direction = OrderDirection.ORDER_DIRECTION_BUY
        else:
            direction = OrderDirection.ORDER_DIRECTION_SELL
        order_type = OrderType.ORDER_TYPE_LIMIT
        order_id = str(uuid.uuid4())
        quotation = _float_to_quotation(price)
        with Client(self.token) as client:
            return _dataclasses_to_dict(
                client.orders.post_order(
                    figi=figi,
                    quantity=lots,
                    price=quotation,
                    direction=direction,
                    account_id=self.account_id,
                    order_type=order_type,
                    order_id=order_id,
                )
            )
