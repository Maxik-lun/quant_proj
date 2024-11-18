from tinvest.grpc import common_pb2 as _common_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from tinvest.grpc.google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class OrderDirection(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ORDER_DIRECTION_UNSPECIFIED: _ClassVar[OrderDirection]
    ORDER_DIRECTION_BUY: _ClassVar[OrderDirection]
    ORDER_DIRECTION_SELL: _ClassVar[OrderDirection]

class OrderType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ORDER_TYPE_UNSPECIFIED: _ClassVar[OrderType]
    ORDER_TYPE_LIMIT: _ClassVar[OrderType]
    ORDER_TYPE_MARKET: _ClassVar[OrderType]
    ORDER_TYPE_BESTPRICE: _ClassVar[OrderType]

class OrderExecutionReportStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EXECUTION_REPORT_STATUS_UNSPECIFIED: _ClassVar[OrderExecutionReportStatus]
    EXECUTION_REPORT_STATUS_FILL: _ClassVar[OrderExecutionReportStatus]
    EXECUTION_REPORT_STATUS_REJECTED: _ClassVar[OrderExecutionReportStatus]
    EXECUTION_REPORT_STATUS_CANCELLED: _ClassVar[OrderExecutionReportStatus]
    EXECUTION_REPORT_STATUS_NEW: _ClassVar[OrderExecutionReportStatus]
    EXECUTION_REPORT_STATUS_PARTIALLYFILL: _ClassVar[OrderExecutionReportStatus]

class TimeInForceType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TIME_IN_FORCE_UNSPECIFIED: _ClassVar[TimeInForceType]
    TIME_IN_FORCE_DAY: _ClassVar[TimeInForceType]
    TIME_IN_FORCE_FILL_AND_KILL: _ClassVar[TimeInForceType]
    TIME_IN_FORCE_FILL_OR_KILL: _ClassVar[TimeInForceType]

class OrderIdType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ORDER_ID_TYPE_UNSPECIFIED: _ClassVar[OrderIdType]
    ORDER_ID_TYPE_EXCHANGE: _ClassVar[OrderIdType]
    ORDER_ID_TYPE_REQUEST: _ClassVar[OrderIdType]
ORDER_DIRECTION_UNSPECIFIED: OrderDirection
ORDER_DIRECTION_BUY: OrderDirection
ORDER_DIRECTION_SELL: OrderDirection
ORDER_TYPE_UNSPECIFIED: OrderType
ORDER_TYPE_LIMIT: OrderType
ORDER_TYPE_MARKET: OrderType
ORDER_TYPE_BESTPRICE: OrderType
EXECUTION_REPORT_STATUS_UNSPECIFIED: OrderExecutionReportStatus
EXECUTION_REPORT_STATUS_FILL: OrderExecutionReportStatus
EXECUTION_REPORT_STATUS_REJECTED: OrderExecutionReportStatus
EXECUTION_REPORT_STATUS_CANCELLED: OrderExecutionReportStatus
EXECUTION_REPORT_STATUS_NEW: OrderExecutionReportStatus
EXECUTION_REPORT_STATUS_PARTIALLYFILL: OrderExecutionReportStatus
TIME_IN_FORCE_UNSPECIFIED: TimeInForceType
TIME_IN_FORCE_DAY: TimeInForceType
TIME_IN_FORCE_FILL_AND_KILL: TimeInForceType
TIME_IN_FORCE_FILL_OR_KILL: TimeInForceType
ORDER_ID_TYPE_UNSPECIFIED: OrderIdType
ORDER_ID_TYPE_EXCHANGE: OrderIdType
ORDER_ID_TYPE_REQUEST: OrderIdType

class TradesStreamRequest(_message.Message):
    __slots__ = ("accounts",)
    ACCOUNTS_FIELD_NUMBER: _ClassVar[int]
    accounts: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, accounts: _Optional[_Iterable[str]] = ...) -> None: ...

class TradesStreamResponse(_message.Message):
    __slots__ = ("order_trades", "ping", "subscription")
    ORDER_TRADES_FIELD_NUMBER: _ClassVar[int]
    PING_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIPTION_FIELD_NUMBER: _ClassVar[int]
    order_trades: OrderTrades
    ping: _common_pb2.Ping
    subscription: SubscriptionResponse
    def __init__(self, order_trades: _Optional[_Union[OrderTrades, _Mapping]] = ..., ping: _Optional[_Union[_common_pb2.Ping, _Mapping]] = ..., subscription: _Optional[_Union[SubscriptionResponse, _Mapping]] = ...) -> None: ...

