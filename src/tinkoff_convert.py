# converter utils for tinkoff classes
import datetime
import json
import types
from dataclasses import fields, is_dataclass
from decimal import Decimal
from typing import Any

import pandas as pd
from .logging import log_function_call
from tinkoff.invest import utils
from tinkoff.invest.schemas import (
    MoneyValue,
    Quotation,
    TradeDirection,
)


@log_function_call(level="TRACE")
def _dataclasses_to_dict(obj: Any, dict_factory=dict) -> Any:
    if isinstance(obj, types.GeneratorType):
        return _dataclasses_to_dict([*obj])
    if isinstance(obj, datetime.datetime):
        return _datetime_to_timestamp(obj)
    if isinstance(obj, MoneyValue):
        return _money_value_to_float(obj)
    if isinstance(obj, Quotation):
        return _quotation_to_float(obj)
    if isinstance(obj, TradeDirection):
        return int(obj)
    if is_dataclass(obj):
        return _dataclass_to_dict(obj, dict_factory=dict_factory)
    if isinstance(obj, tuple) and hasattr(obj, "_fields"):
        return type(obj)(*[_dataclasses_to_dict(v, dict_factory) for v in obj])
    if isinstance(obj, (list, tuple)):
        return type(obj)(_dataclasses_to_dict(v, dict_factory) for v in obj)
    if isinstance(obj, dict):
        return type(obj)(
            (_dataclasses_to_dict(k), _dataclasses_to_dict(v))
            for k, v in obj.items()
            if v is not None
        )
    return obj


@log_function_call(level="TRACE")
def _dataclass_to_dict(dataclass, dict_factory=dict) -> dict:
    result = []
    for field in fields(dataclass):
        value = _dataclasses_to_dict(
            getattr(dataclass, field.name),
            dict_factory,
        )
        result.append((field.name, value))
    return dict_factory(result)


@log_function_call(level="TRACE")
def _datetime_to_timestamp(datetime_: datetime.datetime):
    if datetime_.hour == 0 and datetime_.minute == 0:
        return pd.Timestamp(datetime_.replace(tzinfo=None))
    return pd.Timestamp(datetime_.astimezone(tz=None).replace(tzinfo=None))


@log_function_call(level="TRACE")
def _money_value_to_float(money_value: MoneyValue) -> float:
    fractional = money_value.nano / Decimal("10e8")
    return float(Decimal(money_value.units) + fractional)


@log_function_call(level="TRACE")
def _quotation_to_float(quotation: Quotation) -> float:
    return float(utils.quotation_to_decimal(quotation))


@log_function_call(level="TRACE")
def _float_to_quotation(float_: float):
    return utils.decimal_to_quotation(Decimal(float_))