from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class InstrumentType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    INSTRUMENT_TYPE_UNSPECIFIED: _ClassVar[InstrumentType]
    INSTRUMENT_TYPE_BOND: _ClassVar[InstrumentType]
    INSTRUMENT_TYPE_SHARE: _ClassVar[InstrumentType]
    INSTRUMENT_TYPE_CURRENCY: _ClassVar[InstrumentType]
    INSTRUMENT_TYPE_ETF: _ClassVar[InstrumentType]
    INSTRUMENT_TYPE_FUTURES: _ClassVar[InstrumentType]
    INSTRUMENT_TYPE_SP: _ClassVar[InstrumentType]
    INSTRUMENT_TYPE_OPTION: _ClassVar[InstrumentType]
    INSTRUMENT_TYPE_CLEARING_CERTIFICATE: _ClassVar[InstrumentType]
    INSTRUMENT_TYPE_INDEX: _ClassVar[InstrumentType]
    INSTRUMENT_TYPE_COMMODITY: _ClassVar[InstrumentType]

class SecurityTradingStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SECURITY_TRADING_STATUS_UNSPECIFIED: _ClassVar[SecurityTradingStatus]
    SECURITY_TRADING_STATUS_NOT_AVAILABLE_FOR_TRADING: _ClassVar[SecurityTradingStatus]
    SECURITY_TRADING_STATUS_OPENING_PERIOD: _ClassVar[SecurityTradingStatus]
    SECURITY_TRADING_STATUS_CLOSING_PERIOD: _ClassVar[SecurityTradingStatus]
    SECURITY_TRADING_STATUS_BREAK_IN_TRADING: _ClassVar[SecurityTradingStatus]
    SECURITY_TRADING_STATUS_NORMAL_TRADING: _ClassVar[SecurityTradingStatus]
    SECURITY_TRADING_STATUS_CLOSING_AUCTION: _ClassVar[SecurityTradingStatus]
    SECURITY_TRADING_STATUS_DARK_POOL_AUCTION: _ClassVar[SecurityTradingStatus]
    SECURITY_TRADING_STATUS_DISCRETE_AUCTION: _ClassVar[SecurityTradingStatus]
    SECURITY_TRADING_STATUS_OPENING_AUCTION_PERIOD: _ClassVar[SecurityTradingStatus]
    SECURITY_TRADING_STATUS_TRADING_AT_CLOSING_AUCTION_PRICE: _ClassVar[SecurityTradingStatus]
    SECURITY_TRADING_STATUS_SESSION_ASSIGNED: _ClassVar[SecurityTradingStatus]
    SECURITY_TRADING_STATUS_SESSION_CLOSE: _ClassVar[SecurityTradingStatus]
    SECURITY_TRADING_STATUS_SESSION_OPEN: _ClassVar[SecurityTradingStatus]
    SECURITY_TRADING_STATUS_DEALER_NORMAL_TRADING: _ClassVar[SecurityTradingStatus]
    SECURITY_TRADING_STATUS_DEALER_BREAK_IN_TRADING: _ClassVar[SecurityTradingStatus]
    SECURITY_TRADING_STATUS_DEALER_NOT_AVAILABLE_FOR_TRADING: _ClassVar[SecurityTradingStatus]

class PriceType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PRICE_TYPE_UNSPECIFIED: _ClassVar[PriceType]
    PRICE_TYPE_POINT: _ClassVar[PriceType]
    PRICE_TYPE_CURRENCY: _ClassVar[PriceType]

class ResultSubscriptionStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    RESULT_SUBSCRIPTION_STATUS_UNSPECIFIED: _ClassVar[ResultSubscriptionStatus]
    RESULT_SUBSCRIPTION_STATUS_OK: _ClassVar[ResultSubscriptionStatus]
    RESULT_SUBSCRIPTION_STATUS_ERROR: _ClassVar[ResultSubscriptionStatus]