class OrderTrades(_message.Message):
    __slots__ = ("order_id", "created_at", "direction", "figi", "trades", "account_id", "instrument_uid")
    ORDER_ID_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    DIRECTION_FIELD_NUMBER: _ClassVar[int]
    FIGI_FIELD_NUMBER: _ClassVar[int]
    TRADES_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    INSTRUMENT_UID_FIELD_NUMBER: _ClassVar[int]
    order_id: str
    created_at: _timestamp_pb2.Timestamp
    direction: OrderDirection
    figi: str
    trades: _containers.RepeatedCompositeFieldContainer[OrderTrade]
    account_id: str
    instrument_uid: str
    def __init__(self, order_id: _Optional[str] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., direction: _Optional[_Union[OrderDirection, str]] = ..., figi: _Optional[str] = ..., trades: _Optional[_Iterable[_Union[OrderTrade, _Mapping]]] = ..., account_id: _Optional[str] = ..., instrument_uid: _Optional[str] = ...) -> None: ...

class OrderTrade(_message.Message):
    __slots__ = ("date_time", "price", "quantity", "trade_id")
    DATE_TIME_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    TRADE_ID_FIELD_NUMBER: _ClassVar[int]
    date_time: _timestamp_pb2.Timestamp
    price: _common_pb2.Quotation
    quantity: int
    trade_id: str
    def __init__(self, date_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., price: _Optional[_Union[_common_pb2.Quotation, _Mapping]] = ..., quantity: _Optional[int] = ..., trade_id: _Optional[str] = ...) -> None: ...

class PostOrderRequest(_message.Message):
    __slots__ = ("figi", "quantity", "price", "direction", "account_id", "order_type", "order_id", "instrument_id", "time_in_force", "price_type")
    FIGI_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    DIRECTION_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    ORDER_TYPE_FIELD_NUMBER: _ClassVar[int]
    ORDER_ID_FIELD_NUMBER: _ClassVar[int]
    INSTRUMENT_ID_FIELD_NUMBER: _ClassVar[int]
    TIME_IN_FORCE_FIELD_NUMBER: _ClassVar[int]
    PRICE_TYPE_FIELD_NUMBER: _ClassVar[int]
    figi: str
    quantity: int
    price: _common_pb2.Quotation
    direction: OrderDirection
    account_id: str
    order_type: OrderType
    order_id: str
    instrument_id: str
    time_in_force: TimeInForceType
    price_type: _common_pb2.PriceType
    def __init__(self, figi: _Optional[str] = ..., quantity: _Optional[int] = ..., price: _Optional[_Union[_common_pb2.Quotation, _Mapping]] = ..., direction: _Optional[_Union[OrderDirection, str]] = ..., account_id: _Optional[str] = ..., order_type: _Optional[_Union[OrderType, str]] = ..., order_id: _Optional[str] = ..., instrument_id: _Optional[str] = ..., time_in_force: _Optional[_Union[TimeInForceType, str]] = ..., price_type: _Optional[_Union[_common_pb2.PriceType, str]] = ...) -> None: ...

class PostOrderResponse(_message.Message):
    __slots__ = ("order_id", "execution_report_status", "lots_requested", "lots_executed", "initial_order_price", "executed_order_price", "total_order_amount", "initial_commission", "executed_commission", "aci_value", "figi", "direction", "initial_security_price", "order_type", "message", "initial_order_price_pt", "instrument_uid", "order_request_id", "response_metadata")
    ORDER_ID_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_REPORT_STATUS_FIELD_NUMBER: _ClassVar[int]
    LOTS_REQUESTED_FIELD_NUMBER: _ClassVar[int]
    LOTS_EXECUTED_FIELD_NUMBER: _ClassVar[int]
    INITIAL_ORDER_PRICE_FIELD_NUMBER: _ClassVar[int]
    EXECUTED_ORDER_PRICE_FIELD_NUMBER: _ClassVar[int]
    TOTAL_ORDER_AMOUNT_FIELD_NUMBER: _ClassVar[int]
    INITIAL_COMMISSION_FIELD_NUMBER: _ClassVar[int]
    EXECUTED_COMMISSION_FIELD_NUMBER: _ClassVar[int]
    ACI_VALUE_FIELD_NUMBER: _ClassVar[int]
    FIGI_FIELD_NUMBER: _ClassVar[int]
    DIRECTION_FIELD_NUMBER: _ClassVar[int]
    INITIAL_SECURITY_PRICE_FIELD_NUMBER: _ClassVar[int]
    ORDER_TYPE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    INITIAL_ORDER_PRICE_PT_FIELD_NUMBER: _ClassVar[int]
    INSTRUMENT_UID_FIELD_NUMBER: _ClassVar[int]
    ORDER_REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_METADATA_FIELD_NUMBER: _ClassVar[int]
    order_id: str
    execution_report_status: OrderExecutionReportStatus
    lots_requested: int
    lots_executed: int
    initial_order_price: _common_pb2.MoneyValue
    executed_order_price: _common_pb2.MoneyValue
    total_order_amount: _common_pb2.MoneyValue
    initial_commission: _common_pb2.MoneyValue
    executed_commission: _common_pb2.MoneyValue
    aci_value: _common_pb2.MoneyValue
    figi: str
    direction: OrderDirection
    initial_security_price: _common_pb2.MoneyValue
    order_type: OrderType
    message: str
    initial_order_price_pt: _common_pb2.Quotation
    instrument_uid: str
    order_request_id: str
    response_metadata: _common_pb2.ResponseMetadata
    def __init__(self, order_id: _Optional[str] = ..., execution_report_status: _Optional[_Union[OrderExecutionReportStatus, str]] = ..., lots_requested: _Optional[int] = ..., lots_executed: _Optional[int] = ..., initial_order_price: _Optional[_Union[_common_pb2.MoneyValue, _Mapping]] = ..., executed_order_price: _Optional[_Union[_common_pb2.MoneyValue, _Mapping]] = ..., total_order_amount: _Optional[_Union[_common_pb2.MoneyValue, _Mapping]] = ..., initial_commission: _Optional[_Union[_common_pb2.MoneyValue, _Mapping]] = ..., executed_commission: _Optional[_Union[_common_pb2.MoneyValue, _Mapping]] = ..., aci_value: _Optional[_Union[_common_pb2.MoneyValue, _Mapping]] = ..., figi: _Optional[str] = ..., direction: _Optional[_Union[OrderDirection, str]] = ..., initial_security_price: _Optional[_Union[_common_pb2.MoneyValue, _Mapping]] = ..., order_type: _Optional[_Union[OrderType, str]] = ..., message: _Optional[str] = ..., initial_order_price_pt: _Optional[_Union[_common_pb2.Quotation, _Mapping]] = ..., instrument_uid: _Optional[str] = ..., order_request_id: _Optional[str] = ..., response_metadata: _Optional[_Union[_common_pb2.ResponseMetadata, _Mapping]] = ...) -> None: ...

