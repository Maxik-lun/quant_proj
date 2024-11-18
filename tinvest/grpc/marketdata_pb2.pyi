from google.protobuf import timestamp_pb2 as _timestamp_pb2
from tinvest.grpc import common_pb2 as _common_pb2
from tinvest.grpc.google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SubscriptionAction(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SUBSCRIPTION_ACTION_UNSPECIFIED: _ClassVar[SubscriptionAction]
    SUBSCRIPTION_ACTION_SUBSCRIBE: _ClassVar[SubscriptionAction]
    SUBSCRIPTION_ACTION_UNSUBSCRIBE: _ClassVar[SubscriptionAction]

class SubscriptionInterval(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SUBSCRIPTION_INTERVAL_UNSPECIFIED: _ClassVar[SubscriptionInterval]
    SUBSCRIPTION_INTERVAL_ONE_MINUTE: _ClassVar[SubscriptionInterval]
    SUBSCRIPTION_INTERVAL_FIVE_MINUTES: _ClassVar[SubscriptionInterval]
    SUBSCRIPTION_INTERVAL_FIFTEEN_MINUTES: _ClassVar[SubscriptionInterval]
    SUBSCRIPTION_INTERVAL_ONE_HOUR: _ClassVar[SubscriptionInterval]
    SUBSCRIPTION_INTERVAL_ONE_DAY: _ClassVar[SubscriptionInterval]
    SUBSCRIPTION_INTERVAL_2_MIN: _ClassVar[SubscriptionInterval]
    SUBSCRIPTION_INTERVAL_3_MIN: _ClassVar[SubscriptionInterval]
    SUBSCRIPTION_INTERVAL_10_MIN: _ClassVar[SubscriptionInterval]
    SUBSCRIPTION_INTERVAL_30_MIN: _ClassVar[SubscriptionInterval]
    SUBSCRIPTION_INTERVAL_2_HOUR: _ClassVar[SubscriptionInterval]
    SUBSCRIPTION_INTERVAL_4_HOUR: _ClassVar[SubscriptionInterval]
    SUBSCRIPTION_INTERVAL_WEEK: _ClassVar[SubscriptionInterval]
    SUBSCRIPTION_INTERVAL_MONTH: _ClassVar[SubscriptionInterval]

class SubscriptionStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SUBSCRIPTION_STATUS_UNSPECIFIED: _ClassVar[SubscriptionStatus]
    SUBSCRIPTION_STATUS_SUCCESS: _ClassVar[SubscriptionStatus]
    SUBSCRIPTION_STATUS_INSTRUMENT_NOT_FOUND: _ClassVar[SubscriptionStatus]
    SUBSCRIPTION_STATUS_SUBSCRIPTION_ACTION_IS_INVALID: _ClassVar[SubscriptionStatus]
    SUBSCRIPTION_STATUS_DEPTH_IS_INVALID: _ClassVar[SubscriptionStatus]
    SUBSCRIPTION_STATUS_INTERVAL_IS_INVALID: _ClassVar[SubscriptionStatus]
    SUBSCRIPTION_STATUS_LIMIT_IS_EXCEEDED: _ClassVar[SubscriptionStatus]
    SUBSCRIPTION_STATUS_INTERNAL_ERROR: _ClassVar[SubscriptionStatus]
    SUBSCRIPTION_STATUS_TOO_MANY_REQUESTS: _ClassVar[SubscriptionStatus]
    SUBSCRIPTION_STATUS_SUBSCRIPTION_NOT_FOUND: _ClassVar[SubscriptionStatus]

class TradeSourceType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TRADE_SOURCE_UNSPECIFIED: _ClassVar[TradeSourceType]
    TRADE_SOURCE_EXCHANGE: _ClassVar[TradeSourceType]
    TRADE_SOURCE_DEALER: _ClassVar[TradeSourceType]
    TRADE_SOURCE_ALL: _ClassVar[TradeSourceType]

class TradeDirection(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TRADE_DIRECTION_UNSPECIFIED: _ClassVar[TradeDirection]
    TRADE_DIRECTION_BUY: _ClassVar[TradeDirection]
    TRADE_DIRECTION_SELL: _ClassVar[TradeDirection]

class CandleInterval(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CANDLE_INTERVAL_UNSPECIFIED: _ClassVar[CandleInterval]
    CANDLE_INTERVAL_1_MIN: _ClassVar[CandleInterval]
    CANDLE_INTERVAL_5_MIN: _ClassVar[CandleInterval]
    CANDLE_INTERVAL_15_MIN: _ClassVar[CandleInterval]
    CANDLE_INTERVAL_HOUR: _ClassVar[CandleInterval]
    CANDLE_INTERVAL_DAY: _ClassVar[CandleInterval]
    CANDLE_INTERVAL_2_MIN: _ClassVar[CandleInterval]
    CANDLE_INTERVAL_3_MIN: _ClassVar[CandleInterval]
    CANDLE_INTERVAL_10_MIN: _ClassVar[CandleInterval]
    CANDLE_INTERVAL_30_MIN: _ClassVar[CandleInterval]
    CANDLE_INTERVAL_2_HOUR: _ClassVar[CandleInterval]
    CANDLE_INTERVAL_4_HOUR: _ClassVar[CandleInterval]
    CANDLE_INTERVAL_WEEK: _ClassVar[CandleInterval]
    CANDLE_INTERVAL_MONTH: _ClassVar[CandleInterval]

class CandleSource(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CANDLE_SOURCE_UNSPECIFIED: _ClassVar[CandleSource]
    CANDLE_SOURCE_EXCHANGE: _ClassVar[CandleSource]
    CANDLE_SOURCE_DEALER_WEEKEND: _ClassVar[CandleSource]

class OrderBookType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ORDERBOOK_TYPE_UNSPECIFIED: _ClassVar[OrderBookType]
    ORDERBOOK_TYPE_EXCHANGE: _ClassVar[OrderBookType]
    ORDERBOOK_TYPE_DEALER: _ClassVar[OrderBookType]

class LastPriceType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    LAST_PRICE_UNSPECIFIED: _ClassVar[LastPriceType]
    LAST_PRICE_EXCHANGE: _ClassVar[LastPriceType]
    LAST_PRICE_DEALER: _ClassVar[LastPriceType]
SUBSCRIPTION_ACTION_UNSPECIFIED: SubscriptionAction
SUBSCRIPTION_ACTION_SUBSCRIBE: SubscriptionAction
SUBSCRIPTION_ACTION_UNSUBSCRIBE: SubscriptionAction
SUBSCRIPTION_INTERVAL_UNSPECIFIED: SubscriptionInterval
SUBSCRIPTION_INTERVAL_ONE_MINUTE: SubscriptionInterval
SUBSCRIPTION_INTERVAL_FIVE_MINUTES: SubscriptionInterval
SUBSCRIPTION_INTERVAL_FIFTEEN_MINUTES: SubscriptionInterval
SUBSCRIPTION_INTERVAL_ONE_HOUR: SubscriptionInterval
SUBSCRIPTION_INTERVAL_ONE_DAY: SubscriptionInterval
SUBSCRIPTION_INTERVAL_2_MIN: SubscriptionInterval
SUBSCRIPTION_INTERVAL_3_MIN: SubscriptionInterval
SUBSCRIPTION_INTERVAL_10_MIN: SubscriptionInterval
SUBSCRIPTION_INTERVAL_30_MIN: SubscriptionInterval
SUBSCRIPTION_INTERVAL_2_HOUR: SubscriptionInterval
SUBSCRIPTION_INTERVAL_4_HOUR: SubscriptionInterval
SUBSCRIPTION_INTERVAL_WEEK: SubscriptionInterval
SUBSCRIPTION_INTERVAL_MONTH: SubscriptionInterval
SUBSCRIPTION_STATUS_UNSPECIFIED: SubscriptionStatus
SUBSCRIPTION_STATUS_SUCCESS: SubscriptionStatus
SUBSCRIPTION_STATUS_INSTRUMENT_NOT_FOUND: SubscriptionStatus
SUBSCRIPTION_STATUS_SUBSCRIPTION_ACTION_IS_INVALID: SubscriptionStatus
SUBSCRIPTION_STATUS_DEPTH_IS_INVALID: SubscriptionStatus
SUBSCRIPTION_STATUS_INTERVAL_IS_INVALID: SubscriptionStatus
SUBSCRIPTION_STATUS_LIMIT_IS_EXCEEDED: SubscriptionStatus
SUBSCRIPTION_STATUS_INTERNAL_ERROR: SubscriptionStatus
SUBSCRIPTION_STATUS_TOO_MANY_REQUESTS: SubscriptionStatus
SUBSCRIPTION_STATUS_SUBSCRIPTION_NOT_FOUND: SubscriptionStatus
TRADE_SOURCE_UNSPECIFIED: TradeSourceType
TRADE_SOURCE_EXCHANGE: TradeSourceType
TRADE_SOURCE_DEALER: TradeSourceType
TRADE_SOURCE_ALL: TradeSourceType
TRADE_DIRECTION_UNSPECIFIED: TradeDirection
TRADE_DIRECTION_BUY: TradeDirection
TRADE_DIRECTION_SELL: TradeDirection
CANDLE_INTERVAL_UNSPECIFIED: CandleInterval
CANDLE_INTERVAL_1_MIN: CandleInterval
CANDLE_INTERVAL_5_MIN: CandleInterval
CANDLE_INTERVAL_15_MIN: CandleInterval
CANDLE_INTERVAL_HOUR: CandleInterval
CANDLE_INTERVAL_DAY: CandleInterval
CANDLE_INTERVAL_2_MIN: CandleInterval
CANDLE_INTERVAL_3_MIN: CandleInterval
CANDLE_INTERVAL_10_MIN: CandleInterval
CANDLE_INTERVAL_30_MIN: CandleInterval
CANDLE_INTERVAL_2_HOUR: CandleInterval
CANDLE_INTERVAL_4_HOUR: CandleInterval
CANDLE_INTERVAL_WEEK: CandleInterval
CANDLE_INTERVAL_MONTH: CandleInterval
CANDLE_SOURCE_UNSPECIFIED: CandleSource
CANDLE_SOURCE_EXCHANGE: CandleSource
CANDLE_SOURCE_DEALER_WEEKEND: CandleSource
ORDERBOOK_TYPE_UNSPECIFIED: OrderBookType
ORDERBOOK_TYPE_EXCHANGE: OrderBookType
ORDERBOOK_TYPE_DEALER: OrderBookType
LAST_PRICE_UNSPECIFIED: LastPriceType
LAST_PRICE_EXCHANGE: LastPriceType
LAST_PRICE_DEALER: LastPriceType

class MarketDataRequest(_message.Message):
    __slots__ = ("subscribe_candles_request", "subscribe_order_book_request", "subscribe_trades_request", "subscribe_info_request", "subscribe_last_price_request", "get_my_subscriptions")
    SUBSCRIBE_CANDLES_REQUEST_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIBE_ORDER_BOOK_REQUEST_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIBE_TRADES_REQUEST_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIBE_INFO_REQUEST_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIBE_LAST_PRICE_REQUEST_FIELD_NUMBER: _ClassVar[int]
    GET_MY_SUBSCRIPTIONS_FIELD_NUMBER: _ClassVar[int]
    subscribe_candles_request: SubscribeCandlesRequest
    subscribe_order_book_request: SubscribeOrderBookRequest
    subscribe_trades_request: SubscribeTradesRequest
    subscribe_info_request: SubscribeInfoRequest
    subscribe_last_price_request: SubscribeLastPriceRequest
    get_my_subscriptions: GetMySubscriptions
    def __init__(self, subscribe_candles_request: _Optional[_Union[SubscribeCandlesRequest, _Mapping]] = ..., subscribe_order_book_request: _Optional[_Union[SubscribeOrderBookRequest, _Mapping]] = ..., subscribe_trades_request: _Optional[_Union[SubscribeTradesRequest, _Mapping]] = ..., subscribe_info_request: _Optional[_Union[SubscribeInfoRequest, _Mapping]] = ..., subscribe_last_price_request: _Optional[_Union[SubscribeLastPriceRequest, _Mapping]] = ..., get_my_subscriptions: _Optional[_Union[GetMySubscriptions, _Mapping]] = ...) -> None: ...

class MarketDataServerSideStreamRequest(_message.Message):
    __slots__ = ("subscribe_candles_request", "subscribe_order_book_request", "subscribe_trades_request", "subscribe_info_request", "subscribe_last_price_request")
    SUBSCRIBE_CANDLES_REQUEST_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIBE_ORDER_BOOK_REQUEST_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIBE_TRADES_REQUEST_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIBE_INFO_REQUEST_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIBE_LAST_PRICE_REQUEST_FIELD_NUMBER: _ClassVar[int]
    subscribe_candles_request: SubscribeCandlesRequest
    subscribe_order_book_request: SubscribeOrderBookRequest
    subscribe_trades_request: SubscribeTradesRequest
    subscribe_info_request: SubscribeInfoRequest
    subscribe_last_price_request: SubscribeLastPriceRequest
    def __init__(self, subscribe_candles_request: _Optional[_Union[SubscribeCandlesRequest, _Mapping]] = ..., subscribe_order_book_request: _Optional[_Union[SubscribeOrderBookRequest, _Mapping]] = ..., subscribe_trades_request: _Optional[_Union[SubscribeTradesRequest, _Mapping]] = ..., subscribe_info_request: _Optional[_Union[SubscribeInfoRequest, _Mapping]] = ..., subscribe_last_price_request: _Optional[_Union[SubscribeLastPriceRequest, _Mapping]] = ...) -> None: ...

class MarketDataResponse(_message.Message):
    __slots__ = ("subscribe_candles_response", "subscribe_order_book_response", "subscribe_trades_response", "subscribe_info_response", "candle", "trade", "orderbook", "trading_status", "ping", "subscribe_last_price_response", "last_price")
    SUBSCRIBE_CANDLES_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIBE_ORDER_BOOK_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIBE_TRADES_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIBE_INFO_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    CANDLE_FIELD_NUMBER: _ClassVar[int]
    TRADE_FIELD_NUMBER: _ClassVar[int]
    ORDERBOOK_FIELD_NUMBER: _ClassVar[int]
    TRADING_STATUS_FIELD_NUMBER: _ClassVar[int]
    PING_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIBE_LAST_PRICE_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    LAST_PRICE_FIELD_NUMBER: _ClassVar[int]
    subscribe_candles_response: SubscribeCandlesResponse
    subscribe_order_book_response: SubscribeOrderBookResponse
    subscribe_trades_response: SubscribeTradesResponse
    subscribe_info_response: SubscribeInfoResponse
    candle: Candle
    trade: Trade
    orderbook: OrderBook
    trading_status: TradingStatus
    ping: _common_pb2.Ping
    subscribe_last_price_response: SubscribeLastPriceResponse
    last_price: LastPrice
    def __init__(self, subscribe_candles_response: _Optional[_Union[SubscribeCandlesResponse, _Mapping]] = ..., subscribe_order_book_response: _Optional[_Union[SubscribeOrderBookResponse, _Mapping]] = ..., subscribe_trades_response: _Optional[_Union[SubscribeTradesResponse, _Mapping]] = ..., subscribe_info_response: _Optional[_Union[SubscribeInfoResponse, _Mapping]] = ..., candle: _Optional[_Union[Candle, _Mapping]] = ..., trade: _Optional[_Union[Trade, _Mapping]] = ..., orderbook: _Optional[_Union[OrderBook, _Mapping]] = ..., trading_status: _Optional[_Union[TradingStatus, _Mapping]] = ..., ping: _Optional[_Union[_common_pb2.Ping, _Mapping]] = ..., subscribe_last_price_response: _Optional[_Union[SubscribeLastPriceResponse, _Mapping]] = ..., last_price: _Optional[_Union[LastPrice, _Mapping]] = ...) -> None: ...

class SubscribeCandlesRequest(_message.Message):
    __slots__ = ("subscription_action", "instruments", "waiting_close")
    SUBSCRIPTION_ACTION_FIELD_NUMBER: _ClassVar[int]
    INSTRUMENTS_FIELD_NUMBER: _ClassVar[int]
    WAITING_CLOSE_FIELD_NUMBER: _ClassVar[int]
    subscription_action: SubscriptionAction
    instruments: _containers.RepeatedCompositeFieldContainer[CandleInstrument]
    waiting_close: bool
    def __init__(self, subscription_action: _Optional[_Union[SubscriptionAction, str]] = ..., instruments: _Optional[_Iterable[_Union[CandleInstrument, _Mapping]]] = ..., waiting_close: bool = ...) -> None: ...

class CandleInstrument(_message.Message):
    __slots__ = ("figi", "interval", "instrument_id")
    FIGI_FIELD_NUMBER: _ClassVar[int]
    INTERVAL_FIELD_NUMBER: _ClassVar[int]
    INSTRUMENT_ID_FIELD_NUMBER: _ClassVar[int]
    figi: str
    interval: SubscriptionInterval
    instrument_id: str
    def __init__(self, figi: _Optional[str] = ..., interval: _Optional[_Union[SubscriptionInterval, str]] = ..., instrument_id: _Optional[str] = ...) -> None: ...

class SubscribeCandlesResponse(_message.Message):
    __slots__ = ("tracking_id", "candles_subscriptions")
    TRACKING_ID_FIELD_NUMBER: _ClassVar[int]
    CANDLES_SUBSCRIPTIONS_FIELD_NUMBER: _ClassVar[int]
    tracking_id: str
    candles_subscriptions: _containers.RepeatedCompositeFieldContainer[CandleSubscription]
    def __init__(self, tracking_id: _Optional[str] = ..., candles_subscriptions: _Optional[_Iterable[_Union[CandleSubscription, _Mapping]]] = ...) -> None: ...

class CandleSubscription(_message.Message):
    __slots__ = ("figi", "interval", "subscription_status", "instrument_uid", "waiting_close", "stream_id", "subscription_id")
    FIGI_FIELD_NUMBER: _ClassVar[int]
    INTERVAL_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIPTION_STATUS_FIELD_NUMBER: _ClassVar[int]
    INSTRUMENT_UID_FIELD_NUMBER: _ClassVar[int]
    WAITING_CLOSE_FIELD_NUMBER: _ClassVar[int]
    STREAM_ID_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIPTION_ID_FIELD_NUMBER: _ClassVar[int]
    figi: str
    interval: SubscriptionInterval
    subscription_status: SubscriptionStatus
    instrument_uid: str
    waiting_close: bool
    stream_id: str
    subscription_id: str
    def __init__(self, figi: _Optional[str] = ..., interval: _Optional[_Union[SubscriptionInterval, str]] = ..., subscription_status: _Optional[_Union[SubscriptionStatus, str]] = ..., instrument_uid: _Optional[str] = ..., waiting_close: bool = ..., stream_id: _Optional[str] = ..., subscription_id: _Optional[str] = ...) -> None: ...

class SubscribeOrderBookRequest(_message.Message):
    __slots__ = ("subscription_action", "instruments")
    SUBSCRIPTION_ACTION_FIELD_NUMBER: _ClassVar[int]
    INSTRUMENTS_FIELD_NUMBER: _ClassVar[int]
    subscription_action: SubscriptionAction
    instruments: _containers.RepeatedCompositeFieldContainer[OrderBookInstrument]
    def __init__(self, subscription_action: _Optional[_Union[SubscriptionAction, str]] = ..., instruments: _Optional[_Iterable[_Union[OrderBookInstrument, _Mapping]]] = ...) -> None: ...

class OrderBookInstrument(_message.Message):
    __slots__ = ("figi", "depth", "instrument_id", "order_book_type")
    FIGI_FIELD_NUMBER: _ClassVar[int]
    DEPTH_FIELD_NUMBER: _ClassVar[int]
    INSTRUMENT_ID_FIELD_NUMBER: _ClassVar[int]
    ORDER_BOOK_TYPE_FIELD_NUMBER: _ClassVar[int]
    figi: str
    depth: int
    instrument_id: str
    order_book_type: OrderBookType
    def __init__(self, figi: _Optional[str] = ..., depth: _Optional[int] = ..., instrument_id: _Optional[str] = ..., order_book_type: _Optional[_Union[OrderBookType, str]] = ...) -> None: ...

class SubscribeOrderBookResponse(_message.Message):
    __slots__ = ("tracking_id", "order_book_subscriptions")
    TRACKING_ID_FIELD_NUMBER: _ClassVar[int]
    ORDER_BOOK_SUBSCRIPTIONS_FIELD_NUMBER: _ClassVar[int]
    tracking_id: str
    order_book_subscriptions: _containers.RepeatedCompositeFieldContainer[OrderBookSubscription]
    def __init__(self, tracking_id: _Optional[str] = ..., order_book_subscriptions: _Optional[_Iterable[_Union[OrderBookSubscription, _Mapping]]] = ...) -> None: ...

class OrderBookSubscription(_message.Message):
    __slots__ = ("figi", "depth", "subscription_status", "instrument_uid", "stream_id", "subscription_id", "order_book_type")
    FIGI_FIELD_NUMBER: _ClassVar[int]
    DEPTH_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIPTION_STATUS_FIELD_NUMBER: _ClassVar[int]
    INSTRUMENT_UID_FIELD_NUMBER: _ClassVar[int]
    STREAM_ID_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIPTION_ID_FIELD_NUMBER: _ClassVar[int]
    ORDER_BOOK_TYPE_FIELD_NUMBER: _ClassVar[int]
    figi: str
    depth: int
    subscription_status: SubscriptionStatus
    instrument_uid: str
    stream_id: str
    subscription_id: str
    order_book_type: OrderBookType
    def __init__(self, figi: _Optional[str] = ..., depth: _Optional[int] = ..., subscription_status: _Optional[_Union[SubscriptionStatus, str]] = ..., instrument_uid: _Optional[str] = ..., stream_id: _Optional[str] = ..., subscription_id: _Optional[str] = ..., order_book_type: _Optional[_Union[OrderBookType, str]] = ...) -> None: ...

class SubscribeTradesRequest(_message.Message):
    __slots__ = ("subscription_action", "instruments", "trade_type")
    SUBSCRIPTION_ACTION_FIELD_NUMBER: _ClassVar[int]
    INSTRUMENTS_FIELD_NUMBER: _ClassVar[int]
    TRADE_TYPE_FIELD_NUMBER: _ClassVar[int]
    subscription_action: SubscriptionAction
    instruments: _containers.RepeatedCompositeFieldContainer[TradeInstrument]
    trade_type: TradeSourceType
    def __init__(self, subscription_action: _Optional[_Union[SubscriptionAction, str]] = ..., instruments: _Optional[_Iterable[_Union[TradeInstrument, _Mapping]]] = ..., trade_type: _Optional[_Union[TradeSourceType, str]] = ...) -> None: ...

class TradeInstrument(_message.Message):
    __slots__ = ("figi", "instrument_id")
    FIGI_FIELD_NUMBER: _ClassVar[int]
    INSTRUMENT_ID_FIELD_NUMBER: _ClassVar[int]
    figi: str
    instrument_id: str
    def __init__(self, figi: _Optional[str] = ..., instrument_id: _Optional[str] = ...) -> None: ...

class SubscribeTradesResponse(_message.Message):
    __slots__ = ("tracking_id", "trade_subscriptions", "trade_type")
    TRACKING_ID_FIELD_NUMBER: _ClassVar[int]
    TRADE_SUBSCRIPTIONS_FIELD_NUMBER: _ClassVar[int]
    TRADE_TYPE_FIELD_NUMBER: _ClassVar[int]
    tracking_id: str
    trade_subscriptions: _containers.RepeatedCompositeFieldContainer[TradeSubscription]
    trade_type: TradeSourceType
    def __init__(self, tracking_id: _Optional[str] = ..., trade_subscriptions: _Optional[_Iterable[_Union[TradeSubscription, _Mapping]]] = ..., trade_type: _Optional[_Union[TradeSourceType, str]] = ...) -> None: ...

class TradeSubscription(_message.Message):
    __slots__ = ("figi", "subscription_status", "instrument_uid", "stream_id", "subscription_id")
    FIGI_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIPTION_STATUS_FIELD_NUMBER: _ClassVar[int]
    INSTRUMENT_UID_FIELD_NUMBER: _ClassVar[int]
    STREAM_ID_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIPTION_ID_FIELD_NUMBER: _ClassVar[int]
    figi: str
    subscription_status: SubscriptionStatus
    instrument_uid: str
    stream_id: str
    subscription_id: str
    def __init__(self, figi: _Optional[str] = ..., subscription_status: _Optional[_Union[SubscriptionStatus, str]] = ..., instrument_uid: _Optional[str] = ..., stream_id: _Optional[str] = ..., subscription_id: _Optional[str] = ...) -> None: ...

class SubscribeInfoRequest(_message.Message):
    __slots__ = ("subscription_action", "instruments")
    SUBSCRIPTION_ACTION_FIELD_NUMBER: _ClassVar[int]
    INSTRUMENTS_FIELD_NUMBER: _ClassVar[int]
    subscription_action: SubscriptionAction
    instruments: _containers.RepeatedCompositeFieldContainer[InfoInstrument]
    def __init__(self, subscription_action: _Optional[_Union[SubscriptionAction, str]] = ..., instruments: _Optional[_Iterable[_Union[InfoInstrument, _Mapping]]] = ...) -> None: ...

class InfoInstrument(_message.Message):
    __slots__ = ("figi", "instrument_id")
    FIGI_FIELD_NUMBER: _ClassVar[int]
    INSTRUMENT_ID_FIELD_NUMBER: _ClassVar[int]
    figi: str
    instrument_id: str
    def __init__(self, figi: _Optional[str] = ..., instrument_id: _Optional[str] = ...) -> None: ...

class SubscribeInfoResponse(_message.Message):
    __slots__ = ("tracking_id", "info_subscriptions")
    TRACKING_ID_FIELD_NUMBER: _ClassVar[int]
    INFO_SUBSCRIPTIONS_FIELD_NUMBER: _ClassVar[int]
    tracking_id: str
    info_subscriptions: _containers.RepeatedCompositeFieldContainer[InfoSubscription]
    def __init__(self, tracking_id: _Optional[str] = ..., info_subscriptions: _Optional[_Iterable[_Union[InfoSubscription, _Mapping]]] = ...) -> None: ...

class InfoSubscription(_message.Message):
    __slots__ = ("figi", "subscription_status", "instrument_uid", "stream_id", "subscription_id")
    FIGI_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIPTION_STATUS_FIELD_NUMBER: _ClassVar[int]
    INSTRUMENT_UID_FIELD_NUMBER: _ClassVar[int]
    STREAM_ID_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIPTION_ID_FIELD_NUMBER: _ClassVar[int]
    figi: str
    subscription_status: SubscriptionStatus
    instrument_uid: str
    stream_id: str
    subscription_id: str
    def __init__(self, figi: _Optional[str] = ..., subscription_status: _Optional[_Union[SubscriptionStatus, str]] = ..., instrument_uid: _Optional[str] = ..., stream_id: _Optional[str] = ..., subscription_id: _Optional[str] = ...) -> None: ...

class SubscribeLastPriceRequest(_message.Message):
    __slots__ = ("subscription_action", "instruments")
    SUBSCRIPTION_ACTION_FIELD_NUMBER: _ClassVar[int]
    INSTRUMENTS_FIELD_NUMBER: _ClassVar[int]
    subscription_action: SubscriptionAction
    instruments: _containers.RepeatedCompositeFieldContainer[LastPriceInstrument]
    def __init__(self, subscription_action: _Optional[_Union[SubscriptionAction, str]] = ..., instruments: _Optional[_Iterable[_Union[LastPriceInstrument, _Mapping]]] = ...) -> None: ...

class LastPriceInstrument(_message.Message):
    __slots__ = ("figi", "instrument_id")
    FIGI_FIELD_NUMBER: _ClassVar[int]
    INSTRUMENT_ID_FIELD_NUMBER: _ClassVar[int]
    figi: str
    instrument_id: str
    def __init__(self, figi: _Optional[str] = ..., instrument_id: _Optional[str] = ...) -> None: ...

class SubscribeLastPriceResponse(_message.Message):
    __slots__ = ("tracking_id", "last_price_subscriptions")
    TRACKING_ID_FIELD_NUMBER: _ClassVar[int]
    LAST_PRICE_SUBSCRIPTIONS_FIELD_NUMBER: _ClassVar[int]
    tracking_id: str
    last_price_subscriptions: _containers.RepeatedCompositeFieldContainer[LastPriceSubscription]
    def __init__(self, tracking_id: _Optional[str] = ..., last_price_subscriptions: _Optional[_Iterable[_Union[LastPriceSubscription, _Mapping]]] = ...) -> None: ...

class LastPriceSubscription(_message.Message):
    __slots__ = ("figi", "subscription_status", "instrument_uid", "stream_id", "subscription_id")
    FIGI_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIPTION_STATUS_FIELD_NUMBER: _ClassVar[int]
    INSTRUMENT_UID_FIELD_NUMBER: _ClassVar[int]
    STREAM_ID_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIPTION_ID_FIELD_NUMBER: _ClassVar[int]
    figi: str
    subscription_status: SubscriptionStatus
    instrument_uid: str
    stream_id: str
    subscription_id: str
    def __init__(self, figi: _Optional[str] = ..., subscription_status: _Optional[_Union[SubscriptionStatus, str]] = ..., instrument_uid: _Optional[str] = ..., stream_id: _Optional[str] = ..., subscription_id: _Optional[str] = ...) -> None: ...

class Candle(_message.Message):
    __slots__ = ("figi", "interval", "open", "high", "low", "close", "volume", "time", "last_trade_ts", "instrument_uid")
    FIGI_FIELD_NUMBER: _ClassVar[int]
    INTERVAL_FIELD_NUMBER: _ClassVar[int]
    OPEN_FIELD_NUMBER: _ClassVar[int]
    HIGH_FIELD_NUMBER: _ClassVar[int]
    LOW_FIELD_NUMBER: _ClassVar[int]
    CLOSE_FIELD_NUMBER: _ClassVar[int]
    VOLUME_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    LAST_TRADE_TS_FIELD_NUMBER: _ClassVar[int]
    INSTRUMENT_UID_FIELD_NUMBER: _ClassVar[int]
    figi: str
    interval: SubscriptionInterval
    open: _common_pb2.Quotation
    high: _common_pb2.Quotation
    low: _common_pb2.Quotation
    close: _common_pb2.Quotation
    volume: int
    time: _timestamp_pb2.Timestamp
    last_trade_ts: _timestamp_pb2.Timestamp
    instrument_uid: str
    def __init__(self, figi: _Optional[str] = ..., interval: _Optional[_Union[SubscriptionInterval, str]] = ..., open: _Optional[_Union[_common_pb2.Quotation, _Mapping]] = ..., high: _Optional[_Union[_common_pb2.Quotation, _Mapping]] = ..., low: _Optional[_Union[_common_pb2.Quotation, _Mapping]] = ..., close: _Optional[_Union[_common_pb2.Quotation, _Mapping]] = ..., volume: _Optional[int] = ..., time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., last_trade_ts: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., instrument_uid: _Optional[str] = ...) -> None: ...

class OrderBook(_message.Message):
    __slots__ = ("figi", "depth", "is_consistent", "bids", "asks", "time", "limit_up", "limit_down", "instrument_uid", "order_book_type")
    FIGI_FIELD_NUMBER: _ClassVar[int]
    DEPTH_FIELD_NUMBER: _ClassVar[int]
    IS_CONSISTENT_FIELD_NUMBER: _ClassVar[int]
    BIDS_FIELD_NUMBER: _ClassVar[int]
    ASKS_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    LIMIT_UP_FIELD_NUMBER: _ClassVar[int]
    LIMIT_DOWN_FIELD_NUMBER: _ClassVar[int]
    INSTRUMENT_UID_FIELD_NUMBER: _ClassVar[int]
    ORDER_BOOK_TYPE_FIELD_NUMBER: _ClassVar[int]
    figi: str
    depth: int
    is_consistent: bool
    bids: _containers.RepeatedCompositeFieldContainer[Order]
    asks: _containers.RepeatedCompositeFieldContainer[Order]
    time: _timestamp_pb2.Timestamp
    limit_up: _common_pb2.Quotation
    limit_down: _common_pb2.Quotation
    instrument_uid: str
    order_book_type: OrderBookType
    def __init__(self, figi: _Optional[str] = ..., depth: _Optional[int] = ..., is_consistent: bool = ..., bids: _Optional[_Iterable[_Union[Order, _Mapping]]] = ..., asks: _Optional[_Iterable[_Union[Order, _Mapping]]] = ..., time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., limit_up: _Optional[_Union[_common_pb2.Quotation, _Mapping]] = ..., limit_down: _Optional[_Union[_common_pb2.Quotation, _Mapping]] = ..., instrument_uid: _Optional[str] = ..., order_book_type: _Optional[_Union[OrderBookType, str]] = ...) -> None: ...

class Order(_message.Message):
    __slots__ = ("price", "quantity")
    PRICE_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    price: _common_pb2.Quotation
    quantity: int
    def __init__(self, price: _Optional[_Union[_common_pb2.Quotation, _Mapping]] = ..., quantity: _Optional[int] = ...) -> None: ...

class Trade(_message.Message):
    __slots__ = ("figi", "direction", "price", "quantity", "time", "instrument_uid", "tradeSource")
    FIGI_FIELD_NUMBER: _ClassVar[int]
    DIRECTION_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    INSTRUMENT_UID_FIELD_NUMBER: _ClassVar[int]
    TRADESOURCE_FIELD_NUMBER: _ClassVar[int]
    figi: str
    direction: TradeDirection
    price: _common_pb2.Quotation
    quantity: int
    time: _timestamp_pb2.Timestamp
    instrument_uid: str
    tradeSource: TradeSourceType
    def __init__(self, figi: _Optional[str] = ..., direction: _Optional[_Union[TradeDirection, str]] = ..., price: _Optional[_Union[_common_pb2.Quotation, _Mapping]] = ..., quantity: _Optional[int] = ..., time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., instrument_uid: _Optional[str] = ..., tradeSource: _Optional[_Union[TradeSourceType, str]] = ...) -> None: ...

class TradingStatus(_message.Message):
    __slots__ = ("figi", "trading_status", "time", "limit_order_available_flag", "market_order_available_flag", "instrument_uid")
    FIGI_FIELD_NUMBER: _ClassVar[int]
    TRADING_STATUS_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    LIMIT_ORDER_AVAILABLE_FLAG_FIELD_NUMBER: _ClassVar[int]
    MARKET_ORDER_AVAILABLE_FLAG_FIELD_NUMBER: _ClassVar[int]
    INSTRUMENT_UID_FIELD_NUMBER: _ClassVar[int]
    figi: str
    trading_status: _common_pb2.SecurityTradingStatus
    time: _timestamp_pb2.Timestamp
    limit_order_available_flag: bool
    market_order_available_flag: bool
    instrument_uid: str
    def __init__(self, figi: _Optional[str] = ..., trading_status: _Optional[_Union[_common_pb2.SecurityTradingStatus, str]] = ..., time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., limit_order_available_flag: bool = ..., market_order_available_flag: bool = ..., instrument_uid: _Optional[str] = ...) -> None: ...

class GetCandlesRequest(_message.Message):
    __slots__ = ("figi", "to", "interval", "instrument_id", "candle_source_type", "limit")
    class CandleSource(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CANDLE_SOURCE_UNSPECIFIED: _ClassVar[GetCandlesRequest.CandleSource]
        CANDLE_SOURCE_EXCHANGE: _ClassVar[GetCandlesRequest.CandleSource]
        CANDLE_SOURCE_INCLUDE_WEEKEND: _ClassVar[GetCandlesRequest.CandleSource]
    CANDLE_SOURCE_UNSPECIFIED: GetCandlesRequest.CandleSource
    CANDLE_SOURCE_EXCHANGE: GetCandlesRequest.CandleSource
    CANDLE_SOURCE_INCLUDE_WEEKEND: GetCandlesRequest.CandleSource
    FIGI_FIELD_NUMBER: _ClassVar[int]
    FROM_FIELD_NUMBER: _ClassVar[int]
    TO_FIELD_NUMBER: _ClassVar[int]
    INTERVAL_FIELD_NUMBER: _ClassVar[int]
    INSTRUMENT_ID_FIELD_NUMBER: _ClassVar[int]
    CANDLE_SOURCE_TYPE_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    figi: str
    to: _timestamp_pb2.Timestamp
    interval: CandleInterval
    instrument_id: str
    candle_source_type: GetCandlesRequest.CandleSource
    limit: int
    def __init__(self, figi: _Optional[str] = ..., to: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., interval: _Optional[_Union[CandleInterval, str]] = ..., instrument_id: _Optional[str] = ..., candle_source_type: _Optional[_Union[GetCandlesRequest.CandleSource, str]] = ..., limit: _Optional[int] = ..., **kwargs) -> None: ...

class GetCandlesResponse(_message.Message):
    __slots__ = ("candles",)
    CANDLES_FIELD_NUMBER: _ClassVar[int]
    candles: _containers.RepeatedCompositeFieldContainer[HistoricCandle]
    def __init__(self, candles: _Optional[_Iterable[_Union[HistoricCandle, _Mapping]]] = ...) -> None: ...

class HistoricCandle(_message.Message):
    __slots__ = ("open", "high", "low", "close", "volume", "time", "is_complete", "candle_source")
    OPEN_FIELD_NUMBER: _ClassVar[int]
    HIGH_FIELD_NUMBER: _ClassVar[int]
    LOW_FIELD_NUMBER: _ClassVar[int]
    CLOSE_FIELD_NUMBER: _ClassVar[int]
    VOLUME_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    IS_COMPLETE_FIELD_NUMBER: _ClassVar[int]
    CANDLE_SOURCE_FIELD_NUMBER: _ClassVar[int]
    open: _common_pb2.Quotation
    high: _common_pb2.Quotation
    low: _common_pb2.Quotation
    close: _common_pb2.Quotation
    volume: int
    time: _timestamp_pb2.Timestamp
    is_complete: bool
    candle_source: CandleSource
    def __init__(self, open: _Optional[_Union[_common_pb2.Quotation, _Mapping]] = ..., high: _Optional[_Union[_common_pb2.Quotation, _Mapping]] = ..., low: _Optional[_Union[_common_pb2.Quotation, _Mapping]] = ..., close: _Optional[_Union[_common_pb2.Quotation, _Mapping]] = ..., volume: _Optional[int] = ..., time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., is_complete: bool = ..., candle_source: _Optional[_Union[CandleSource, str]] = ...) -> None: ...

class GetLastPricesRequest(_message.Message):
    __slots__ = ("figi", "instrument_id", "last_price_type")
    FIGI_FIELD_NUMBER: _ClassVar[int]
    INSTRUMENT_ID_FIELD_NUMBER: _ClassVar[int]
    LAST_PRICE_TYPE_FIELD_NUMBER: _ClassVar[int]
    figi: _containers.RepeatedScalarFieldContainer[str]
    instrument_id: _containers.RepeatedScalarFieldContainer[str]
    last_price_type: LastPriceType
    def __init__(self, figi: _Optional[_Iterable[str]] = ..., instrument_id: _Optional[_Iterable[str]] = ..., last_price_type: _Optional[_Union[LastPriceType, str]] = ...) -> None: ...

class GetLastPricesResponse(_message.Message):
    __slots__ = ("last_prices",)
    LAST_PRICES_FIELD_NUMBER: _ClassVar[int]
    last_prices: _containers.RepeatedCompositeFieldContainer[LastPrice]
    def __init__(self, last_prices: _Optional[_Iterable[_Union[LastPrice, _Mapping]]] = ...) -> None: ...

class LastPrice(_message.Message):
    __slots__ = ("figi", "price", "time", "instrument_uid", "last_price_type")
    FIGI_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    INSTRUMENT_UID_FIELD_NUMBER: _ClassVar[int]
    LAST_PRICE_TYPE_FIELD_NUMBER: _ClassVar[int]
    figi: str
    price: _common_pb2.Quotation
    time: _timestamp_pb2.Timestamp
    instrument_uid: str
    last_price_type: LastPriceType
    def __init__(self, figi: _Optional[str] = ..., price: _Optional[_Union[_common_pb2.Quotation, _Mapping]] = ..., time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., instrument_uid: _Optional[str] = ..., last_price_type: _Optional[_Union[LastPriceType, str]] = ...) -> None: ...

class GetOrderBookRequest(_message.Message):
    __slots__ = ("figi", "depth", "instrument_id")
    FIGI_FIELD_NUMBER: _ClassVar[int]
    DEPTH_FIELD_NUMBER: _ClassVar[int]
    INSTRUMENT_ID_FIELD_NUMBER: _ClassVar[int]
    figi: str
    depth: int
    instrument_id: str
    def __init__(self, figi: _Optional[str] = ..., depth: _Optional[int] = ..., instrument_id: _Optional[str] = ...) -> None: ...

class GetOrderBookResponse(_message.Message):
    __slots__ = ("figi", "depth", "bids", "asks", "last_price", "close_price", "limit_up", "limit_down", "last_price_ts", "close_price_ts", "orderbook_ts", "instrument_uid")
    FIGI_FIELD_NUMBER: _ClassVar[int]
    DEPTH_FIELD_NUMBER: _ClassVar[int]
    BIDS_FIELD_NUMBER: _ClassVar[int]
    ASKS_FIELD_NUMBER: _ClassVar[int]
    LAST_PRICE_FIELD_NUMBER: _ClassVar[int]
    CLOSE_PRICE_FIELD_NUMBER: _ClassVar[int]
    LIMIT_UP_FIELD_NUMBER: _ClassVar[int]
    LIMIT_DOWN_FIELD_NUMBER: _ClassVar[int]
    LAST_PRICE_TS_FIELD_NUMBER: _ClassVar[int]
    CLOSE_PRICE_TS_FIELD_NUMBER: _ClassVar[int]
    ORDERBOOK_TS_FIELD_NUMBER: _ClassVar[int]
    INSTRUMENT_UID_FIELD_NUMBER: _ClassVar[int]
    figi: str
    depth: int
    bids: _containers.RepeatedCompositeFieldContainer[Order]
    asks: _containers.RepeatedCompositeFieldContainer[Order]
    last_price: _common_pb2.Quotation
    close_price: _common_pb2.Quotation
    limit_up: _common_pb2.Quotation
    limit_down: _common_pb2.Quotation
    last_price_ts: _timestamp_pb2.Timestamp
    close_price_ts: _timestamp_pb2.Timestamp
    orderbook_ts: _timestamp_pb2.Timestamp
    instrument_uid: str
    def __init__(self, figi: _Optional[str] = ..., depth: _Optional[int] = ..., bids: _Optional[_Iterable[_Union[Order, _Mapping]]] = ..., asks: _Optional[_Iterable[_Union[Order, _Mapping]]] = ..., last_price: _Optional[_Union[_common_pb2.Quotation, _Mapping]] = ..., close_price: _Optional[_Union[_common_pb2.Quotation, _Mapping]] = ..., limit_up: _Optional[_Union[_common_pb2.Quotation, _Mapping]] = ..., limit_down: _Optional[_Union[_common_pb2.Quotation, _Mapping]] = ..., last_price_ts: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., close_price_ts: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., orderbook_ts: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., instrument_uid: _Optional[str] = ...) -> None: ...

class GetTradingStatusRequest(_message.Message):
    __slots__ = ("figi", "instrument_id")
    FIGI_FIELD_NUMBER: _ClassVar[int]
    INSTRUMENT_ID_FIELD_NUMBER: _ClassVar[int]
    figi: str
    instrument_id: str
    def __init__(self, figi: _Optional[str] = ..., instrument_id: _Optional[str] = ...) -> None: ...

class GetTradingStatusesRequest(_message.Message):
    __slots__ = ("instrument_id",)
    INSTRUMENT_ID_FIELD_NUMBER: _ClassVar[int]
    instrument_id: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, instrument_id: _Optional[_Iterable[str]] = ...) -> None: ...

class GetTradingStatusesResponse(_message.Message):
    __slots__ = ("trading_statuses",)
    TRADING_STATUSES_FIELD_NUMBER: _ClassVar[int]
    trading_statuses: _containers.RepeatedCompositeFieldContainer[GetTradingStatusResponse]
    def __init__(self, trading_statuses: _Optional[_Iterable[_Union[GetTradingStatusResponse, _Mapping]]] = ...) -> None: ...

class GetTradingStatusResponse(_message.Message):
    __slots__ = ("figi", "trading_status", "limit_order_available_flag", "market_order_available_flag", "api_trade_available_flag", "instrument_uid", "bestprice_order_available_flag", "only_best_price")
    FIGI_FIELD_NUMBER: _ClassVar[int]
    TRADING_STATUS_FIELD_NUMBER: _ClassVar[int]
    LIMIT_ORDER_AVAILABLE_FLAG_FIELD_NUMBER: _ClassVar[int]
    MARKET_ORDER_AVAILABLE_FLAG_FIELD_NUMBER: _ClassVar[int]
    API_TRADE_AVAILABLE_FLAG_FIELD_NUMBER: _ClassVar[int]
    INSTRUMENT_UID_FIELD_NUMBER: _ClassVar[int]
    BESTPRICE_ORDER_AVAILABLE_FLAG_FIELD_NUMBER: _ClassVar[int]
    ONLY_BEST_PRICE_FIELD_NUMBER: _ClassVar[int]
    figi: str
    trading_status: _common_pb2.SecurityTradingStatus
    limit_order_available_flag: bool
    market_order_available_flag: bool
    api_trade_available_flag: bool
    instrument_uid: str
    bestprice_order_available_flag: bool
    only_best_price: bool
    def __init__(self, figi: _Optional[str] = ..., trading_status: _Optional[_Union[_common_pb2.SecurityTradingStatus, str]] = ..., limit_order_available_flag: bool = ..., market_order_available_flag: bool = ..., api_trade_available_flag: bool = ..., instrument_uid: _Optional[str] = ..., bestprice_order_available_flag: bool = ..., only_best_price: bool = ...) -> None: ...

class GetLastTradesRequest(_message.Message):
    __slots__ = ("figi", "to", "instrument_id")
    FIGI_FIELD_NUMBER: _ClassVar[int]
    FROM_FIELD_NUMBER: _ClassVar[int]
    TO_FIELD_NUMBER: _ClassVar[int]
    INSTRUMENT_ID_FIELD_NUMBER: _ClassVar[int]
    figi: str
    to: _timestamp_pb2.Timestamp
    instrument_id: str
    def __init__(self, figi: _Optional[str] = ..., to: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., instrument_id: _Optional[str] = ..., **kwargs) -> None: ...

class GetLastTradesResponse(_message.Message):
    __slots__ = ("trades",)
    TRADES_FIELD_NUMBER: _ClassVar[int]
    trades: _containers.RepeatedCompositeFieldContainer[Trade]
    def __init__(self, trades: _Optional[_Iterable[_Union[Trade, _Mapping]]] = ...) -> None: ...

class GetMySubscriptions(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetClosePricesRequest(_message.Message):
    __slots__ = ("instruments",)
    INSTRUMENTS_FIELD_NUMBER: _ClassVar[int]
    instruments: _containers.RepeatedCompositeFieldContainer[InstrumentClosePriceRequest]
    def __init__(self, instruments: _Optional[_Iterable[_Union[InstrumentClosePriceRequest, _Mapping]]] = ...) -> None: ...

class InstrumentClosePriceRequest(_message.Message):
    __slots__ = ("instrument_id",)
    INSTRUMENT_ID_FIELD_NUMBER: _ClassVar[int]
    instrument_id: str
    def __init__(self, instrument_id: _Optional[str] = ...) -> None: ...

class GetClosePricesResponse(_message.Message):
    __slots__ = ("close_prices",)
    CLOSE_PRICES_FIELD_NUMBER: _ClassVar[int]
    close_prices: _containers.RepeatedCompositeFieldContainer[InstrumentClosePriceResponse]
    def __init__(self, close_prices: _Optional[_Iterable[_Union[InstrumentClosePriceResponse, _Mapping]]] = ...) -> None: ...

class InstrumentClosePriceResponse(_message.Message):
    __slots__ = ("figi", "instrument_uid", "price", "evening_session_price", "time")
    FIGI_FIELD_NUMBER: _ClassVar[int]
    INSTRUMENT_UID_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    EVENING_SESSION_PRICE_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    figi: str
    instrument_uid: str
    price: _common_pb2.Quotation
    evening_session_price: _common_pb2.Quotation
    time: _timestamp_pb2.Timestamp
    def __init__(self, figi: _Optional[str] = ..., instrument_uid: _Optional[str] = ..., price: _Optional[_Union[_common_pb2.Quotation, _Mapping]] = ..., evening_session_price: _Optional[_Union[_common_pb2.Quotation, _Mapping]] = ..., time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class GetTechAnalysisRequest(_message.Message):
    __slots__ = ("indicator_type", "instrument_uid", "to", "interval", "type_of_price", "length", "deviation", "smoothing")
    class IndicatorInterval(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        INDICATOR_INTERVAL_UNSPECIFIED: _ClassVar[GetTechAnalysisRequest.IndicatorInterval]
        INDICATOR_INTERVAL_ONE_MINUTE: _ClassVar[GetTechAnalysisRequest.IndicatorInterval]
        INDICATOR_INTERVAL_FIVE_MINUTES: _ClassVar[GetTechAnalysisRequest.IndicatorInterval]
        INDICATOR_INTERVAL_FIFTEEN_MINUTES: _ClassVar[GetTechAnalysisRequest.IndicatorInterval]
        INDICATOR_INTERVAL_ONE_HOUR: _ClassVar[GetTechAnalysisRequest.IndicatorInterval]
        INDICATOR_INTERVAL_ONE_DAY: _ClassVar[GetTechAnalysisRequest.IndicatorInterval]
        INDICATOR_INTERVAL_2_MIN: _ClassVar[GetTechAnalysisRequest.IndicatorInterval]
        INDICATOR_INTERVAL_3_MIN: _ClassVar[GetTechAnalysisRequest.IndicatorInterval]
        INDICATOR_INTERVAL_10_MIN: _ClassVar[GetTechAnalysisRequest.IndicatorInterval]
        INDICATOR_INTERVAL_30_MIN: _ClassVar[GetTechAnalysisRequest.IndicatorInterval]
        INDICATOR_INTERVAL_2_HOUR: _ClassVar[GetTechAnalysisRequest.IndicatorInterval]
        INDICATOR_INTERVAL_4_HOUR: _ClassVar[GetTechAnalysisRequest.IndicatorInterval]
        INDICATOR_INTERVAL_WEEK: _ClassVar[GetTechAnalysisRequest.IndicatorInterval]
        INDICATOR_INTERVAL_MONTH: _ClassVar[GetTechAnalysisRequest.IndicatorInterval]
    INDICATOR_INTERVAL_UNSPECIFIED: GetTechAnalysisRequest.IndicatorInterval
    INDICATOR_INTERVAL_ONE_MINUTE: GetTechAnalysisRequest.IndicatorInterval
    INDICATOR_INTERVAL_FIVE_MINUTES: GetTechAnalysisRequest.IndicatorInterval
    INDICATOR_INTERVAL_FIFTEEN_MINUTES: GetTechAnalysisRequest.IndicatorInterval
    INDICATOR_INTERVAL_ONE_HOUR: GetTechAnalysisRequest.IndicatorInterval
    INDICATOR_INTERVAL_ONE_DAY: GetTechAnalysisRequest.IndicatorInterval
    INDICATOR_INTERVAL_2_MIN: GetTechAnalysisRequest.IndicatorInterval
    INDICATOR_INTERVAL_3_MIN: GetTechAnalysisRequest.IndicatorInterval
    INDICATOR_INTERVAL_10_MIN: GetTechAnalysisRequest.IndicatorInterval
    INDICATOR_INTERVAL_30_MIN: GetTechAnalysisRequest.IndicatorInterval
    INDICATOR_INTERVAL_2_HOUR: GetTechAnalysisRequest.IndicatorInterval
    INDICATOR_INTERVAL_4_HOUR: GetTechAnalysisRequest.IndicatorInterval
    INDICATOR_INTERVAL_WEEK: GetTechAnalysisRequest.IndicatorInterval
    INDICATOR_INTERVAL_MONTH: GetTechAnalysisRequest.IndicatorInterval
    class TypeOfPrice(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TYPE_OF_PRICE_UNSPECIFIED: _ClassVar[GetTechAnalysisRequest.TypeOfPrice]
        TYPE_OF_PRICE_CLOSE: _ClassVar[GetTechAnalysisRequest.TypeOfPrice]
        TYPE_OF_PRICE_OPEN: _ClassVar[GetTechAnalysisRequest.TypeOfPrice]
        TYPE_OF_PRICE_HIGH: _ClassVar[GetTechAnalysisRequest.TypeOfPrice]
        TYPE_OF_PRICE_LOW: _ClassVar[GetTechAnalysisRequest.TypeOfPrice]
        TYPE_OF_PRICE_AVG: _ClassVar[GetTechAnalysisRequest.TypeOfPrice]
    TYPE_OF_PRICE_UNSPECIFIED: GetTechAnalysisRequest.TypeOfPrice
    TYPE_OF_PRICE_CLOSE: GetTechAnalysisRequest.TypeOfPrice
    TYPE_OF_PRICE_OPEN: GetTechAnalysisRequest.TypeOfPrice
    TYPE_OF_PRICE_HIGH: GetTechAnalysisRequest.TypeOfPrice
    TYPE_OF_PRICE_LOW: GetTechAnalysisRequest.TypeOfPrice
    TYPE_OF_PRICE_AVG: GetTechAnalysisRequest.TypeOfPrice
    class IndicatorType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        INDICATOR_TYPE_UNSPECIFIED: _ClassVar[GetTechAnalysisRequest.IndicatorType]
        INDICATOR_TYPE_BB: _ClassVar[GetTechAnalysisRequest.IndicatorType]
        INDICATOR_TYPE_EMA: _ClassVar[GetTechAnalysisRequest.IndicatorType]
        INDICATOR_TYPE_RSI: _ClassVar[GetTechAnalysisRequest.IndicatorType]
        INDICATOR_TYPE_MACD: _ClassVar[GetTechAnalysisRequest.IndicatorType]
        INDICATOR_TYPE_SMA: _ClassVar[GetTechAnalysisRequest.IndicatorType]
    INDICATOR_TYPE_UNSPECIFIED: GetTechAnalysisRequest.IndicatorType
    INDICATOR_TYPE_BB: GetTechAnalysisRequest.IndicatorType
    INDICATOR_TYPE_EMA: GetTechAnalysisRequest.IndicatorType
    INDICATOR_TYPE_RSI: GetTechAnalysisRequest.IndicatorType
    INDICATOR_TYPE_MACD: GetTechAnalysisRequest.IndicatorType
    INDICATOR_TYPE_SMA: GetTechAnalysisRequest.IndicatorType
    class Smoothing(_message.Message):
        __slots__ = ("fast_length", "slow_length", "signal_smoothing")
        FAST_LENGTH_FIELD_NUMBER: _ClassVar[int]
        SLOW_LENGTH_FIELD_NUMBER: _ClassVar[int]
        SIGNAL_SMOOTHING_FIELD_NUMBER: _ClassVar[int]
        fast_length: int
        slow_length: int
        signal_smoothing: int
        def __init__(self, fast_length: _Optional[int] = ..., slow_length: _Optional[int] = ..., signal_smoothing: _Optional[int] = ...) -> None: ...
    class Deviation(_message.Message):
        __slots__ = ("deviation_multiplier",)
        DEVIATION_MULTIPLIER_FIELD_NUMBER: _ClassVar[int]
        deviation_multiplier: _common_pb2.Quotation
        def __init__(self, deviation_multiplier: _Optional[_Union[_common_pb2.Quotation, _Mapping]] = ...) -> None: ...
    INDICATOR_TYPE_FIELD_NUMBER: _ClassVar[int]
    INSTRUMENT_UID_FIELD_NUMBER: _ClassVar[int]
    FROM_FIELD_NUMBER: _ClassVar[int]
    TO_FIELD_NUMBER: _ClassVar[int]
    INTERVAL_FIELD_NUMBER: _ClassVar[int]
    TYPE_OF_PRICE_FIELD_NUMBER: _ClassVar[int]
    LENGTH_FIELD_NUMBER: _ClassVar[int]
    DEVIATION_FIELD_NUMBER: _ClassVar[int]
    SMOOTHING_FIELD_NUMBER: _ClassVar[int]
    indicator_type: GetTechAnalysisRequest.IndicatorType
    instrument_uid: str
    to: _timestamp_pb2.Timestamp
    interval: GetTechAnalysisRequest.IndicatorInterval
    type_of_price: GetTechAnalysisRequest.TypeOfPrice
    length: int
    deviation: GetTechAnalysisRequest.Deviation
    smoothing: GetTechAnalysisRequest.Smoothing
    def __init__(self, indicator_type: _Optional[_Union[GetTechAnalysisRequest.IndicatorType, str]] = ..., instrument_uid: _Optional[str] = ..., to: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., interval: _Optional[_Union[GetTechAnalysisRequest.IndicatorInterval, str]] = ..., type_of_price: _Optional[_Union[GetTechAnalysisRequest.TypeOfPrice, str]] = ..., length: _Optional[int] = ..., deviation: _Optional[_Union[GetTechAnalysisRequest.Deviation, _Mapping]] = ..., smoothing: _Optional[_Union[GetTechAnalysisRequest.Smoothing, _Mapping]] = ..., **kwargs) -> None: ...

class GetTechAnalysisResponse(_message.Message):
    __slots__ = ("technical_indicators",)
    class TechAnalysisItem(_message.Message):
        __slots__ = ("timestamp", "middle_band", "upper_band", "lower_band", "signal", "macd")
        TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
        MIDDLE_BAND_FIELD_NUMBER: _ClassVar[int]
        UPPER_BAND_FIELD_NUMBER: _ClassVar[int]
        LOWER_BAND_FIELD_NUMBER: _ClassVar[int]
        SIGNAL_FIELD_NUMBER: _ClassVar[int]
        MACD_FIELD_NUMBER: _ClassVar[int]
        timestamp: _timestamp_pb2.Timestamp
        middle_band: _common_pb2.Quotation
        upper_band: _common_pb2.Quotation
        lower_band: _common_pb2.Quotation
        signal: _common_pb2.Quotation
        macd: _common_pb2.Quotation
        def __init__(self, timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., middle_band: _Optional[_Union[_common_pb2.Quotation, _Mapping]] = ..., upper_band: _Optional[_Union[_common_pb2.Quotation, _Mapping]] = ..., lower_band: _Optional[_Union[_common_pb2.Quotation, _Mapping]] = ..., signal: _Optional[_Union[_common_pb2.Quotation, _Mapping]] = ..., macd: _Optional[_Union[_common_pb2.Quotation, _Mapping]] = ...) -> None: ...
    TECHNICAL_INDICATORS_FIELD_NUMBER: _ClassVar[int]
    technical_indicators: _containers.RepeatedCompositeFieldContainer[GetTechAnalysisResponse.TechAnalysisItem]
    def __init__(self, technical_indicators: _Optional[_Iterable[_Union[GetTechAnalysisResponse.TechAnalysisItem, _Mapping]]] = ...) -> None: ...