INSTRUMENT_TYPE_UNSPECIFIED: InstrumentType
INSTRUMENT_TYPE_BOND: InstrumentType
INSTRUMENT_TYPE_SHARE: InstrumentType
INSTRUMENT_TYPE_CURRENCY: InstrumentType
INSTRUMENT_TYPE_ETF: InstrumentType
INSTRUMENT_TYPE_FUTURES: InstrumentType
INSTRUMENT_TYPE_SP: InstrumentType
INSTRUMENT_TYPE_OPTION: InstrumentType
INSTRUMENT_TYPE_CLEARING_CERTIFICATE: InstrumentType
INSTRUMENT_TYPE_INDEX: InstrumentType
INSTRUMENT_TYPE_COMMODITY: InstrumentType
SECURITY_TRADING_STATUS_UNSPECIFIED: SecurityTradingStatus
SECURITY_TRADING_STATUS_NOT_AVAILABLE_FOR_TRADING: SecurityTradingStatus
SECURITY_TRADING_STATUS_OPENING_PERIOD: SecurityTradingStatus
SECURITY_TRADING_STATUS_CLOSING_PERIOD: SecurityTradingStatus
SECURITY_TRADING_STATUS_BREAK_IN_TRADING: SecurityTradingStatus
SECURITY_TRADING_STATUS_NORMAL_TRADING: SecurityTradingStatus
SECURITY_TRADING_STATUS_CLOSING_AUCTION: SecurityTradingStatus
SECURITY_TRADING_STATUS_DARK_POOL_AUCTION: SecurityTradingStatus
SECURITY_TRADING_STATUS_DISCRETE_AUCTION: SecurityTradingStatus
SECURITY_TRADING_STATUS_OPENING_AUCTION_PERIOD: SecurityTradingStatus
SECURITY_TRADING_STATUS_TRADING_AT_CLOSING_AUCTION_PRICE: SecurityTradingStatus
SECURITY_TRADING_STATUS_SESSION_ASSIGNED: SecurityTradingStatus
SECURITY_TRADING_STATUS_SESSION_CLOSE: SecurityTradingStatus
SECURITY_TRADING_STATUS_SESSION_OPEN: SecurityTradingStatus
SECURITY_TRADING_STATUS_DEALER_NORMAL_TRADING: SecurityTradingStatus
SECURITY_TRADING_STATUS_DEALER_BREAK_IN_TRADING: SecurityTradingStatus
SECURITY_TRADING_STATUS_DEALER_NOT_AVAILABLE_FOR_TRADING: SecurityTradingStatus
PRICE_TYPE_UNSPECIFIED: PriceType
PRICE_TYPE_POINT: PriceType
PRICE_TYPE_CURRENCY: PriceType
RESULT_SUBSCRIPTION_STATUS_UNSPECIFIED: ResultSubscriptionStatus
RESULT_SUBSCRIPTION_STATUS_OK: ResultSubscriptionStatus
RESULT_SUBSCRIPTION_STATUS_ERROR: ResultSubscriptionStatus

class MoneyValue(_message.Message):
    __slots__ = ("currency", "units", "nano")
    CURRENCY_FIELD_NUMBER: _ClassVar[int]
    UNITS_FIELD_NUMBER: _ClassVar[int]
    NANO_FIELD_NUMBER: _ClassVar[int]
    currency: str
    units: int
    nano: int
    def __init__(self, currency: _Optional[str] = ..., units: _Optional[int] = ..., nano: _Optional[int] = ...) -> None: ...

class Quotation(_message.Message):
    __slots__ = ("units", "nano")
    UNITS_FIELD_NUMBER: _ClassVar[int]
    NANO_FIELD_NUMBER: _ClassVar[int]
    units: int
    nano: int
    def __init__(self, units: _Optional[int] = ..., nano: _Optional[int] = ...) -> None: ...

class Ping(_message.Message):
    __slots__ = ("time", "stream_id")
    TIME_FIELD_NUMBER: _ClassVar[int]
    STREAM_ID_FIELD_NUMBER: _ClassVar[int]
    time: _timestamp_pb2.Timestamp
    stream_id: str
    def __init__(self, time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., stream_id: _Optional[str] = ...) -> None: ...

class Page(_message.Message):
    __slots__ = ("limit", "page_number")
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    PAGE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    limit: int
    page_number: int
    def __init__(self, limit: _Optional[int] = ..., page_number: _Optional[int] = ...) -> None: ...

class PageResponse(_message.Message):
    __slots__ = ("limit", "page_number", "total_count")
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    PAGE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    TOTAL_COUNT_FIELD_NUMBER: _ClassVar[int]
    limit: int
    page_number: int
    total_count: int
    def __init__(self, limit: _Optional[int] = ..., page_number: _Optional[int] = ..., total_count: _Optional[int] = ...) -> None: ...

class ResponseMetadata(_message.Message):
    __slots__ = ("tracking_id", "server_time")
    TRACKING_ID_FIELD_NUMBER: _ClassVar[int]
    SERVER_TIME_FIELD_NUMBER: _ClassVar[int]
    tracking_id: str
    server_time: _timestamp_pb2.Timestamp
    def __init__(self, tracking_id: _Optional[str] = ..., server_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class BrandData(_message.Message):
    __slots__ = ("logo_name", "logo_base_color", "text_color")
    LOGO_NAME_FIELD_NUMBER: _ClassVar[int]
    LOGO_BASE_COLOR_FIELD_NUMBER: _ClassVar[int]
    TEXT_COLOR_FIELD_NUMBER: _ClassVar[int]
    logo_name: str
    logo_base_color: str
    text_color: str
    def __init__(self, logo_name: _Optional[str] = ..., logo_base_color: _Optional[str] = ..., text_color: _Optional[str] = ...) -> None: ...

class ErrorDetail(_message.Message):
    __slots__ = ("code", "message")
    CODE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    code: str
    message: str
    def __init__(self, code: _Optional[str] = ..., message: _Optional[str] = ...) -> None: ...