class PostOrderAsyncRequest(_message.Message):
    __slots__ = ("instrument_id", "quantity", "price", "direction", "account_id", "order_type", "order_id", "time_in_force", "price_type")
    INSTRUMENT_ID_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    DIRECTION_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    ORDER_TYPE_FIELD_NUMBER: _ClassVar[int]
    ORDER_ID_FIELD_NUMBER: _ClassVar[int]
    TIME_IN_FORCE_FIELD_NUMBER: _ClassVar[int]
    PRICE_TYPE_FIELD_NUMBER: _ClassVar[int]
    instrument_id: str
    quantity: int
    price: _common_pb2.Quotation
    direction: OrderDirection
    account_id: str
    order_type: OrderType
    order_id: str
    time_in_force: TimeInForceType
    price_type: _common_pb2.PriceType
    def __init__(self, instrument_id: _Optional[str] = ..., quantity: _Optional[int] = ..., price: _Optional[_Union[_common_pb2.Quotation, _Mapping]] = ..., direction: _Optional[_Union[OrderDirection, str]] = ..., account_id: _Optional[str] = ..., order_type: _Optional[_Union[OrderType, str]] = ..., order_id: _Optional[str] = ..., time_in_force: _Optional[_Union[TimeInForceType, str]] = ..., price_type: _Optional[_Union[_common_pb2.PriceType, str]] = ...) -> None: ...

class PostOrderAsyncResponse(_message.Message):
    __slots__ = ("order_request_id", "execution_report_status", "trade_intent_id")
    ORDER_REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_REPORT_STATUS_FIELD_NUMBER: _ClassVar[int]
    TRADE_INTENT_ID_FIELD_NUMBER: _ClassVar[int]
    order_request_id: str
    execution_report_status: OrderExecutionReportStatus
    trade_intent_id: str
    def __init__(self, order_request_id: _Optional[str] = ..., execution_report_status: _Optional[_Union[OrderExecutionReportStatus, str]] = ..., trade_intent_id: _Optional[str] = ...) -> None: ...

class CancelOrderRequest(_message.Message):
    __slots__ = ("account_id", "order_id", "order_id_type")
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    ORDER_ID_FIELD_NUMBER: _ClassVar[int]
    ORDER_ID_TYPE_FIELD_NUMBER: _ClassVar[int]
    account_id: str
    order_id: str
    order_id_type: OrderIdType
    def __init__(self, account_id: _Optional[str] = ..., order_id: _Optional[str] = ..., order_id_type: _Optional[_Union[OrderIdType, str]] = ...) -> None: ...

class CancelOrderResponse(_message.Message):
    __slots__ = ("time", "response_metadata")
    TIME_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_METADATA_FIELD_NUMBER: _ClassVar[int]
    time: _timestamp_pb2.Timestamp
    response_metadata: _common_pb2.ResponseMetadata
    def __init__(self, time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., response_metadata: _Optional[_Union[_common_pb2.ResponseMetadata, _Mapping]] = ...) -> None: ...

