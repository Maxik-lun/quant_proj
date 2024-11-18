from google.protobuf import timestamp_pb2 as _timestamp_pb2
from tinvest.grpc.google.api import field_behavior_pb2 as _field_behavior_pb2
from tinvest.grpc import common_pb2 as _common_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class StopOrderDirection(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    STOP_ORDER_DIRECTION_UNSPECIFIED: _ClassVar[StopOrderDirection]
    STOP_ORDER_DIRECTION_BUY: _ClassVar[StopOrderDirection]
    STOP_ORDER_DIRECTION_SELL: _ClassVar[StopOrderDirection]

class StopOrderExpirationType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    STOP_ORDER_EXPIRATION_TYPE_UNSPECIFIED: _ClassVar[StopOrderExpirationType]
    STOP_ORDER_EXPIRATION_TYPE_GOOD_TILL_CANCEL: _ClassVar[StopOrderExpirationType]
    STOP_ORDER_EXPIRATION_TYPE_GOOD_TILL_DATE: _ClassVar[StopOrderExpirationType]

class StopOrderType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    STOP_ORDER_TYPE_UNSPECIFIED: _ClassVar[StopOrderType]
    STOP_ORDER_TYPE_TAKE_PROFIT: _ClassVar[StopOrderType]
    STOP_ORDER_TYPE_STOP_LOSS: _ClassVar[StopOrderType]
    STOP_ORDER_TYPE_STOP_LIMIT: _ClassVar[StopOrderType]

class StopOrderStatusOption(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    STOP_ORDER_STATUS_UNSPECIFIED: _ClassVar[StopOrderStatusOption]
    STOP_ORDER_STATUS_ALL: _ClassVar[StopOrderStatusOption]
    STOP_ORDER_STATUS_ACTIVE: _ClassVar[StopOrderStatusOption]
    STOP_ORDER_STATUS_EXECUTED: _ClassVar[StopOrderStatusOption]
    STOP_ORDER_STATUS_CANCELED: _ClassVar[StopOrderStatusOption]
    STOP_ORDER_STATUS_EXPIRED: _ClassVar[StopOrderStatusOption]

class ExchangeOrderType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EXCHANGE_ORDER_TYPE_UNSPECIFIED: _ClassVar[ExchangeOrderType]
    EXCHANGE_ORDER_TYPE_MARKET: _ClassVar[ExchangeOrderType]
    EXCHANGE_ORDER_TYPE_LIMIT: _ClassVar[ExchangeOrderType]

class TakeProfitType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TAKE_PROFIT_TYPE_UNSPECIFIED: _ClassVar[TakeProfitType]
    TAKE_PROFIT_TYPE_REGULAR: _ClassVar[TakeProfitType]
    TAKE_PROFIT_TYPE_TRAILING: _ClassVar[TakeProfitType]

class TrailingValueType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TRAILING_VALUE_UNSPECIFIED: _ClassVar[TrailingValueType]
    TRAILING_VALUE_ABSOLUTE: _ClassVar[TrailingValueType]
    TRAILING_VALUE_RELATIVE: _ClassVar[TrailingValueType]

class TrailingStopStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TRAILING_STOP_UNSPECIFIED: _ClassVar[TrailingStopStatus]
    TRAILING_STOP_ACTIVE: _ClassVar[TrailingStopStatus]
    TRAILING_STOP_ACTIVATED: _ClassVar[TrailingStopStatus]
STOP_ORDER_DIRECTION_UNSPECIFIED: StopOrderDirection
STOP_ORDER_DIRECTION_BUY: StopOrderDirection
STOP_ORDER_DIRECTION_SELL: StopOrderDirection
STOP_ORDER_EXPIRATION_TYPE_UNSPECIFIED: StopOrderExpirationType
STOP_ORDER_EXPIRATION_TYPE_GOOD_TILL_CANCEL: StopOrderExpirationType
STOP_ORDER_EXPIRATION_TYPE_GOOD_TILL_DATE: StopOrderExpirationType
STOP_ORDER_TYPE_UNSPECIFIED: StopOrderType
STOP_ORDER_TYPE_TAKE_PROFIT: StopOrderType
STOP_ORDER_TYPE_STOP_LOSS: StopOrderType
STOP_ORDER_TYPE_STOP_LIMIT: StopOrderType
STOP_ORDER_STATUS_UNSPECIFIED: StopOrderStatusOption
STOP_ORDER_STATUS_ALL: StopOrderStatusOption
STOP_ORDER_STATUS_ACTIVE: StopOrderStatusOption
STOP_ORDER_STATUS_EXECUTED: StopOrderStatusOption
STOP_ORDER_STATUS_CANCELED: StopOrderStatusOption
STOP_ORDER_STATUS_EXPIRED: StopOrderStatusOption
EXCHANGE_ORDER_TYPE_UNSPECIFIED: ExchangeOrderType
EXCHANGE_ORDER_TYPE_MARKET: ExchangeOrderType
EXCHANGE_ORDER_TYPE_LIMIT: ExchangeOrderType
TAKE_PROFIT_TYPE_UNSPECIFIED: TakeProfitType
TAKE_PROFIT_TYPE_REGULAR: TakeProfitType
TAKE_PROFIT_TYPE_TRAILING: TakeProfitType
TRAILING_VALUE_UNSPECIFIED: TrailingValueType
TRAILING_VALUE_ABSOLUTE: TrailingValueType
TRAILING_VALUE_RELATIVE: TrailingValueType
TRAILING_STOP_UNSPECIFIED: TrailingStopStatus
TRAILING_STOP_ACTIVE: TrailingStopStatus
TRAILING_STOP_ACTIVATED: TrailingStopStatus

class PostStopOrderRequest(_message.Message):
    __slots__ = ("figi", "quantity", "price", "stop_price", "direction", "account_id", "expiration_type", "stop_order_type", "expire_date", "instrument_id", "exchange_order_type", "take_profit_type", "trailing_data", "price_type", "order_id")
    class TrailingData(_message.Message):
        __slots__ = ("indent", "indent_type", "spread", "spread_type")
        INDENT_FIELD_NUMBER: _ClassVar[int]
        INDENT_TYPE_FIELD_NUMBER: _ClassVar[int]
        SPREAD_FIELD_NUMBER: _ClassVar[int]
        SPREAD_TYPE_FIELD_NUMBER: _ClassVar[int]
        indent: _common_pb2.Quotation
        indent_type: TrailingValueType
        spread: _common_pb2.Quotation
        spread_type: TrailingValueType
        def __init__(self, indent: _Optional[_Union[_common_pb2.Quotation, _Mapping]] = ..., indent_type: _Optional[_Union[TrailingValueType, str]] = ..., spread: _Optional[_Union[_common_pb2.Quotation, _Mapping]] = ..., spread_type: _Optional[_Union[TrailingValueType, str]] = ...) -> None: ...
    FIGI_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    STOP_PRICE_FIELD_NUMBER: _ClassVar[int]
    DIRECTION_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    EXPIRATION_TYPE_FIELD_NUMBER: _ClassVar[int]
    STOP_ORDER_TYPE_FIELD_NUMBER: _ClassVar[int]
    EXPIRE_DATE_FIELD_NUMBER: _ClassVar[int]
    INSTRUMENT_ID_FIELD_NUMBER: _ClassVar[int]
    EXCHANGE_ORDER_TYPE_FIELD_NUMBER: _ClassVar[int]
    TAKE_PROFIT_TYPE_FIELD_NUMBER: _ClassVar[int]
    TRAILING_DATA_FIELD_NUMBER: _ClassVar[int]
    PRICE_TYPE_FIELD_NUMBER: _ClassVar[int]
    ORDER_ID_FIELD_NUMBER: _ClassVar[int]
    figi: str
    quantity: int
    price: _common_pb2.Quotation
    stop_price: _common_pb2.Quotation
    direction: StopOrderDirection
    account_id: str
    expiration_type: StopOrderExpirationType
    stop_order_type: StopOrderType
    expire_date: _timestamp_pb2.Timestamp
    instrument_id: str
    exchange_order_type: ExchangeOrderType
    take_profit_type: TakeProfitType
    trailing_data: PostStopOrderRequest.TrailingData
    price_type: _common_pb2.PriceType
    order_id: str
    def __init__(self, figi: _Optional[str] = ..., quantity: _Optional[int] = ..., price: _Optional[_Union[_common_pb2.Quotation, _Mapping]] = ..., stop_price: _Optional[_Union[_common_pb2.Quotation, _Mapping]] = ..., direction: _Optional[_Union[StopOrderDirection, str]] = ..., account_id: _Optional[str] = ..., expiration_type: _Optional[_Union[StopOrderExpirationType, str]] = ..., stop_order_type: _Optional[_Union[StopOrderType, str]] = ..., expire_date: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., instrument_id: _Optional[str] = ..., exchange_order_type: _Optional[_Union[ExchangeOrderType, str]] = ..., take_profit_type: _Optional[_Union[TakeProfitType, str]] = ..., trailing_data: _Optional[_Union[PostStopOrderRequest.TrailingData, _Mapping]] = ..., price_type: _Optional[_Union[_common_pb2.PriceType, str]] = ..., order_id: _Optional[str] = ...) -> None: ...

class PostStopOrderResponse(_message.Message):
    __slots__ = ("stop_order_id", "order_request_id", "response_metadata")
    STOP_ORDER_ID_FIELD_NUMBER: _ClassVar[int]
    ORDER_REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_METADATA_FIELD_NUMBER: _ClassVar[int]
    stop_order_id: str
    order_request_id: str
    response_metadata: _common_pb2.ResponseMetadata
    def __init__(self, stop_order_id: _Optional[str] = ..., order_request_id: _Optional[str] = ..., response_metadata: _Optional[_Union[_common_pb2.ResponseMetadata, _Mapping]] = ...) -> None: ...

class GetStopOrdersRequest(_message.Message):
    __slots__ = ("account_id", "status", "to")
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    FROM_FIELD_NUMBER: _ClassVar[int]
    TO_FIELD_NUMBER: _ClassVar[int]
    account_id: str
    status: StopOrderStatusOption
    to: _timestamp_pb2.Timestamp
    def __init__(self, account_id: _Optional[str] = ..., status: _Optional[_Union[StopOrderStatusOption, str]] = ..., to: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., **kwargs) -> None: ...

class GetStopOrdersResponse(_message.Message):
    __slots__ = ("stop_orders",)
    STOP_ORDERS_FIELD_NUMBER: _ClassVar[int]
    stop_orders: _containers.RepeatedCompositeFieldContainer[StopOrder]
    def __init__(self, stop_orders: _Optional[_Iterable[_Union[StopOrder, _Mapping]]] = ...) -> None: ...

class CancelStopOrderRequest(_message.Message):
    __slots__ = ("account_id", "stop_order_id")
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    STOP_ORDER_ID_FIELD_NUMBER: _ClassVar[int]
    account_id: str
    stop_order_id: str
    def __init__(self, account_id: _Optional[str] = ..., stop_order_id: _Optional[str] = ...) -> None: ...

class CancelStopOrderResponse(_message.Message):
    __slots__ = ("time",)
    TIME_FIELD_NUMBER: _ClassVar[int]
    time: _timestamp_pb2.Timestamp
    def __init__(self, time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class StopOrder(_message.Message):
    __slots__ = ("stop_order_id", "lots_requested", "figi", "direction", "currency", "order_type", "create_date", "activation_date_time", "expiration_time", "price", "stop_price", "instrument_uid", "take_profit_type", "trailing_data", "status", "exchange_order_type", "exchange_order_id")
    class TrailingData(_message.Message):
        __slots__ = ("indent", "indent_type", "spread", "spread_type", "status", "price", "extr")
        INDENT_FIELD_NUMBER: _ClassVar[int]
        INDENT_TYPE_FIELD_NUMBER: _ClassVar[int]
        SPREAD_FIELD_NUMBER: _ClassVar[int]
        SPREAD_TYPE_FIELD_NUMBER: _ClassVar[int]
        STATUS_FIELD_NUMBER: _ClassVar[int]
        PRICE_FIELD_NUMBER: _ClassVar[int]
        EXTR_FIELD_NUMBER: _ClassVar[int]
        indent: _common_pb2.Quotation
        indent_type: TrailingValueType
        spread: _common_pb2.Quotation
        spread_type: TrailingValueType
        status: TrailingStopStatus
        price: _common_pb2.Quotation
        extr: _common_pb2.Quotation
        def __init__(self, indent: _Optional[_Union[_common_pb2.Quotation, _Mapping]] = ..., indent_type: _Optional[_Union[TrailingValueType, str]] = ..., spread: _Optional[_Union[_common_pb2.Quotation, _Mapping]] = ..., spread_type: _Optional[_Union[TrailingValueType, str]] = ..., status: _Optional[_Union[TrailingStopStatus, str]] = ..., price: _Optional[_Union[_common_pb2.Quotation, _Mapping]] = ..., extr: _Optional[_Union[_common_pb2.Quotation, _Mapping]] = ...) -> None: ...
    STOP_ORDER_ID_FIELD_NUMBER: _ClassVar[int]
    LOTS_REQUESTED_FIELD_NUMBER: _ClassVar[int]
    FIGI_FIELD_NUMBER: _ClassVar[int]
    DIRECTION_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_FIELD_NUMBER: _ClassVar[int]
    ORDER_TYPE_FIELD_NUMBER: _ClassVar[int]
    CREATE_DATE_FIELD_NUMBER: _ClassVar[int]
    ACTIVATION_DATE_TIME_FIELD_NUMBER: _ClassVar[int]
    EXPIRATION_TIME_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    STOP_PRICE_FIELD_NUMBER: _ClassVar[int]
    INSTRUMENT_UID_FIELD_NUMBER: _ClassVar[int]
    TAKE_PROFIT_TYPE_FIELD_NUMBER: _ClassVar[int]
    TRAILING_DATA_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    EXCHANGE_ORDER_TYPE_FIELD_NUMBER: _ClassVar[int]
    EXCHANGE_ORDER_ID_FIELD_NUMBER: _ClassVar[int]
    stop_order_id: str
    lots_requested: int
    figi: str
    direction: StopOrderDirection
    currency: str
    order_type: StopOrderType
    create_date: _timestamp_pb2.Timestamp
    activation_date_time: _timestamp_pb2.Timestamp
    expiration_time: _timestamp_pb2.Timestamp
    price: _common_pb2.MoneyValue
    stop_price: _common_pb2.MoneyValue
    instrument_uid: str
    take_profit_type: TakeProfitType
    trailing_data: StopOrder.TrailingData
    status: StopOrderStatusOption
    exchange_order_type: ExchangeOrderType
    exchange_order_id: str
    def __init__(self, stop_order_id: _Optional[str] = ..., lots_requested: _Optional[int] = ..., figi: _Optional[str] = ..., direction: _Optional[_Union[StopOrderDirection, str]] = ..., currency: _Optional[str] = ..., order_type: _Optional[_Union[StopOrderType, str]] = ..., create_date: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., activation_date_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., expiration_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., price: _Optional[_Union[_common_pb2.MoneyValue, _Mapping]] = ..., stop_price: _Optional[_Union[_common_pb2.MoneyValue, _Mapping]] = ..., instrument_uid: _Optional[str] = ..., take_profit_type: _Optional[_Union[TakeProfitType, str]] = ..., trailing_data: _Optional[_Union[StopOrder.TrailingData, _Mapping]] = ..., status: _Optional[_Union[StopOrderStatusOption, str]] = ..., exchange_order_type: _Optional[_Union[ExchangeOrderType, str]] = ..., exchange_order_id: _Optional[str] = ...) -> None: ...