class GetOrderStateRequest(_message.Message):
    __slots__ = ("account_id", "order_id", "price_type", "order_id_type")
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    ORDER_ID_FIELD_NUMBER: _ClassVar[int]
    PRICE_TYPE_FIELD_NUMBER: _ClassVar[int]
    ORDER_ID_TYPE_FIELD_NUMBER: _ClassVar[int]
    account_id: str
    order_id: str
    price_type: _common_pb2.PriceType
    order_id_type: OrderIdType
    def __init__(self, account_id: _Optional[str] = ..., order_id: _Optional[str] = ..., price_type: _Optional[_Union[_common_pb2.PriceType, str]] = ..., order_id_type: _Optional[_Union[OrderIdType, str]] = ...) -> None: ...

class GetOrdersRequest(_message.Message):
    __slots__ = ("account_id",)
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    account_id: str
    def __init__(self, account_id: _Optional[str] = ...) -> None: ...

class GetOrdersResponse(_message.Message):
    __slots__ = ("orders",)
    ORDERS_FIELD_NUMBER: _ClassVar[int]
    orders: _containers.RepeatedCompositeFieldContainer[OrderState]
    def __init__(self, orders: _Optional[_Iterable[_Union[OrderState, _Mapping]]] = ...) -> None: ...

class OrderState(_message.Message):
    __slots__ = ("order_id", "execution_report_status", "lots_requested", "lots_executed", "initial_order_price", "executed_order_price", "total_order_amount", "average_position_price", "initial_commission", "executed_commission", "figi", "direction", "initial_security_price", "stages", "service_commission", "currency", "order_type", "order_date", "instrument_uid", "order_request_id")
    ORDER_ID_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_REPORT_STATUS_FIELD_NUMBER: _ClassVar[int]
    LOTS_REQUESTED_FIELD_NUMBER: _ClassVar[int]
    LOTS_EXECUTED_FIELD_NUMBER: _ClassVar[int]
    INITIAL_ORDER_PRICE_FIELD_NUMBER: _ClassVar[int]
    EXECUTED_ORDER_PRICE_FIELD_NUMBER: _ClassVar[int]
    TOTAL_ORDER_AMOUNT_FIELD_NUMBER: _ClassVar[int]
    AVERAGE_POSITION_PRICE_FIELD_NUMBER: _ClassVar[int]
    INITIAL_COMMISSION_FIELD_NUMBER: _ClassVar[int]
    EXECUTED_COMMISSION_FIELD_NUMBER: _ClassVar[int]
    FIGI_FIELD_NUMBER: _ClassVar[int]
    DIRECTION_FIELD_NUMBER: _ClassVar[int]
    INITIAL_SECURITY_PRICE_FIELD_NUMBER: _ClassVar[int]
    STAGES_FIELD_NUMBER: _ClassVar[int]
    SERVICE_COMMISSION_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_FIELD_NUMBER: _ClassVar[int]
    ORDER_TYPE_FIELD_NUMBER: _ClassVar[int]
    ORDER_DATE_FIELD_NUMBER: _ClassVar[int]
    INSTRUMENT_UID_FIELD_NUMBER: _ClassVar[int]
    ORDER_REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    order_id: str
    execution_report_status: OrderExecutionReportStatus
    lots_requested: int
    lots_executed: int
    initial_order_price: _common_pb2.MoneyValue
    executed_order_price: _common_pb2.MoneyValue
    total_order_amount: _common_pb2.MoneyValue
    average_position_price: _common_pb2.MoneyValue
    initial_commission: _common_pb2.MoneyValue
    executed_commission: _common_pb2.MoneyValue
    figi: str
    direction: OrderDirection
    initial_security_price: _common_pb2.MoneyValue
    stages: _containers.RepeatedCompositeFieldContainer[OrderStage]
    service_commission: _common_pb2.MoneyValue
    currency: str
    order_type: OrderType
    order_date: _timestamp_pb2.Timestamp
    instrument_uid: str
    order_request_id: str
    def __init__(self, order_id: _Optional[str] = ..., execution_report_status: _Optional[_Union[OrderExecutionReportStatus, str]] = ..., lots_requested: _Optional[int] = ..., lots_executed: _Optional[int] = ..., initial_order_price: _Optional[_Union[_common_pb2.MoneyValue, _Mapping]] = ..., executed_order_price: _Optional[_Union[_common_pb2.MoneyValue, _Mapping]] = ..., total_order_amount: _Optional[_Union[_common_pb2.MoneyValue, _Mapping]] = ..., average_position_price: _Optional[_Union[_common_pb2.MoneyValue, _Mapping]] = ..., initial_commission: _Optional[_Union[_common_pb2.MoneyValue, _Mapping]] = ..., executed_commission: _Optional[_Union[_common_pb2.MoneyValue, _Mapping]] = ..., figi: _Optional[str] = ..., direction: _Optional[_Union[OrderDirection, str]] = ..., initial_security_price: _Optional[_Union[_common_pb2.MoneyValue, _Mapping]] = ..., stages: _Optional[_Iterable[_Union[OrderStage, _Mapping]]] = ..., service_commission: _Optional[_Union[_common_pb2.MoneyValue, _Mapping]] = ..., currency: _Optional[str] = ..., order_type: _Optional[_Union[OrderType, str]] = ..., order_date: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., instrument_uid: _Optional[str] = ..., order_request_id: _Optional[str] = ...) -> None: ...

class OrderStage(_message.Message):
    __slots__ = ("price", "quantity", "trade_id", "execution_time")
    PRICE_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    TRADE_ID_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_TIME_FIELD_NUMBER: _ClassVar[int]
    price: _common_pb2.MoneyValue
    quantity: int
    trade_id: str
    execution_time: _timestamp_pb2.Timestamp
    def __init__(self, price: _Optional[_Union[_common_pb2.MoneyValue, _Mapping]] = ..., quantity: _Optional[int] = ..., trade_id: _Optional[str] = ..., execution_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class ReplaceOrderRequest(_message.Message):
    __slots__ = ("account_id", "order_id", "idempotency_key", "quantity", "price", "price_type")
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    ORDER_ID_FIELD_NUMBER: _ClassVar[int]
    IDEMPOTENCY_KEY_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    PRICE_TYPE_FIELD_NUMBER: _ClassVar[int]
    account_id: str
    order_id: str
    idempotency_key: str
    quantity: int
    price: _common_pb2.Quotation
    price_type: _common_pb2.PriceType
    def __init__(self, account_id: _Optional[str] = ..., order_id: _Optional[str] = ..., idempotency_key: _Optional[str] = ..., quantity: _Optional[int] = ..., price: _Optional[_Union[_common_pb2.Quotation, _Mapping]] = ..., price_type: _Optional[_Union[_common_pb2.PriceType, str]] = ...) -> None: ...

class GetMaxLotsRequest(_message.Message):
    __slots__ = ("account_id", "instrument_id", "price")
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    INSTRUMENT_ID_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    account_id: str
    instrument_id: str
    price: _common_pb2.Quotation
    def __init__(self, account_id: _Optional[str] = ..., instrument_id: _Optional[str] = ..., price: _Optional[_Union[_common_pb2.Quotation, _Mapping]] = ...) -> None: ...

class GetMaxLotsResponse(_message.Message):
    __slots__ = ("currency", "buy_limits", "buy_margin_limits", "sell_limits", "sell_margin_limits")
    class BuyLimitsView(_message.Message):
        __slots__ = ("buy_money_amount", "buy_max_lots", "buy_max_market_lots")
        BUY_MONEY_AMOUNT_FIELD_NUMBER: _ClassVar[int]
        BUY_MAX_LOTS_FIELD_NUMBER: _ClassVar[int]
        BUY_MAX_MARKET_LOTS_FIELD_NUMBER: _ClassVar[int]
        buy_money_amount: _common_pb2.Quotation
        buy_max_lots: int
        buy_max_market_lots: int
        def __init__(self, buy_money_amount: _Optional[_Union[_common_pb2.Quotation, _Mapping]] = ..., buy_max_lots: _Optional[int] = ..., buy_max_market_lots: _Optional[int] = ...) -> None: ...
    class SellLimitsView(_message.Message):
        __slots__ = ("sell_max_lots",)
        SELL_MAX_LOTS_FIELD_NUMBER: _ClassVar[int]
        sell_max_lots: int
        def __init__(self, sell_max_lots: _Optional[int] = ...) -> None: ...
    CURRENCY_FIELD_NUMBER: _ClassVar[int]
    BUY_LIMITS_FIELD_NUMBER: _ClassVar[int]
    BUY_MARGIN_LIMITS_FIELD_NUMBER: _ClassVar[int]
    SELL_LIMITS_FIELD_NUMBER: _ClassVar[int]
    SELL_MARGIN_LIMITS_FIELD_NUMBER: _ClassVar[int]
    currency: str
    buy_limits: GetMaxLotsResponse.BuyLimitsView
    buy_margin_limits: GetMaxLotsResponse.BuyLimitsView
    sell_limits: GetMaxLotsResponse.SellLimitsView
    sell_margin_limits: GetMaxLotsResponse.SellLimitsView
    def __init__(self, currency: _Optional[str] = ..., buy_limits: _Optional[_Union[GetMaxLotsResponse.BuyLimitsView, _Mapping]] = ..., buy_margin_limits: _Optional[_Union[GetMaxLotsResponse.BuyLimitsView, _Mapping]] = ..., sell_limits: _Optional[_Union[GetMaxLotsResponse.SellLimitsView, _Mapping]] = ..., sell_margin_limits: _Optional[_Union[GetMaxLotsResponse.SellLimitsView, _Mapping]] = ...) -> None: ...

class GetOrderPriceRequest(_message.Message):
    __slots__ = ("account_id", "instrument_id", "price", "direction", "quantity")
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    INSTRUMENT_ID_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    DIRECTION_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    account_id: str
    instrument_id: str
    price: _common_pb2.Quotation
    direction: OrderDirection
    quantity: int
    def __init__(self, account_id: _Optional[str] = ..., instrument_id: _Optional[str] = ..., price: _Optional[_Union[_common_pb2.Quotation, _Mapping]] = ..., direction: _Optional[_Union[OrderDirection, str]] = ..., quantity: _Optional[int] = ...) -> None: ...

class GetOrderPriceResponse(_message.Message):
    __slots__ = ("total_order_amount", "initial_order_amount", "lots_requested", "executed_commission", "executed_commission_rub", "service_commission", "deal_commission", "extra_bond", "extra_future")
    class ExtraBond(_message.Message):
        __slots__ = ("aci_value", "nominal_conversion_rate")
        ACI_VALUE_FIELD_NUMBER: _ClassVar[int]
        NOMINAL_CONVERSION_RATE_FIELD_NUMBER: _ClassVar[int]
        aci_value: _common_pb2.MoneyValue
        nominal_conversion_rate: _common_pb2.Quotation
        def __init__(self, aci_value: _Optional[_Union[_common_pb2.MoneyValue, _Mapping]] = ..., nominal_conversion_rate: _Optional[_Union[_common_pb2.Quotation, _Mapping]] = ...) -> None: ...
    class ExtraFuture(_message.Message):
        __slots__ = ("initial_margin",)
        INITIAL_MARGIN_FIELD_NUMBER: _ClassVar[int]
        initial_margin: _common_pb2.MoneyValue
        def __init__(self, initial_margin: _Optional[_Union[_common_pb2.MoneyValue, _Mapping]] = ...) -> None: ...
    TOTAL_ORDER_AMOUNT_FIELD_NUMBER: _ClassVar[int]
    INITIAL_ORDER_AMOUNT_FIELD_NUMBER: _ClassVar[int]
    LOTS_REQUESTED_FIELD_NUMBER: _ClassVar[int]
    EXECUTED_COMMISSION_FIELD_NUMBER: _ClassVar[int]
    EXECUTED_COMMISSION_RUB_FIELD_NUMBER: _ClassVar[int]
    SERVICE_COMMISSION_FIELD_NUMBER: _ClassVar[int]
    DEAL_COMMISSION_FIELD_NUMBER: _ClassVar[int]
    EXTRA_BOND_FIELD_NUMBER: _ClassVar[int]
    EXTRA_FUTURE_FIELD_NUMBER: _ClassVar[int]
    total_order_amount: _common_pb2.MoneyValue
    initial_order_amount: _common_pb2.MoneyValue
    lots_requested: int
    executed_commission: _common_pb2.MoneyValue
    executed_commission_rub: _common_pb2.MoneyValue
    service_commission: _common_pb2.MoneyValue
    deal_commission: _common_pb2.MoneyValue
    extra_bond: GetOrderPriceResponse.ExtraBond
    extra_future: GetOrderPriceResponse.ExtraFuture
    def __init__(self, total_order_amount: _Optional[_Union[_common_pb2.MoneyValue, _Mapping]] = ..., initial_order_amount: _Optional[_Union[_common_pb2.MoneyValue, _Mapping]] = ..., lots_requested: _Optional[int] = ..., executed_commission: _Optional[_Union[_common_pb2.MoneyValue, _Mapping]] = ..., executed_commission_rub: _Optional[_Union[_common_pb2.MoneyValue, _Mapping]] = ..., service_commission: _Optional[_Union[_common_pb2.MoneyValue, _Mapping]] = ..., deal_commission: _Optional[_Union[_common_pb2.MoneyValue, _Mapping]] = ..., extra_bond: _Optional[_Union[GetOrderPriceResponse.ExtraBond, _Mapping]] = ..., extra_future: _Optional[_Union[GetOrderPriceResponse.ExtraFuture, _Mapping]] = ...) -> None: ...

class OrderStateStreamRequest(_message.Message):
    __slots__ = ("accounts", "ping_delay_millis")
    ACCOUNTS_FIELD_NUMBER: _ClassVar[int]
    PING_DELAY_MILLIS_FIELD_NUMBER: _ClassVar[int]
    accounts: _containers.RepeatedScalarFieldContainer[str]
    ping_delay_millis: int
    def __init__(self, accounts: _Optional[_Iterable[str]] = ..., ping_delay_millis: _Optional[int] = ...) -> None: ...

class SubscriptionResponse(_message.Message):
    __slots__ = ("tracking_id", "status", "stream_id", "accounts", "error")
    TRACKING_ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    STREAM_ID_FIELD_NUMBER: _ClassVar[int]
    ACCOUNTS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    tracking_id: str
    status: _common_pb2.ResultSubscriptionStatus
    stream_id: str
    accounts: _containers.RepeatedScalarFieldContainer[str]
    error: _common_pb2.ErrorDetail
    def __init__(self, tracking_id: _Optional[str] = ..., status: _Optional[_Union[_common_pb2.ResultSubscriptionStatus, str]] = ..., stream_id: _Optional[str] = ..., accounts: _Optional[_Iterable[str]] = ..., error: _Optional[_Union[_common_pb2.ErrorDetail, _Mapping]] = ...) -> None: ...

class OrderStateStreamResponse(_message.Message):
    __slots__ = ("order_state", "ping", "subscription")
    class MarkerType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        MARKER_UNKNOWN: _ClassVar[OrderStateStreamResponse.MarkerType]
        MARKER_BROKER: _ClassVar[OrderStateStreamResponse.MarkerType]
        MARKER_CHAT: _ClassVar[OrderStateStreamResponse.MarkerType]
        MARKER_PAPER: _ClassVar[OrderStateStreamResponse.MarkerType]
        MARKER_MARGIN: _ClassVar[OrderStateStreamResponse.MarkerType]
        MARKER_TKBNM: _ClassVar[OrderStateStreamResponse.MarkerType]
        MARKER_SHORT: _ClassVar[OrderStateStreamResponse.MarkerType]
        MARKER_SPECMM: _ClassVar[OrderStateStreamResponse.MarkerType]
        MARKER_PO: _ClassVar[OrderStateStreamResponse.MarkerType]
    MARKER_UNKNOWN: OrderStateStreamResponse.MarkerType
    MARKER_BROKER: OrderStateStreamResponse.MarkerType
    MARKER_CHAT: OrderStateStreamResponse.MarkerType
    MARKER_PAPER: OrderStateStreamResponse.MarkerType
    MARKER_MARGIN: OrderStateStreamResponse.MarkerType
    MARKER_TKBNM: OrderStateStreamResponse.MarkerType
    MARKER_SHORT: OrderStateStreamResponse.MarkerType
    MARKER_SPECMM: OrderStateStreamResponse.MarkerType
    MARKER_PO: OrderStateStreamResponse.MarkerType
    class StatusCauseInfo(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CAUSE_UNSPECIFIED: _ClassVar[OrderStateStreamResponse.StatusCauseInfo]
        CAUSE_CANCELLED_BY_CLIENT: _ClassVar[OrderStateStreamResponse.StatusCauseInfo]
        CAUSE_CANCELLED_BY_EXCHANGE: _ClassVar[OrderStateStreamResponse.StatusCauseInfo]
        CAUSE_CANCELLED_NOT_ENOUGH_POSITION: _ClassVar[OrderStateStreamResponse.StatusCauseInfo]
        CAUSE_CANCELLED_BY_CLIENT_BLOCK: _ClassVar[OrderStateStreamResponse.StatusCauseInfo]
        CAUSE_REJECTED_BY_BROKER: _ClassVar[OrderStateStreamResponse.StatusCauseInfo]
        CAUSE_REJECTED_BY_EXCHANGE: _ClassVar[OrderStateStreamResponse.StatusCauseInfo]
        CAUSE_CANCELLED_BY_BROKER: _ClassVar[OrderStateStreamResponse.StatusCauseInfo]
    CAUSE_UNSPECIFIED: OrderStateStreamResponse.StatusCauseInfo
    CAUSE_CANCELLED_BY_CLIENT: OrderStateStreamResponse.StatusCauseInfo
    CAUSE_CANCELLED_BY_EXCHANGE: OrderStateStreamResponse.StatusCauseInfo
    CAUSE_CANCELLED_NOT_ENOUGH_POSITION: OrderStateStreamResponse.StatusCauseInfo
    CAUSE_CANCELLED_BY_CLIENT_BLOCK: OrderStateStreamResponse.StatusCauseInfo
    CAUSE_REJECTED_BY_BROKER: OrderStateStreamResponse.StatusCauseInfo
    CAUSE_REJECTED_BY_EXCHANGE: OrderStateStreamResponse.StatusCauseInfo
    CAUSE_CANCELLED_BY_BROKER: OrderStateStreamResponse.StatusCauseInfo
    class OrderState(_message.Message):
        __slots__ = ("order_id", "order_request_id", "client_code", "created_at", "execution_report_status", "status_info", "ticker", "class_code", "lot_size", "direction", "time_in_force", "order_type", "account_id", "initial_order_price", "order_price", "amount", "executed_order_price", "currency", "lots_requested", "lots_executed", "lots_left", "lots_cancelled", "marker", "trades", "completion_time", "exchange", "instrument_uid")
        ORDER_ID_FIELD_NUMBER: _ClassVar[int]
        ORDER_REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
        CLIENT_CODE_FIELD_NUMBER: _ClassVar[int]
        CREATED_AT_FIELD_NUMBER: _ClassVar[int]
        EXECUTION_REPORT_STATUS_FIELD_NUMBER: _ClassVar[int]
        STATUS_INFO_FIELD_NUMBER: _ClassVar[int]
        TICKER_FIELD_NUMBER: _ClassVar[int]
        CLASS_CODE_FIELD_NUMBER: _ClassVar[int]
        LOT_SIZE_FIELD_NUMBER: _ClassVar[int]
        DIRECTION_FIELD_NUMBER: _ClassVar[int]
        TIME_IN_FORCE_FIELD_NUMBER: _ClassVar[int]
        ORDER_TYPE_FIELD_NUMBER: _ClassVar[int]
        ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
        INITIAL_ORDER_PRICE_FIELD_NUMBER: _ClassVar[int]
        ORDER_PRICE_FIELD_NUMBER: _ClassVar[int]
        AMOUNT_FIELD_NUMBER: _ClassVar[int]
        EXECUTED_ORDER_PRICE_FIELD_NUMBER: _ClassVar[int]
        CURRENCY_FIELD_NUMBER: _ClassVar[int]
        LOTS_REQUESTED_FIELD_NUMBER: _ClassVar[int]
        LOTS_EXECUTED_FIELD_NUMBER: _ClassVar[int]
        LOTS_LEFT_FIELD_NUMBER: _ClassVar[int]
        LOTS_CANCELLED_FIELD_NUMBER: _ClassVar[int]
        MARKER_FIELD_NUMBER: _ClassVar[int]
        TRADES_FIELD_NUMBER: _ClassVar[int]
        COMPLETION_TIME_FIELD_NUMBER: _ClassVar[int]
        EXCHANGE_FIELD_NUMBER: _ClassVar[int]
        INSTRUMENT_UID_FIELD_NUMBER: _ClassVar[int]
        order_id: str
        order_request_id: str
        client_code: str
        created_at: _timestamp_pb2.Timestamp
        execution_report_status: OrderExecutionReportStatus
        status_info: OrderStateStreamResponse.StatusCauseInfo
        ticker: str
        class_code: str
        lot_size: int
        direction: OrderDirection
        time_in_force: TimeInForceType
        order_type: OrderType
        account_id: str
        initial_order_price: _common_pb2.MoneyValue
        order_price: _common_pb2.MoneyValue
        amount: _common_pb2.MoneyValue
        executed_order_price: _common_pb2.MoneyValue
        currency: str
        lots_requested: int
        lots_executed: int
        lots_left: int
        lots_cancelled: int
        marker: OrderStateStreamResponse.MarkerType
        trades: _containers.RepeatedCompositeFieldContainer[OrderTrade]
        completion_time: _timestamp_pb2.Timestamp
        exchange: str
        instrument_uid: str
        def __init__(self, order_id: _Optional[str] = ..., order_request_id: _Optional[str] = ..., client_code: _Optional[str] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., execution_report_status: _Optional[_Union[OrderExecutionReportStatus, str]] = ..., status_info: _Optional[_Union[OrderStateStreamResponse.StatusCauseInfo, str]] = ..., ticker: _Optional[str] = ..., class_code: _Optional[str] = ..., lot_size: _Optional[int] = ..., direction: _Optional[_Union[OrderDirection, str]] = ..., time_in_force: _Optional[_Union[TimeInForceType, str]] = ..., order_type: _Optional[_Union[OrderType, str]] = ..., account_id: _Optional[str] = ..., initial_order_price: _Optional[_Union[_common_pb2.MoneyValue, _Mapping]] = ..., order_price: _Optional[_Union[_common_pb2.MoneyValue, _Mapping]] = ..., amount: _Optional[_Union[_common_pb2.MoneyValue, _Mapping]] = ..., executed_order_price: _Optional[_Union[_common_pb2.MoneyValue, _Mapping]] = ..., currency: _Optional[str] = ..., lots_requested: _Optional[int] = ..., lots_executed: _Optional[int] = ..., lots_left: _Optional[int] = ..., lots_cancelled: _Optional[int] = ..., marker: _Optional[_Union[OrderStateStreamResponse.MarkerType, str]] = ..., trades: _Optional[_Iterable[_Union[OrderTrade, _Mapping]]] = ..., completion_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., exchange: _Optional[str] = ..., instrument_uid: _Optional[str] = ...) -> None: ...
    ORDER_STATE_FIELD_NUMBER: _ClassVar[int]
    PING_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIPTION_FIELD_NUMBER: _ClassVar[int]
    order_state: OrderStateStreamResponse.OrderState
    ping: _common_pb2.Ping
    subscription: SubscriptionResponse
    def __init__(self, order_state: _Optional[_Union[OrderStateStreamResponse.OrderState, _Mapping]] = ..., ping: _Optional[_Union[_common_pb2.Ping, _Mapping]] = ..., subscription: _Optional[_Union[SubscriptionResponse, _Mapping]] = ...) -> None: ...
