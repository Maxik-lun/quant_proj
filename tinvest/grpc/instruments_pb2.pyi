from google.protobuf import timestamp_pb2 as _timestamp_pb2
from tinvest.grpc import common_pb2 as _common_pb2
from tinvest.grpc.google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CouponType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    COUPON_TYPE_UNSPECIFIED: _ClassVar[CouponType]
    COUPON_TYPE_CONSTANT: _ClassVar[CouponType]
    COUPON_TYPE_FLOATING: _ClassVar[CouponType]
    COUPON_TYPE_DISCOUNT: _ClassVar[CouponType]
    COUPON_TYPE_MORTGAGE: _ClassVar[CouponType]
    COUPON_TYPE_FIX: _ClassVar[CouponType]
    COUPON_TYPE_VARIABLE: _ClassVar[CouponType]
    COUPON_TYPE_OTHER: _ClassVar[CouponType]

class OptionDirection(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    OPTION_DIRECTION_UNSPECIFIED: _ClassVar[OptionDirection]
    OPTION_DIRECTION_PUT: _ClassVar[OptionDirection]
    OPTION_DIRECTION_CALL: _ClassVar[OptionDirection]

class OptionPaymentType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    OPTION_PAYMENT_TYPE_UNSPECIFIED: _ClassVar[OptionPaymentType]
    OPTION_PAYMENT_TYPE_PREMIUM: _ClassVar[OptionPaymentType]
    OPTION_PAYMENT_TYPE_MARGINAL: _ClassVar[OptionPaymentType]

class OptionStyle(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    OPTION_STYLE_UNSPECIFIED: _ClassVar[OptionStyle]
    OPTION_STYLE_AMERICAN: _ClassVar[OptionStyle]
    OPTION_STYLE_EUROPEAN: _ClassVar[OptionStyle]

class OptionSettlementType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    OPTION_EXECUTION_TYPE_UNSPECIFIED: _ClassVar[OptionSettlementType]
    OPTION_EXECUTION_TYPE_PHYSICAL_DELIVERY: _ClassVar[OptionSettlementType]
    OPTION_EXECUTION_TYPE_CASH_SETTLEMENT: _ClassVar[OptionSettlementType]

class InstrumentIdType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    INSTRUMENT_ID_UNSPECIFIED: _ClassVar[InstrumentIdType]
    INSTRUMENT_ID_TYPE_FIGI: _ClassVar[InstrumentIdType]
    INSTRUMENT_ID_TYPE_TICKER: _ClassVar[InstrumentIdType]
    INSTRUMENT_ID_TYPE_UID: _ClassVar[InstrumentIdType]
    INSTRUMENT_ID_TYPE_POSITION_UID: _ClassVar[InstrumentIdType]

class InstrumentStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    INSTRUMENT_STATUS_UNSPECIFIED: _ClassVar[InstrumentStatus]
    INSTRUMENT_STATUS_BASE: _ClassVar[InstrumentStatus]
    INSTRUMENT_STATUS_ALL: _ClassVar[InstrumentStatus]

class ShareType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SHARE_TYPE_UNSPECIFIED: _ClassVar[ShareType]
    SHARE_TYPE_COMMON: _ClassVar[ShareType]
    SHARE_TYPE_PREFERRED: _ClassVar[ShareType]
    SHARE_TYPE_ADR: _ClassVar[ShareType]
    SHARE_TYPE_GDR: _ClassVar[ShareType]
    SHARE_TYPE_MLP: _ClassVar[ShareType]
    SHARE_TYPE_NY_REG_SHRS: _ClassVar[ShareType]
    SHARE_TYPE_CLOSED_END_FUND: _ClassVar[ShareType]
    SHARE_TYPE_REIT: _ClassVar[ShareType]

class AssetType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ASSET_TYPE_UNSPECIFIED: _ClassVar[AssetType]
    ASSET_TYPE_CURRENCY: _ClassVar[AssetType]
    ASSET_TYPE_COMMODITY: _ClassVar[AssetType]
    ASSET_TYPE_INDEX: _ClassVar[AssetType]
    ASSET_TYPE_SECURITY: _ClassVar[AssetType]

class StructuredProductType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SP_TYPE_UNSPECIFIED: _ClassVar[StructuredProductType]
    SP_TYPE_DELIVERABLE: _ClassVar[StructuredProductType]
    SP_TYPE_NON_DELIVERABLE: _ClassVar[StructuredProductType]

class EditFavoritesActionType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EDIT_FAVORITES_ACTION_TYPE_UNSPECIFIED: _ClassVar[EditFavoritesActionType]
    EDIT_FAVORITES_ACTION_TYPE_ADD: _ClassVar[EditFavoritesActionType]
    EDIT_FAVORITES_ACTION_TYPE_DEL: _ClassVar[EditFavoritesActionType]

class RealExchange(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    REAL_EXCHANGE_UNSPECIFIED: _ClassVar[RealExchange]
    REAL_EXCHANGE_MOEX: _ClassVar[RealExchange]
    REAL_EXCHANGE_RTS: _ClassVar[RealExchange]
    REAL_EXCHANGE_OTC: _ClassVar[RealExchange]
    REAL_EXCHANGE_DEALER: _ClassVar[RealExchange]

class Recommendation(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    RECOMMENDATION_UNSPECIFIED: _ClassVar[Recommendation]
    RECOMMENDATION_BUY: _ClassVar[Recommendation]
    RECOMMENDATION_HOLD: _ClassVar[Recommendation]
    RECOMMENDATION_SELL: _ClassVar[Recommendation]

class RiskLevel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    RISK_LEVEL_UNSPECIFIED: _ClassVar[RiskLevel]
    RISK_LEVEL_LOW: _ClassVar[RiskLevel]
    RISK_LEVEL_MODERATE: _ClassVar[RiskLevel]
    RISK_LEVEL_HIGH: _ClassVar[RiskLevel]

class BondType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    BOND_TYPE_UNSPECIFIED: _ClassVar[BondType]
    BOND_TYPE_REPLACED: _ClassVar[BondType]

class InstrumentExchangeType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    INSTRUMENT_EXCHANGE_UNSPECIFIED: _ClassVar[InstrumentExchangeType]
    INSTRUMENT_EXCHANGE_DEALER: _ClassVar[InstrumentExchangeType]
COUPON_TYPE_UNSPECIFIED: CouponType
COUPON_TYPE_CONSTANT: CouponType
COUPON_TYPE_FLOATING: CouponType
COUPON_TYPE_DISCOUNT: CouponType
COUPON_TYPE_MORTGAGE: CouponType
COUPON_TYPE_FIX: CouponType
COUPON_TYPE_VARIABLE: CouponType
COUPON_TYPE_OTHER: CouponType
OPTION_DIRECTION_UNSPECIFIED: OptionDirection
OPTION_DIRECTION_PUT: OptionDirection
OPTION_DIRECTION_CALL: OptionDirection
OPTION_PAYMENT_TYPE_UNSPECIFIED: OptionPaymentType
OPTION_PAYMENT_TYPE_PREMIUM: OptionPaymentType
OPTION_PAYMENT_TYPE_MARGINAL: OptionPaymentType
OPTION_STYLE_UNSPECIFIED: OptionStyle
OPTION_STYLE_AMERICAN: OptionStyle
OPTION_STYLE_EUROPEAN: OptionStyle
OPTION_EXECUTION_TYPE_UNSPECIFIED: OptionSettlementType
OPTION_EXECUTION_TYPE_PHYSICAL_DELIVERY: OptionSettlementType
OPTION_EXECUTION_TYPE_CASH_SETTLEMENT: OptionSettlementType
INSTRUMENT_ID_UNSPECIFIED: InstrumentIdType
INSTRUMENT_ID_TYPE_FIGI: InstrumentIdType
INSTRUMENT_ID_TYPE_TICKER: InstrumentIdType
INSTRUMENT_ID_TYPE_UID: InstrumentIdType
INSTRUMENT_ID_TYPE_POSITION_UID: InstrumentIdType
INSTRUMENT_STATUS_UNSPECIFIED: InstrumentStatus
INSTRUMENT_STATUS_BASE: InstrumentStatus
INSTRUMENT_STATUS_ALL: InstrumentStatus
SHARE_TYPE_UNSPECIFIED: ShareType
SHARE_TYPE_COMMON: ShareType
SHARE_TYPE_PREFERRED: ShareType
SHARE_TYPE_ADR: ShareType
SHARE_TYPE_GDR: ShareType
SHARE_TYPE_MLP: ShareType
SHARE_TYPE_NY_REG_SHRS: ShareType
SHARE_TYPE_CLOSED_END_FUND: ShareType
SHARE_TYPE_REIT: ShareType
ASSET_TYPE_UNSPECIFIED: AssetType
ASSET_TYPE_CURRENCY: AssetType
ASSET_TYPE_COMMODITY: AssetType
ASSET_TYPE_INDEX: AssetType
ASSET_TYPE_SECURITY: AssetType
SP_TYPE_UNSPECIFIED: StructuredProductType
SP_TYPE_DELIVERABLE: StructuredProductType
SP_TYPE_NON_DELIVERABLE: StructuredProductType
EDIT_FAVORITES_ACTION_TYPE_UNSPECIFIED: EditFavoritesActionType
EDIT_FAVORITES_ACTION_TYPE_ADD: EditFavoritesActionType
EDIT_FAVORITES_ACTION_TYPE_DEL: EditFavoritesActionType
REAL_EXCHANGE_UNSPECIFIED: RealExchange
REAL_EXCHANGE_MOEX: RealExchange
REAL_EXCHANGE_RTS: RealExchange
REAL_EXCHANGE_OTC: RealExchange
REAL_EXCHANGE_DEALER: RealExchange
RECOMMENDATION_UNSPECIFIED: Recommendation
RECOMMENDATION_BUY: Recommendation
RECOMMENDATION_HOLD: Recommendation
RECOMMENDATION_SELL: Recommendation
RISK_LEVEL_UNSPECIFIED: RiskLevel
RISK_LEVEL_LOW: RiskLevel
RISK_LEVEL_MODERATE: RiskLevel
RISK_LEVEL_HIGH: RiskLevel
BOND_TYPE_UNSPECIFIED: BondType
BOND_TYPE_REPLACED: BondType
INSTRUMENT_EXCHANGE_UNSPECIFIED: InstrumentExchangeType
INSTRUMENT_EXCHANGE_DEALER: InstrumentExchangeType

class TradingSchedulesRequest(_message.Message):
    __slots__ = ("exchange", "to")
    EXCHANGE_FIELD_NUMBER: _ClassVar[int]
    FROM_FIELD_NUMBER: _ClassVar[int]
    TO_FIELD_NUMBER: _ClassVar[int]
    exchange: str
    to: _timestamp_pb2.Timestamp
    def __init__(self, exchange: _Optional[str] = ..., to: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., **kwargs) -> None: ...

class TradingSchedulesResponse(_message.Message):
    __slots__ = ("exchanges",)
    EXCHANGES_FIELD_NUMBER: _ClassVar[int]
    exchanges: _containers.RepeatedCompositeFieldContainer[TradingSchedule]
    def __init__(self, exchanges: _Optional[_Iterable[_Union[TradingSchedule, _Mapping]]] = ...) -> None: ...

class TradingSchedule(_message.Message):
    __slots__ = ("exchange", "days")
    EXCHANGE_FIELD_NUMBER: _ClassVar[int]
    DAYS_FIELD_NUMBER: _ClassVar[int]
    exchange: str
    days: _containers.RepeatedCompositeFieldContainer[TradingDay]
    def __init__(self, exchange: _Optional[str] = ..., days: _Optional[_Iterable[_Union[TradingDay, _Mapping]]] = ...) -> None: ...

class TradingDay(_message.Message):
    __slots__ = ("date", "is_trading_day", "start_time", "end_time", "opening_auction_start_time", "closing_auction_end_time", "evening_opening_auction_start_time", "evening_start_time", "evening_end_time", "clearing_start_time", "clearing_end_time", "premarket_start_time", "premarket_end_time", "closing_auction_start_time", "opening_auction_end_time", "intervals")
    DATE_FIELD_NUMBER: _ClassVar[int]
    IS_TRADING_DAY_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    OPENING_AUCTION_START_TIME_FIELD_NUMBER: _ClassVar[int]
    CLOSING_AUCTION_END_TIME_FIELD_NUMBER: _ClassVar[int]
    EVENING_OPENING_AUCTION_START_TIME_FIELD_NUMBER: _ClassVar[int]
    EVENING_START_TIME_FIELD_NUMBER: _ClassVar[int]
    EVENING_END_TIME_FIELD_NUMBER: _ClassVar[int]
    CLEARING_START_TIME_FIELD_NUMBER: _ClassVar[int]
    CLEARING_END_TIME_FIELD_NUMBER: _ClassVar[int]
    PREMARKET_START_TIME_FIELD_NUMBER: _ClassVar[int]
    PREMARKET_END_TIME_FIELD_NUMBER: _ClassVar[int]
    CLOSING_AUCTION_START_TIME_FIELD_NUMBER: _ClassVar[int]
    OPENING_AUCTION_END_TIME_FIELD_NUMBER: _ClassVar[int]
    INTERVALS_FIELD_NUMBER: _ClassVar[int]
    date: _timestamp_pb2.Timestamp
    is_trading_day: bool
    start_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp
    opening_auction_start_time: _timestamp_pb2.Timestamp
    closing_auction_end_time: _timestamp_pb2.Timestamp
    evening_opening_auction_start_time: _timestamp_pb2.Timestamp
    evening_start_time: _timestamp_pb2.Timestamp
    evening_end_time: _timestamp_pb2.Timestamp
    clearing_start_time: _timestamp_pb2.Timestamp
    clearing_end_time: _timestamp_pb2.Timestamp
    premarket_start_time: _timestamp_pb2.Timestamp
    premarket_end_time: _timestamp_pb2.Timestamp
    closing_auction_start_time: _timestamp_pb2.Timestamp
    opening_auction_end_time: _timestamp_pb2.Timestamp
    intervals: _containers.RepeatedCompositeFieldContainer[TradingInterval]
    def __init__(self, date: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., is_trading_day: bool = ..., start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., opening_auction_start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., closing_auction_end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., evening_opening_auction_start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., evening_start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., evening_end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., clearing_start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., clearing_end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., premarket_start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., premarket_end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., closing_auction_start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., opening_auction_end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., intervals: _Optional[_Iterable[_Union[TradingInterval, _Mapping]]] = ...) -> None: ...

class InstrumentRequest(_message.Message):
    __slots__ = ("id_type", "class_code", "id")
    ID_TYPE_FIELD_NUMBER: _ClassVar[int]
    CLASS_CODE_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    id_type: InstrumentIdType
    class_code: str
    id: str
    def __init__(self, id_type: _Optional[_Union[InstrumentIdType, str]] = ..., class_code: _Optional[str] = ..., id: _Optional[str] = ...) -> None: ...

class InstrumentsRequest(_message.Message):
    __slots__ = ("instrument_status", "instrument_exchange")
    INSTRUMENT_STATUS_FIELD_NUMBER: _ClassVar[int]
    INSTRUMENT_EXCHANGE_FIELD_NUMBER: _ClassVar[int]
    instrument_status: InstrumentStatus
    instrument_exchange: InstrumentExchangeType
    def __init__(self, instrument_status: _Optional[_Union[InstrumentStatus, str]] = ..., instrument_exchange: _Optional[_Union[InstrumentExchangeType, str]] = ...) -> None: ...

class FilterOptionsRequest(_message.Message):
    __slots__ = ("basic_asset_uid", "basic_asset_position_uid")
    BASIC_ASSET_UID_FIELD_NUMBER: _ClassVar[int]
    BASIC_ASSET_POSITION_UID_FIELD_NUMBER: _ClassVar[int]
    basic_asset_uid: str
    basic_asset_position_uid: str
    def __init__(self, basic_asset_uid: _Optional[str] = ..., basic_asset_position_uid: _Optional[str] = ...) -> None: ...

class BondResponse(_message.Message):
    __slots__ = ("instrument",)
    INSTRUMENT_FIELD_NUMBER: _ClassVar[int]
    instrument: Bond
    def __init__(self, instrument: _Optional[_Union[Bond, _Mapping]] = ...) -> None: ...

class BondsResponse(_message.Message):
    __slots__ = ("instruments",)
    INSTRUMENTS_FIELD_NUMBER: _ClassVar[int]
    instruments: _containers.RepeatedCompositeFieldContainer[Bond]
    def __init__(self, instruments: _Optional[_Iterable[_Union[Bond, _Mapping]]] = ...) -> None: ...

class GetBondCouponsRequest(_message.Message):
    __slots__ = ("figi", "to", "instrument_id")
    FIGI_FIELD_NUMBER: _ClassVar[int]
    FROM_FIELD_NUMBER: _ClassVar[int]
    TO_FIELD_NUMBER: _ClassVar[int]
    INSTRUMENT_ID_FIELD_NUMBER: _ClassVar[int]
    figi: str
    to: _timestamp_pb2.Timestamp
    instrument_id: str
    def __init__(self, figi: _Optional[str] = ..., to: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., instrument_id: _Optional[str] = ..., **kwargs) -> None: ...

class GetBondCouponsResponse(_message.Message):
    __slots__ = ("events",)
    EVENTS_FIELD_NUMBER: _ClassVar[int]
    events: _containers.RepeatedCompositeFieldContainer[Coupon]
    def __init__(self, events: _Optional[_Iterable[_Union[Coupon, _Mapping]]] = ...) -> None: ...

class GetBondEventsRequest(_message.Message):
    __slots__ = ("to", "instrument_id", "type")
    class EventType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        EVENT_TYPE_UNSPECIFIED: _ClassVar[GetBondEventsRequest.EventType]
        EVENT_TYPE_CPN: _ClassVar[GetBondEventsRequest.EventType]
        EVENT_TYPE_CALL: _ClassVar[GetBondEventsRequest.EventType]
        EVENT_TYPE_MTY: _ClassVar[GetBondEventsRequest.EventType]
        EVENT_TYPE_CONV: _ClassVar[GetBondEventsRequest.EventType]
    EVENT_TYPE_UNSPECIFIED: GetBondEventsRequest.EventType
    EVENT_TYPE_CPN: GetBondEventsRequest.EventType
    EVENT_TYPE_CALL: GetBondEventsRequest.EventType
    EVENT_TYPE_MTY: GetBondEventsRequest.EventType
    EVENT_TYPE_CONV: GetBondEventsRequest.EventType
    FROM_FIELD_NUMBER: _ClassVar[int]
    TO_FIELD_NUMBER: _ClassVar[int]
    INSTRUMENT_ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    to: _timestamp_pb2.Timestamp
    instrument_id: str
    type: GetBondEventsRequest.EventType
    def __init__(self, to: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., instrument_id: _Optional[str] = ..., type: _Optional[_Union[GetBondEventsRequest.EventType, str]] = ..., **kwargs) -> None: ...

class GetBondEventsResponse(_message.Message):
    __slots__ = ("events",)
    class BondEvent(_message.Message):
        __slots__ = ("instrument_id", "event_number", "event_date", "event_type", "event_total_vol", "fix_date", "rate_date", "default_date", "real_pay_date", "pay_date", "pay_one_bond", "money_flow_val", "execution", "operation_type", "value", "note", "convert_to_fin_tool_id", "coupon_start_date", "coupon_end_date", "coupon_period", "coupon_interest_rate")
        INSTRUMENT_ID_FIELD_NUMBER: _ClassVar[int]
        EVENT_NUMBER_FIELD_NUMBER: _ClassVar[int]
        EVENT_DATE_FIELD_NUMBER: _ClassVar[int]
        EVENT_TYPE_FIELD_NUMBER: _ClassVar[int]
        EVENT_TOTAL_VOL_FIELD_NUMBER: _ClassVar[int]
        FIX_DATE_FIELD_NUMBER: _ClassVar[int]
        RATE_DATE_FIELD_NUMBER: _ClassVar[int]
        DEFAULT_DATE_FIELD_NUMBER: _ClassVar[int]
        REAL_PAY_DATE_FIELD_NUMBER: _ClassVar[int]
        PAY_DATE_FIELD_NUMBER: _ClassVar[int]
        PAY_ONE_BOND_FIELD_NUMBER: _ClassVar[int]
        MONEY_FLOW_VAL_FIELD_NUMBER: _ClassVar[int]
        EXECUTION_FIELD_NUMBER: _ClassVar[int]
        OPERATION_TYPE_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        NOTE_FIELD_NUMBER: _ClassVar[int]
        CONVERT_TO_FIN_TOOL_ID_FIELD_NUMBER: _ClassVar[int]
        COUPON_START_DATE_FIELD_NUMBER: _ClassVar[int]
        COUPON_END_DATE_FIELD_NUMBER: _ClassVar[int]
        COUPON_PERIOD_FIELD_NUMBER: _ClassVar[int]
        COUPON_INTEREST_RATE_FIELD_NUMBER: _ClassVar[int]
        instrument_id: str
        event_number: int
        event_date: _timestamp_pb2.Timestamp
        event_type: GetBondEventsRequest.EventType
        event_total_vol: _common_pb2.Quotation
        fix_date: _timestamp_pb2.Timestamp
        rate_date: _timestamp_pb2.Timestamp
        default_date: _timestamp_pb2.Timestamp
        real_pay_date: _timestamp_pb2.Timestamp
        pay_date: _timestamp_pb2.Timestamp
        pay_one_bond: _common_pb2.MoneyValue
        money_flow_val: _common_pb2.MoneyValue
        execution: str
        operation_type: str
        value: _common_pb2.Quotation
        note: str
        convert_to_fin_tool_id: str
        coupon_start_date: _timestamp_pb2.Timestamp
        coupon_end_date: _timestamp_pb2.Timestamp
        coupon_period: int
        coupon_interest_rate: _common_pb2.Quotation
        def __init__(self, instrument_id: _Optional[str] = ..., event_number: _Optional[int] = ..., event_date: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., event_type: _Optional[_Union[GetBondEventsRequest.EventType, str]] = ..., event_total_vol: _Optional[_Union[_common_pb2.Quotation, _Mapping]] = ..., fix_date: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., rate_date: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., default_date: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., real_pay_date: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., pay_date: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., pay_one_bond: _Optional[_Union[_common_pb2.MoneyValue, _Mapping]] = ..., money_flow_val: _Optional[_Union[_common_pb2.MoneyValue, _Mapping]] = ..., execution: _Optional[str] = ..., operation_type: _Optional[str] = ..., value: _Optional[_Union[_common_pb2.Quotation, _Mapping]] = ..., note: _Optional[str] = ..., convert_to_fin_tool_id: _Optional[str] = ..., coupon_start_date: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., coupon_end_date: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., coupon_period: _Optional[int] = ..., coupon_interest_rate: _Optional[_Union[_common_pb2.Quotation, _Mapping]] = ...) -> None: ...
    EVENTS_FIELD_NUMBER: _ClassVar[int]
    events: _containers.RepeatedCompositeFieldContainer[GetBondEventsResponse.BondEvent]
    def __init__(self, events: _Optional[_Iterable[_Union[GetBondEventsResponse.BondEvent, _Mapping]]] = ...) -> None: ...

class Coupon(_message.Message):
    __slots__ = ("figi", "coupon_date", "coupon_number", "fix_date", "pay_one_bond", "coupon_type", "coupon_start_date", "coupon_end_date", "coupon_period")
    FIGI_FIELD_NUMBER: _ClassVar[int]
    COUPON_DATE_FIELD_NUMBER: _ClassVar[int]
    COUPON_NUMBER_FIELD_NUMBER: _ClassVar[int]
    FIX_DATE_FIELD_NUMBER: _ClassVar[int]
    PAY_ONE_BOND_FIELD_NUMBER: _ClassVar[int]
    COUPON_TYPE_FIELD_NUMBER: _ClassVar[int]
    COUPON_START_DATE_FIELD_NUMBER: _ClassVar[int]
    COUPON_END_DATE_FIELD_NUMBER: _ClassVar[int]
    COUPON_PERIOD_FIELD_NUMBER: _ClassVar[int]
    figi: str
    coupon_date: _timestamp_pb2.Timestamp
    coupon_number: int
    fix_date: _timestamp_pb2.Timestamp
    pay_one_bond: _common_pb2.MoneyValue
    coupon_type: CouponType
    coupon_start_date: _timestamp_pb2.Timestamp
    coupon_end_date: _timestamp_pb2.Timestamp
    coupon_period: int
    def __init__(self, figi: _Optional[str] = ..., coupon_date: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., coupon_number: _Optional[int] = ..., fix_date: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., pay_one_bond: _Optional[_Union[_common_pb2.MoneyValue, _Mapping]] = ..., coupon_type: _Optional[_Union[CouponType, str]] = ..., coupon_start_date: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., coupon_end_date: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., coupon_period: _Optional[int] = ...) -> None: ...

class CurrencyResponse(_message.Message):
    __slots__ = ("instrument",)
    INSTRUMENT_FIELD_NUMBER: _ClassVar[int]
    instrument: Currency
    def __init__(self, instrument: _Optional[_Union[Currency, _Mapping]] = ...) -> None: ...

class CurrenciesResponse(_message.Message):
    __slots__ = ("instruments",)
    INSTRUMENTS_FIELD_NUMBER: _ClassVar[int]
    instruments: _containers.RepeatedCompositeFieldContainer[Currency]
    def __init__(self, instruments: _Optional[_Iterable[_Union[Currency, _Mapping]]] = ...) -> None: ...

class EtfResponse(_message.Message):
    __slots__ = ("instrument",)
    INSTRUMENT_FIELD_NUMBER: _ClassVar[int]
    instrument: Etf
    def __init__(self, instrument: _Optional[_Union[Etf, _Mapping]] = ...) -> None: ...

class EtfsResponse(_message.Message):
    __slots__ = ("instruments",)
    INSTRUMENTS_FIELD_NUMBER: _ClassVar[int]
    instruments: _containers.RepeatedCompositeFieldContainer[Etf]
    def __init__(self, instruments: _Optional[_Iterable[_Union[Etf, _Mapping]]] = ...) -> None: ...

class FutureResponse(_message.Message):
    __slots__ = ("instrument",)
    INSTRUMENT_FIELD_NUMBER: _ClassVar[int]
    instrument: Future
    def __init__(self, instrument: _Optional[_Union[Future, _Mapping]] = ...) -> None: ...

class FuturesResponse(_message.Message):
    __slots__ = ("instruments",)
    INSTRUMENTS_FIELD_NUMBER: _ClassVar[int]
    instruments: _containers.RepeatedCompositeFieldContainer[Future]
    def __init__(self, instruments: _Optional[_Iterable[_Union[Future, _Mapping]]] = ...) -> None: ...

class OptionResponse(_message.Message):
    __slots__ = ("instrument",)
    INSTRUMENT_FIELD_NUMBER: _ClassVar[int]
    instrument: Option
    def __init__(self, instrument: _Optional[_Union[Option, _Mapping]] = ...) -> None: ...

class OptionsResponse(_message.Message):
    __slots__ = ("instruments",)
    INSTRUMENTS_FIELD_NUMBER: _ClassVar[int]
    instruments: _containers.RepeatedCompositeFieldContainer[Option]
    def __init__(self, instruments: _Optional[_Iterable[_Union[Option, _Mapping]]] = ...) -> None: ...

class Option(_message.Message):
    __slots__ = ("uid", "position_uid", "ticker", "class_code", "basic_asset_position_uid", "trading_status", "real_exchange", "direction", "payment_type", "style", "settlement_type", "name", "currency", "settlement_currency", "asset_type", "basic_asset", "exchange", "country_of_risk", "country_of_risk_name", "sector", "brand", "lot", "basic_asset_size", "klong", "kshort", "dlong", "dshort", "dlong_min", "dshort_min", "min_price_increment", "strike_price", "expiration_date", "first_trade_date", "last_trade_date", "first_1min_candle_date", "first_1day_candle_date", "short_enabled_flag", "for_iis_flag", "otc_flag", "buy_available_flag", "sell_available_flag", "for_qual_investor_flag", "weekend_flag", "blocked_tca_flag", "api_trade_available_flag")
    UID_FIELD_NUMBER: _ClassVar[int]
    POSITION_UID_FIELD_NUMBER: _ClassVar[int]
    TICKER_FIELD_NUMBER: _ClassVar[int]
    CLASS_CODE_FIELD_NUMBER: _ClassVar[int]
    BASIC_ASSET_POSITION_UID_FIELD_NUMBER: _ClassVar[int]
    TRADING_STATUS_FIELD_NUMBER: _ClassVar[int]
    REAL_EXCHANGE_FIELD_NUMBER: _ClassVar[int]
    DIRECTION_FIELD_NUMBER: _ClassVar[int]
    PAYMENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    STYLE_FIELD_NUMBER: _ClassVar[int]
    SETTLEMENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_FIELD_NUMBER: _ClassVar[int]
    SETTLEMENT_CURRENCY_FIELD_NUMBER: _ClassVar[int]
    ASSET_TYPE_FIELD_NUMBER: _ClassVar[int]
    BASIC_ASSET_FIELD_NUMBER: _ClassVar[int]
    EXCHANGE_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_OF_RISK_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_OF_RISK_NAME_FIELD_NUMBER: _ClassVar[int]
    SECTOR_FIELD_NUMBER: _ClassVar[int]
    BRAND_FIELD_NUMBER: _ClassVar[int]
    LOT_FIELD_NUMBER: _ClassVar[int]
    BASIC_ASSET_SIZE_FIELD_NUMBER: _ClassVar[int]
    KLONG_FIELD_NUMBER: _ClassVar[int]
    KSHORT_FIELD_NUMBER: _ClassVar[int]
    DLONG_FIELD_NUMBER: _ClassVar[int]
    DSHORT_FIELD_NUMBER: _ClassVar[int]
    DLONG_MIN_FIELD_NUMBER: _ClassVar[int]
    DSHORT_MIN_FIELD_NUMBER: _ClassVar[int]
    MIN_PRICE_INCREMENT_FIELD_NUMBER: _ClassVar[int]
    STRIKE_PRICE_FIELD_NUMBER: _ClassVar[int]
    EXPIRATION_DATE_FIELD_NUMBER: _ClassVar[int]
    FIRST_TRADE_DATE_FIELD_NUMBER: _ClassVar[int]
    LAST_TRADE_DATE_FIELD_NUMBER: _ClassVar[int]
    FIRST_1MIN_CANDLE_DATE_FIELD_NUMBER: _ClassVar[int]
    FIRST_1DAY_CANDLE_DATE_FIELD_NUMBER: _ClassVar[int]
    SHORT_ENABLED_FLAG_FIELD_NUMBER: _ClassVar[int]
    FOR_IIS_FLAG_FIELD_NUMBER: _ClassVar[int]
    OTC_FLAG_FIELD_NUMBER: _ClassVar[int]
    BUY_AVAILABLE_FLAG_FIELD_NUMBER: _ClassVar[int]
    SELL_AVAILABLE_FLAG_FIELD_NUMBER: _ClassVar[int]
    FOR_QUAL_INVESTOR_FLAG_FIELD_NUMBER: _ClassVar[int]
    WEEKEND_FLAG_FIELD_NUMBER: _ClassVar[int]
    BLOCKED_TCA_FLAG_FIELD_NUMBER: _ClassVar[int]
    API_TRADE_AVAILABLE_FLAG_FIELD_NUMBER: _ClassVar[int]
    uid: str
    position_uid: str
    ticker: str
    class_code: str
    basic_asset_position_uid: str
    trading_status: _common_pb2.SecurityTradingStatus
    real_exchange: RealExchange
    direction: OptionDirection
    payment_type: OptionPaymentType
    style: OptionStyle
    settlement_type: OptionSettlementType
    name: str
    currency: str
    settlement_currency: str
    asset_type: str
    basic_asset: str
    exchange: str
    country_of_risk: str
    country_of_risk_name: str
    sector: str
    brand: _common_pb2.BrandData
    lot: int
    basic_asset_size: _common_pb2.Quotation
    klong: _common_pb2.Quotation
    kshort: _common_pb2.Quotation
    dlong: _common_pb2.Quotation
    dshort: _common_pb2.Quotation
    dlong_min: _common_pb2.Quotation
    dshort_min: _common_pb2.Quotation
    min_price_increment: _common_pb2.Quotation
    strike_price: _common_pb2.MoneyValue
    expiration_date: _timestamp_pb2.Timestamp
    first_trade_date: _timestamp_pb2.Timestamp
    last_trade_date: _timestamp_pb2.Timestamp
    first_1min_candle_date: _timestamp_pb2.Timestamp
    first_1day_candle_date: _timestamp_pb2.Timestamp
    short_enabled_flag: bool
    for_iis_flag: bool
    otc_flag: bool
    buy_available_flag: bool
    sell_available_flag: bool
    for_qual_investor_flag: bool
    weekend_flag: bool
    blocked_tca_flag: bool
    api_trade_available_flag: bool
    def __init__(self, uid: _Optional[str] = ..., position_uid: _Optional[str] = ..., ticker: _Optional[str] = ..., class_code: _Optional[str] = ..., basic_asset_position_uid: _Optional[str] = ..., trading_status: _Optional[_Union[_common_pb2.SecurityTradingStatus, str]] = ..., real_exchange: _Optional[_Union[RealExchange, str]] = ..., direction: _Optional[_Union[OptionDirection, str]] = ..., payment_type: _Optional[_Union[OptionPaymentType, str]] = ..., style: _Optional[_Union[OptionStyle, str]] = ..., settlement_type: _Optional[_Union[OptionSettlementType, str]] = ..., name: _Optional[str] = ..., currency: _Optional[str] = ..., settlement_currency: _Optional[str] = ..., asset_type: _Optional[str] = ..., basic_asset: _Optional[str] = ..., exchange: _Optional[str] = ..., country_of_risk: _Optional[str] = ..., country_of_risk_name: _Optional[str] = ..., sector: _Optional[str] = ..., brand: _Optional[_Union[_common_pb2.BrandData, _Mapping]] = ..., lot: _Optional[int] = ..., basic_asset_size: _Optional[_Union[_common_pb2.Quotation, _Mapping]] = ..., klong: _Optional[_Union[_common_pb2.Quotation, _Mapping]] = ..., kshort: _Optional[_Union[_common_pb2.Quotation, _Mapping]] = ..., dlong: _Optional[_Union[_common_pb2.Quotation, _Mapping]] = ..., dshort: _Optional[_Union[_common_pb2.Quotation, _Mapping]] = ..., dlong_min: _Optional[_Union[_common_pb2.Quotation, _Mapping]] = ..., dshort_min: _Optional[_Union[_common_pb2.Quotation, _Mapping]] = ..., min_price_increment: _Optional[_Union[_common_pb2.Quotation, _Mapping]] = ..., strike_price: _Optional[_Union[_common_pb2.MoneyValue, _Mapping]] = ..., expiration_date: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., first_trade_date: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., last_trade_date: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., first_1min_candle_date: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., first_1day_candle_date: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., short_enabled_flag: bool = ..., for_iis_flag: bool = ..., otc_flag: bool = ..., buy_available_flag: bool = ..., sell_available_flag: bool = ..., for_qual_investor_flag: bool = ..., weekend_flag: bool = ..., blocked_tca_flag: bool = ..., api_trade_available_flag: bool = ...) -> None: ...

class ShareResponse(_message.Message):
    __slots__ = ("instrument",)
    INSTRUMENT_FIELD_NUMBER: _ClassVar[int]
    instrument: Share
    def __init__(self, instrument: _Optional[_Union[Share, _Mapping]] = ...) -> None: ...

class SharesResponse(_message.Message):
    __slots__ = ("instruments",)
    INSTRUMENTS_FIELD_NUMBER: _ClassVar[int]
    instruments: _containers.RepeatedCompositeFieldContainer[Share]
    def __init__(self, instruments: _Optional[_Iterable[_Union[Share, _Mapping]]] = ...) -> None: ...

class Bond(_message.Message):
    __slots__ = ("figi", "ticker", "class_code", "isin", "lot", "currency", "klong", "kshort", "dlong", "dshort", "dlong_min", "dshort_min", "short_enabled_flag", "name", "exchange", "coupon_quantity_per_year", "maturity_date", "nominal", "initial_nominal", "state_reg_date", "placement_date", "placement_price", "aci_value", "country_of_risk", "country_of_risk_name", "sector", "issue_kind", "issue_size", "issue_size_plan", "trading_status", "otc_flag", "buy_available_flag", "sell_available_flag", "floating_coupon_flag", "perpetual_flag", "amortization_flag", "min_price_increment", "api_trade_available_flag", "uid", "real_exchange", "position_uid", "asset_uid", "for_iis_flag", "for_qual_investor_flag", "weekend_flag", "blocked_tca_flag", "subordinated_flag", "liquidity_flag", "first_1min_candle_date", "first_1day_candle_date", "risk_level", "brand", "bond_type")
    FIGI_FIELD_NUMBER: _ClassVar[int]
    TICKER_FIELD_NUMBER: _ClassVar[int]
    CLASS_CODE_FIELD_NUMBER: _ClassVar[int]
    ISIN_FIELD_NUMBER: _ClassVar[int]
    LOT_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_FIELD_NUMBER: _ClassVar[int]
    KLONG_FIELD_NUMBER: _ClassVar[int]
    KSHORT_FIELD_NUMBER: _ClassVar[int]
    DLONG_FIELD_NUMBER: _ClassVar[int]
    DSHORT_FIELD_NUMBER: _ClassVar[int]
    DLONG_MIN_FIELD_NUMBER: _ClassVar[int]
    DSHORT_MIN_FIELD_NUMBER: _ClassVar[int]
    SHORT_ENABLED_FLAG_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    EXCHANGE_FIELD_NUMBER: _ClassVar[int]
    COUPON_QUANTITY_PER_YEAR_FIELD_NUMBER: _ClassVar[int]
    MATURITY_DATE_FIELD_NUMBER: _ClassVar[int]
    NOMINAL_FIELD_NUMBER: _ClassVar[int]
    INITIAL_NOMINAL_FIELD_NUMBER: _ClassVar[int]
    STATE_REG_DATE_FIELD_NUMBER: _ClassVar[int]
    PLACEMENT_DATE_FIELD_NUMBER: _ClassVar[int]
    PLACEMENT_PRICE_FIELD_NUMBER: _ClassVar[int]
    ACI_VALUE_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_OF_RISK_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_OF_RISK_NAME_FIELD_NUMBER: _ClassVar[int]
    SECTOR_FIELD_NUMBER: _ClassVar[int]
    ISSUE_KIND_FIELD_NUMBER: _ClassVar[int]
    ISSUE_SIZE_FIELD_NUMBER: _ClassVar[int]
    ISSUE_SIZE_PLAN_FIELD_NUMBER: _ClassVar[int]
    TRADING_STATUS_FIELD_NUMBER: _ClassVar[int]
    OTC_FLAG_FIELD_NUMBER: _ClassVar[int]
    BUY_AVAILABLE_FLAG_FIELD_NUMBER: _ClassVar[int]
    SELL_AVAILABLE_FLAG_FIELD_NUMBER: _ClassVar[int]
    FLOATING_COUPON_FLAG_FIELD_NUMBER: _ClassVar[int]
    PERPETUAL_FLAG_FIELD_NUMBER: _ClassVar[int]
    AMORTIZATION_FLAG_FIELD_NUMBER: _ClassVar[int]
    MIN_PRICE_INCREMENT_FIELD_NUMBER: _ClassVar[int]
    API_TRADE_AVAILABLE_FLAG_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    REAL_EXCHANGE_FIELD_NUMBER: _ClassVar[int]
    POSITION_UID_FIELD_NUMBER: _ClassVar[int]
    ASSET_UID_FIELD_NUMBER: _ClassVar[int]
    FOR_IIS_FLAG_FIELD_NUMBER: _ClassVar[int]
    FOR_QUAL_INVESTOR_FLAG_FIELD_NUMBER: _ClassVar[int]
    WEEKEND_FLAG_FIELD_NUMBER: _ClassVar[int]
    BLOCKED_TCA_FLAG_FIELD_NUMBER: _ClassVar[int]
    SUBORDINATED_FLAG_FIELD_NUMBER: _ClassVar[int]
    LIQUIDITY_FLAG_FIELD_NUMBER: _ClassVar[int]
    FIRST_1MIN_CANDLE_DATE_FIELD_NUMBER: _ClassVar[int]
    FIRST_1DAY_CANDLE_DATE_FIELD_NUMBER: _ClassVar[int]
    RISK_LEVEL_FIELD_NUMBER: _ClassVar[int]
    BRAND_FIELD_NUMBER: _ClassVar[int]
    BOND_TYPE_FIELD_NUMBER: _ClassVar[int]
    figi: str
    ticker: str
    class_code: str
    isin: str
    lot: int
    currency: str
    klong: _common_pb2.Quotation
    kshort: _common_pb2.Quotation
    dlong: _common_pb2.Quotation
    dshort: _common_pb2.Quotation
    dlong_min: _common_pb2.Quotation
    dshort_min: _common_pb2.Quotation
    short_enabled_flag: bool
    name: str
    exchange: str
    coupon_quantity_per_year: int
    maturity_date: _timestamp_pb2.Timestamp
    nominal: _common_pb2.MoneyValue
    initial_nominal: _common_pb2.MoneyValue
    state_reg_date: _timestamp_pb2.Timestamp
    placement_date: _timestamp_pb2.Timestamp
    placement_price: _common_pb2.MoneyValue
    aci_value: _common_pb2.MoneyValue
    country_of_risk: str
    country_of_risk_name: str
    sector: str
    issue_kind: str
    issue_size: int
    issue_size_plan: int
    trading_status: _common_pb2.SecurityTradingStatus
    otc_flag: bool
    buy_available_flag: bool
    sell_available_flag: bool
    floating_coupon_flag: bool
    perpetual_flag: bool
    amortization_flag: bool
    min_price_increment: _common_pb2.Quotation
    api_trade_available_flag: bool
    uid: str
    real_exchange: RealExchange
    position_uid: str
    asset_uid: str
    for_iis_flag: bool
    for_qual_investor_flag: bool
    weekend_flag: bool
    blocked_tca_flag: bool
    subordinated_flag: bool
    liquidity_flag: bool
    first_1min_candle_date: _timestamp_pb2.Timestamp
    first_1day_candle_date: _timestamp_pb2.Timestamp
    risk_level: RiskLevel
    brand: _common_pb2.BrandData
    bond_type: BondType
    def __init__(self, figi: _Optional[str] = ..., ticker: _Optional[str] = ..., class_code: _Optional[str] = ..., isin: _Optional[str] = ..., lot: _Optional[int] = ..., currency: _Optional[str] = ..., klong: _Optional[_Union[_common_pb2.Quotation, _Mapping]] = ..., kshort: _Optional[_Union[_common_pb2.Quotation, _Mapping]] = ..., dlong: _Optional[_Union[_common_pb2.Quotation, _Mapping]] = ..., dshort: _Optional[_Union[_common_pb2.Quotation, _Mapping]] = ..., dlong_min: _Optional[_Union[_common_pb2.Quotation, _Mapping]] = ..., dshort_min: _Optional[_Union[_common_pb2.Quotation, _Mapping]] = ..., short_enabled_flag: bool = ..., name: _Optional[str] = ..., exchange: _Optional[str] = ..., coupon_quantity_per_year: _Optional[int] = ..., maturity_date: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., nominal: _Optional[_Union[_common_pb2.MoneyValue, _Mapping]] = ..., initial_nominal: _Optional[_Union[_common_pb2.MoneyValue, _Mapping]] = ..., state_reg_date: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., placement_date: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., placement_price: _Optional[_Union[_common_pb2.MoneyValue, _Mapping]] = ..., aci_value: _Optional[_Union[_common_pb2.MoneyValue, _Mapping]] = ..., country_of_risk: _Optional[str] = ..., country_of_risk_name: _Optional[str] = ..., sector: _Optional[str] = ..., issue_kind: _Optional[str] = ..., issue_size: _Optional[int] = ..., issue_size_plan: _Optional[int] = ..., trading_status: _Optional[_Union[_common_pb2.SecurityTradingStatus, str]] = ..., otc_flag: bool = ..., buy_available_flag: bool = ..., sell_available_flag: bool = ..., floating_coupon_flag: bool = ..., perpetual_flag: bool = ..., amortization_flag: bool = ..., min_price_increment: _Optional[_Union[_common_pb2.Quotation, _Mapping]] = ..., api_trade_available_flag: bool = ..., uid: _Optional[str] = ..., real_exchange: _Optional[_Union[RealExchange, str]] = ..., position_uid: _Optional[str] = ..., asset_uid: _Optional[str] = ..., for_iis_flag: bool = ..., for_qual_investor_flag: bool = ..., weekend_flag: bool = ..., blocked_tca_flag: bool = ..., subordinated_flag: bool = ..., liquidity_flag: bool = ..., first_1min_candle_date: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., first_1day_candle_date: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., risk_level: _Optional[_Union[RiskLevel, str]] = ..., brand: _Optional[_Union[_common_pb2.BrandData, _Mapping]] = ..., bond_type: _Optional[_Union[BondType, str]] = ...) -> None: ...

class Currency(_message.Message):
    __slots__ = ("figi", "ticker", "class_code", "isin", "lot", "currency", "klong", "kshort", "dlong", "dshort", "dlong_min", "dshort_min", "short_enabled_flag", "name", "exchange", "nominal", "country_of_risk", "country_of_risk_name", "trading_status", "otc_flag", "buy_available_flag", "sell_available_flag", "iso_currency_name", "min_price_increment", "api_trade_available_flag", "uid", "real_exchange", "position_uid", "for_iis_flag", "for_qual_investor_flag", "weekend_flag", "blocked_tca_flag", "first_1min_candle_date", "first_1day_candle_date", "brand")
    FIGI_FIELD_NUMBER: _ClassVar[int]
    TICKER_FIELD_NUMBER: _ClassVar[int]
    CLASS_CODE_FIELD_NUMBER: _ClassVar[int]
    ISIN_FIELD_NUMBER: _ClassVar[int]
    LOT_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_FIELD_NUMBER: _ClassVar[int]
    KLONG_FIELD_NUMBER: _ClassVar[int]
    KSHORT_FIELD_NUMBER: _ClassVar[int]
    DLONG_FIELD_NUMBER: _ClassVar[int]
    DSHORT_FIELD_NUMBER: _ClassVar[int]
    DLONG_MIN_FIELD_NUMBER: _ClassVar[int]
    DSHORT_MIN_FIELD_NUMBER: _ClassVar[int]
    SHORT_ENABLED_FLAG_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    EXCHANGE_FIELD_NUMBER: _ClassVar[int]
    NOMINAL_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_OF_RISK_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_OF_RISK_NAME_FIELD_NUMBER: _ClassVar[int]
    TRADING_STATUS_FIELD_NUMBER: _ClassVar[int]
    OTC_FLAG_FIELD_NUMBER: _ClassVar[int]
    BUY_AVAILABLE_FLAG_FIELD_NUMBER: _ClassVar[int]
    SELL_AVAILABLE_FLAG_FIELD_NUMBER: _ClassVar[int]
    ISO_CURRENCY_NAME_FIELD_NUMBER: _ClassVar[int]
    MIN_PRICE_INCREMENT_FIELD_NUMBER: _ClassVar[int]
    API_TRADE_AVAILABLE_FLAG_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    REAL_EXCHANGE_FIELD_NUMBER: _ClassVar[int]
    POSITION_UID_FIELD_NUMBER: _ClassVar[int]
    FOR_IIS_FLAG_FIELD_NUMBER: _ClassVar[int]
    FOR_QUAL_INVESTOR_FLAG_FIELD_NUMBER: _ClassVar[int]
    WEEKEND_FLAG_FIELD_NUMBER: _ClassVar[int]
    BLOCKED_TCA_FLAG_FIELD_NUMBER: _ClassVar[int]
    FIRST_1MIN_CANDLE_DATE_FIELD_NUMBER: _ClassVar[int]
    FIRST_1DAY_CANDLE_DATE_FIELD_NUMBER: _ClassVar[int]
    BRAND_FIELD_NUMBER: _ClassVar[int]
    figi: str
    ticker: str
    class_code: str
    isin: str
    lot: int
    currency: str
    klong: _common_pb2.Quotation
    kshort: _common_pb2.Quotation
    dlong: _common_pb2.Quotation
    dshort: _common_pb2.Quotation
    dlong_min: _common_pb2.Quotation
    dshort_min: _common_pb2.Quotation
    short_enabled_flag: bool
    name: str
    exchange: str
    nominal: _common_pb2.MoneyValue
    country_of_risk: str
    country_of_risk_name: str
    trading_status: _common_pb2.SecurityTradingStatus
    otc_flag: bool
    buy_available_flag: bool
    sell_available_flag: bool
    iso_currency_name: str
    min_price_increment: _common_pb2.Quotation
    api_trade_available_flag: bool
    uid: str
    real_exchange: RealExchange
    position_uid: str
    for_iis_flag: bool
    for_qual_investor_flag: bool
    weekend_flag: bool
    blocked_tca_flag: bool
    first_1min_candle_date: _timestamp_pb2.Timestamp
    first_1day_candle_date: _timestamp_pb2.Timestamp
    brand: _common_pb2.BrandData
    def __init__(self, figi: _Optional[str] = ..., ticker: _Optional[str] = ..., class_code: _Optional[str] = ..., isin: _Optional[str] = ..., lot: _Optional[int] = ..., currency: _Optional[str] = ..., klong: _Optional[_Union[_common_pb2.Quotation, _Mapping]] = ..., kshort: _Optional[_Union[_common_pb2.Quotation, _Mapping]] = ..., dlong: _Optional[_Union[_common_pb2.Quotation, _Mapping]] = ..., dshort: _Optional[_Union[_common_pb2.Quotation, _Mapping]] = ..., dlong_min: _Optional[_Union[_common_pb2.Quotation, _Mapping]] = ..., dshort_min: _Optional[_Union[_common_pb2.Quotation, _Mapping]] = ..., short_enabled_flag: bool = ..., name: _Optional[str] = ..., exchange: _Optional[str] = ..., nominal: _Optional[_Union[_common_pb2.MoneyValue, _Mapping]] = ..., country_of_risk: _Optional[str] = ..., country_of_risk_name: _Optional[str] = ..., trading_status: _Optional[_Union[_common_pb2.SecurityTradingStatus, str]] = ..., otc_flag: bool = ..., buy_available_flag: bool = ..., sell_available_flag: bool = ..., iso_currency_name: _Optional[str] = ..., min_price_increment: _Optional[_Union[_common_pb2.Quotation, _Mapping]] = ..., api_trade_available_flag: bool = ..., uid: _Optional[str] = ..., real_exchange: _Optional[_Union[RealExchange, str]] = ..., position_uid: _Optional[str] = ..., for_iis_flag: bool = ..., for_qual_investor_flag: bool = ..., weekend_flag: bool = ..., blocked_tca_flag: bool = ..., first_1min_candle_date: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., first_1day_candle_date: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., brand: _Optional[_Union[_common_pb2.BrandData, _Mapping]] = ...) -> None: ...

class Etf(_message.Message):
    __slots__ = ("figi", "ticker", "class_code", "isin", "lot", "currency", "klong", "kshort", "dlong", "dshort", "dlong_min", "dshort_min", "short_enabled_flag", "name", "exchange", "fixed_commission", "focus_type", "released_date", "num_shares", "country_of_risk", "country_of_risk_name", "sector", "rebalancing_freq", "trading_status", "otc_flag", "buy_available_flag", "sell_available_flag", "min_price_increment", "api_trade_available_flag", "uid", "real_exchange", "position_uid", "asset_uid", "instrument_exchange", "for_iis_flag", "for_qual_investor_flag", "weekend_flag", "blocked_tca_flag", "liquidity_flag", "first_1min_candle_date", "first_1day_candle_date", "brand")
    FIGI_FIELD_NUMBER: _ClassVar[int]
    TICKER_FIELD_NUMBER: _ClassVar[int]
    CLASS_CODE_FIELD_NUMBER: _ClassVar[int]
    ISIN_FIELD_NUMBER: _ClassVar[int]
    LOT_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_FIELD_NUMBER: _ClassVar[int]
    KLONG_FIELD_NUMBER: _ClassVar[int]
    KSHORT_FIELD_NUMBER: _ClassVar[int]
    DLONG_FIELD_NUMBER: _ClassVar[int]
    DSHORT_FIELD_NUMBER: _ClassVar[int]
    DLONG_MIN_FIELD_NUMBER: _ClassVar[int]
    DSHORT_MIN_FIELD_NUMBER: _ClassVar[int]
    SHORT_ENABLED_FLAG_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    EXCHANGE_FIELD_NUMBER: _ClassVar[int]
    FIXED_COMMISSION_FIELD_NUMBER: _ClassVar[int]
    FOCUS_TYPE_FIELD_NUMBER: _ClassVar[int]
    RELEASED_DATE_FIELD_NUMBER: _ClassVar[int]
    NUM_SHARES_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_OF_RISK_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_OF_RISK_NAME_FIELD_NUMBER: _ClassVar[int]
    SECTOR_FIELD_NUMBER: _ClassVar[int]
    REBALANCING_FREQ_FIELD_NUMBER: _ClassVar[int]
    TRADING_STATUS_FIELD_NUMBER: _ClassVar[int]
    OTC_FLAG_FIELD_NUMBER: _ClassVar[int]
    BUY_AVAILABLE_FLAG_FIELD_NUMBER: _ClassVar[int]
    SELL_AVAILABLE_FLAG_FIELD_NUMBER: _ClassVar[int]
    MIN_PRICE_INCREMENT_FIELD_NUMBER: _ClassVar[int]
    API_TRADE_AVAILABLE_FLAG_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    REAL_EXCHANGE_FIELD_NUMBER: _ClassVar[int]
    POSITION_UID_FIELD_NUMBER: _ClassVar[int]
    ASSET_UID_FIELD_NUMBER: _ClassVar[int]
    INSTRUMENT_EXCHANGE_FIELD_NUMBER: _ClassVar[int]
    FOR_IIS_FLAG_FIELD_NUMBER: _ClassVar[int]
    FOR_QUAL_INVESTOR_FLAG_FIELD_NUMBER: _ClassVar[int]
    WEEKEND_FLAG_FIELD_NUMBER: _ClassVar[int]
    BLOCKED_TCA_FLAG_FIELD_NUMBER: _ClassVar[int]
    LIQUIDITY_FLAG_FIELD_NUMBER: _ClassVar[int]
    FIRST_1MIN_CANDLE_DATE_FIELD_NUMBER: _ClassVar[int]
    FIRST_1DAY_CANDLE_DATE_FIELD_NUMBER: _ClassVar[int]
    BRAND_FIELD_NUMBER: _ClassVar[int]
    figi: str
    ticker: str
    class_code: str
    isin: str
    lot: int
    currency: str
    klong: _common_pb2.Quotation
    kshort: _common_pb2.Quotation
    dlong: _common_pb2.Quotation
    dshort: _common_pb2.Quotation
    dlong_min: _common_pb2.Quotation
    dshort_min: _common_pb2.Quotation
    short_enabled_flag: bool
    name: str
    exchange: str
    fixed_commission: _common_pb2.Quotation
    focus_type: str
    released_date: _timestamp_pb2.Timestamp
    num_shares: _common_pb2.Quotation
    country_of_risk: str
    country_of_risk_name: str
    sector: str
    rebalancing_freq: str
    trading_status: _common_pb2.SecurityTradingStatus
    otc_flag: bool
    buy_available_flag: bool
    sell_available_flag: bool
    min_price_increment: _common_pb2.Quotation
    api_trade_available_flag: bool
    uid: str
    real_exchange: RealExchange
    position_uid: str
    asset_uid: str
    instrument_exchange: InstrumentExchangeType
    for_iis_flag: bool
    for_qual_investor_flag: bool
    weekend_flag: bool
    blocked_tca_flag: bool
    liquidity_flag: bool
    first_1min_candle_date: _timestamp_pb2.Timestamp
    first_1day_candle_date: _timestamp_pb2.Timestamp
    brand: _common_pb2.BrandData
    def __init__(self, figi: _Optional[str] = ..., ticker: _Optional[str] = ..., class_code: _Optional[str] = ..., isin: _Optional[str] = ..., lot: _Optional[int] = ..., currency: _Optional[str] = ..., klong: _Optional[_Union[_common_pb2.Quotation, _Mapping]] = ..., kshort: _Optional[_Union[_common_pb2.Quotation, _Mapping]] = ..., dlong: _Optional[_Union[_common_pb2.Quotation, _Mapping]] = ..., dshort: _Optional[_Union[_common_pb2.Quotation, _Mapping]] = ..., dlong_min: _Optional[_Union[_common_pb2.Quotation, _Mapping]] = ..., dshort_min: _Optional[_Union[_common_pb2.Quotation, _Mapping]] = ..., short_enabled_flag: bool = ..., name: _Optional[str] = ..., exchange: _Optional[str] = ..., fixed_commission: _Optional[_Union[_common_pb2.Quotation, _Mapping]] = ..., focus_type: _Optional[str] = ..., released_date: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., num_shares: _Optional[_Union[_common_pb2.Quotation, _Mapping]] = ..., country_of_risk: _Optional[str] = ..., country_of_risk_name: _Optional[str] = ..., sector: _Optional[str] = ..., rebalancing_freq: _Optional[str] = ..., trading_status: _Optional[_Union[_common_pb2.SecurityTradingStatus, str]] = ..., otc_flag: bool = ..., buy_available_flag: bool = ..., sell_available_flag: bool = ..., min_price_increment: _Optional[_Union[_common_pb2.Quotation, _Mapping]] = ..., api_trade_available_flag: bool = ..., uid: _Optional[str] = ..., real_exchange: _Optional[_Union[RealExchange, str]] = ..., position_uid: _Optional[str] = ..., asset_uid: _Optional[str] = ..., instrument_exchange: _Optional[_Union[InstrumentExchangeType, str]] = ..., for_iis_flag: bool = ..., for_qual_investor_flag: bool = ..., weekend_flag: bool = ..., blocked_tca_flag: bool = ..., liquidity_flag: bool = ..., first_1min_candle_date: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., first_1day_candle_date: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., brand: _Optional[_Union[_common_pb2.BrandData, _Mapping]] = ...) -> None: ...

class Future(_message.Message):
    __slots__ = ("figi", "ticker", "class_code", "lot", "currency", "klong", "kshort", "dlong", "dshort", "dlong_min", "dshort_min", "short_enabled_flag", "name", "exchange", "first_trade_date", "last_trade_date", "futures_type", "asset_type", "basic_asset", "basic_asset_size", "country_of_risk", "country_of_risk_name", "sector", "expiration_date", "trading_status", "otc_flag", "buy_available_flag", "sell_available_flag", "min_price_increment", "api_trade_available_flag", "uid", "real_exchange", "position_uid", "basic_asset_position_uid", "for_iis_flag", "for_qual_investor_flag", "weekend_flag", "blocked_tca_flag", "first_1min_candle_date", "first_1day_candle_date", "initial_margin_on_buy", "initial_margin_on_sell", "min_price_increment_amount", "brand")
    FIGI_FIELD_NUMBER: _ClassVar[int]
    TICKER_FIELD_NUMBER: _ClassVar[int]
    CLASS_CODE_FIELD_NUMBER: _ClassVar[int]
    LOT_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_FIELD_NUMBER: _ClassVar[int]
    KLONG_FIELD_NUMBER: _ClassVar[int]
    KSHORT_FIELD_NUMBER: _ClassVar[int]
    DLONG_FIELD_NUMBER: _ClassVar[int]
    DSHORT_FIELD_NUMBER: _ClassVar[int]
    DLONG_MIN_FIELD_NUMBER: _ClassVar[int]
    DSHORT_MIN_FIELD_NUMBER: _ClassVar[int]
    SHORT_ENABLED_FLAG_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    EXCHANGE_FIELD_NUMBER: _ClassVar[int]
    FIRST_TRADE_DATE_FIELD_NUMBER: _ClassVar[int]
    LAST_TRADE_DATE_FIELD_NUMBER: _ClassVar[int]
    FUTURES_TYPE_FIELD_NUMBER: _ClassVar[int]
    ASSET_TYPE_FIELD_NUMBER: _ClassVar[int]
    BASIC_ASSET_FIELD_NUMBER: _ClassVar[int]
    BASIC_ASSET_SIZE_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_OF_RISK_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_OF_RISK_NAME_FIELD_NUMBER: _ClassVar[int]
    SECTOR_FIELD_NUMBER: _ClassVar[int]
    EXPIRATION_DATE_FIELD_NUMBER: _ClassVar[int]
    TRADING_STATUS_FIELD_NUMBER: _ClassVar[int]
    OTC_FLAG_FIELD_NUMBER: _ClassVar[int]
    BUY_AVAILABLE_FLAG_FIELD_NUMBER: _ClassVar[int]
    SELL_AVAILABLE_FLAG_FIELD_NUMBER: _ClassVar[int]
    MIN_PRICE_INCREMENT_FIELD_NUMBER: _ClassVar[int]
    API_TRADE_AVAILABLE_FLAG_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    REAL_EXCHANGE_FIELD_NUMBER: _ClassVar[int]
    POSITION_UID_FIELD_NUMBER: _ClassVar[int]
    BASIC_ASSET_POSITION_UID_FIELD_NUMBER: _ClassVar[int]
    FOR_IIS_FLAG_FIELD_NUMBER: _ClassVar[int]
    FOR_QUAL_INVESTOR_FLAG_FIELD_NUMBER: _ClassVar[int]
    WEEKEND_FLAG_FIELD_NUMBER: _ClassVar[int]
    BLOCKED_TCA_FLAG_FIELD_NUMBER: _ClassVar[int]
    FIRST_1MIN_CANDLE_DATE_FIELD_NUMBER: _ClassVar[int]
    FIRST_1DAY_CANDLE_DATE_FIELD_NUMBER: _ClassVar[int]
    INITIAL_MARGIN_ON_BUY_FIELD_NUMBER: _ClassVar[int]
    INITIAL_MARGIN_ON_SELL_FIELD_NUMBER: _ClassVar[int]
    MIN_PRICE_INCREMENT_AMOUNT_FIELD_NUMBER: _ClassVar[int]
    BRAND_FIELD_NUMBER: _ClassVar[int]
    figi: str
    ticker: str
    class_code: str
    lot: int
    currency: str
    klong: _common_pb2.Quotation
    kshort: _common_pb2.Quotation
    dlong: _common_pb2.Quotation
    dshort: _common_pb2.Quotation
    dlong_min: _common_pb2.Quotation
    dshort_min: _common_pb2.Quotation
    short_enabled_flag: bool
    name: str
    exchange: str
    first_trade_date: _timestamp_pb2.Timestamp
    last_trade_date: _timestamp_pb2.Timestamp
    futures_type: str
    asset_type: str
    basic_asset: str
    basic_asset_size: _common_pb2.Quotation
    country_of_risk: str
    country_of_risk_name: str
    sector: str
    expiration_date: _timestamp_pb2.Timestamp
    trading_status: _common_pb2.SecurityTradingStatus
    otc_flag: bool
    buy_available_flag: bool
    sell_available_flag: bool
    min_price_increment: _common_pb2.Quotation
    api_trade_available_flag: bool
    uid: str
    real_exchange: RealExchange
    position_uid: str
    basic_asset_position_uid: str
    for_iis_flag: bool
    for_qual_investor_flag: bool
    weekend_flag: bool
    blocked_tca_flag: bool
    first_1min_candle_date: _timestamp_pb2.Timestamp
    first_1day_candle_date: _timestamp_pb2.Timestamp
    initial_margin_on_buy: _common_pb2.MoneyValue
    initial_margin_on_sell: _common_pb2.MoneyValue
    min_price_increment_amount: _common_pb2.Quotation
    brand: _common_pb2.BrandData
    def __init__(self, figi: _Optional[str] = ..., ticker: _Optional[str] = ..., class_code: _Optional[str] = ..., lot: _Optional[int] = ..., currency: _Optional[str] = ..., klong: _Optional[_Union[_common_pb2.Quotation, _Mapping]] = ..., kshort: _Optional[_Union[_common_pb2.Quotation, _Mapping]] = ..., dlong: _Optional[_Union[_common_pb2.Quotation, _Mapping]] = ..., dshort: _Optional[_Union[_common_pb2.Quotation, _Mapping]] = ..., dlong_min: _Optional[_Union[_common_pb2.Quotation, _Mapping]] = ..., dshort_min: _Optional[_Union[_common_pb2.Quotation, _Mapping]] = ..., short_enabled_flag: bool = ..., name: _Optional[str] = ..., exchange: _Optional[str] = ..., first_trade_date: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., last_trade_date: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., futures_type: _Optional[str] = ..., asset_type: _Optional[str] = ..., basic_asset: _Optional[str] = ..., basic_asset_size: _Optional[_Union[_common_pb2.Quotation, _Mapping]] = ..., country_of_risk: _Optional[str] = ..., country_of_risk_name: _Optional[str] = ..., sector: _Optional[str] = ..., expiration_date: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., trading_status: _Optional[_Union[_common_pb2.SecurityTradingStatus, str]] = ..., otc_flag: bool = ..., buy_available_flag: bool = ..., sell_available_flag: bool = ..., min_price_increment: _Optional[_Union[_common_pb2.Quotation, _Mapping]] = ..., api_trade_available_flag: bool = ..., uid: _Optional[str] = ..., real_exchange: _Optional[_Union[RealExchange, str]] = ..., position_uid: _Optional[str] = ..., basic_asset_position_uid: _Optional[str] = ..., for_iis_flag: bool = ..., for_qual_investor_flag: bool = ..., weekend_flag: bool = ..., blocked_tca_flag: bool = ..., first_1min_candle_date: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., first_1day_candle_date: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., initial_margin_on_buy: _Optional[_Union[_common_pb2.MoneyValue, _Mapping]] = ..., initial_margin_on_sell: _Optional[_Union[_common_pb2.MoneyValue, _Mapping]] = ..., min_price_increment_amount: _Optional[_Union[_common_pb2.Quotation, _Mapping]] = ..., brand: _Optional[_Union[_common_pb2.BrandData, _Mapping]] = ...) -> None: ...

class Share(_message.Message):
    __slots__ = ("figi", "ticker", "class_code", "isin", "lot", "currency", "klong", "kshort", "dlong", "dshort", "dlong_min", "dshort_min", "short_enabled_flag", "name", "exchange", "ipo_date", "issue_size", "country_of_risk", "country_of_risk_name", "sector", "issue_size_plan", "nominal", "trading_status", "otc_flag", "buy_available_flag", "sell_available_flag", "div_yield_flag", "share_type", "min_price_increment", "api_trade_available_flag", "uid", "real_exchange", "position_uid", "asset_uid", "instrument_exchange", "for_iis_flag", "for_qual_investor_flag", "weekend_flag", "blocked_tca_flag", "liquidity_flag", "first_1min_candle_date", "first_1day_candle_date", "brand")
    FIGI_FIELD_NUMBER: _ClassVar[int]
    TICKER_FIELD_NUMBER: _ClassVar[int]
    CLASS_CODE_FIELD_NUMBER: _ClassVar[int]
    ISIN_FIELD_NUMBER: _ClassVar[int]
    LOT_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_FIELD_NUMBER: _ClassVar[int]
    KLONG_FIELD_NUMBER: _ClassVar[int]
    KSHORT_FIELD_NUMBER: _ClassVar[int]
    DLONG_FIELD_NUMBER: _ClassVar[int]
    DSHORT_FIELD_NUMBER: _ClassVar[int]
    DLONG_MIN_FIELD_NUMBER: _ClassVar[int]
    DSHORT_MIN_FIELD_NUMBER: _ClassVar[int]
    SHORT_ENABLED_FLAG_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    EXCHANGE_FIELD_NUMBER: _ClassVar[int]
    IPO_DATE_FIELD_NUMBER: _ClassVar[int]
    ISSUE_SIZE_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_OF_RISK_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_OF_RISK_NAME_FIELD_NUMBER: _ClassVar[int]
    SECTOR_FIELD_NUMBER: _ClassVar[int]
    ISSUE_SIZE_PLAN_FIELD_NUMBER: _ClassVar[int]
    NOMINAL_FIELD_NUMBER: _ClassVar[int]
    TRADING_STATUS_FIELD_NUMBER: _ClassVar[int]
    OTC_FLAG_FIELD_NUMBER: _ClassVar[int]
    BUY_AVAILABLE_FLAG_FIELD_NUMBER: _ClassVar[int]
    SELL_AVAILABLE_FLAG_FIELD_NUMBER: _ClassVar[int]
    DIV_YIELD_FLAG_FIELD_NUMBER: _ClassVar[int]
    SHARE_TYPE_FIELD_NUMBER: _ClassVar[int]
    MIN_PRICE_INCREMENT_FIELD_NUMBER: _ClassVar[int]
    API_TRADE_AVAILABLE_FLAG_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    REAL_EXCHANGE_FIELD_NUMBER: _ClassVar[int]
    POSITION_UID_FIELD_NUMBER: _ClassVar[int]
    ASSET_UID_FIELD_NUMBER: _ClassVar[int]
    INSTRUMENT_EXCHANGE_FIELD_NUMBER: _ClassVar[int]
    FOR_IIS_FLAG_FIELD_NUMBER: _ClassVar[int]
    FOR_QUAL_INVESTOR_FLAG_FIELD_NUMBER: _ClassVar[int]
    WEEKEND_FLAG_FIELD_NUMBER: _ClassVar[int]
    BLOCKED_TCA_FLAG_FIELD_NUMBER: _ClassVar[int]
    LIQUIDITY_FLAG_FIELD_NUMBER: _ClassVar[int]
    FIRST_1MIN_CANDLE_DATE_FIELD_NUMBER: _ClassVar[int]
    FIRST_1DAY_CANDLE_DATE_FIELD_NUMBER: _ClassVar[int]
    BRAND_FIELD_NUMBER: _ClassVar[int]
    figi: str
    ticker: str
    class_code: str
    isin: str
    lot: int
    currency: str
    klong: _common_pb2.Quotation
    kshort: _common_pb2.Quotation
    dlong: _common_pb2.Quotation
    dshort: _common_pb2.Quotation
    dlong_min: _common_pb2.Quotation
    dshort_min: _common_pb2.Quotation
    short_enabled_flag: bool
    name: str
    exchange: str
    ipo_date: _timestamp_pb2.Timestamp
    issue_size: int
    country_of_risk: str
    country_of_risk_name: str
    sector: str
    issue_size_plan: int
    nominal: _common_pb2.MoneyValue
    trading_status: _common_pb2.SecurityTradingStatus
    otc_flag: bool
    buy_available_flag: bool
    sell_available_flag: bool
    div_yield_flag: bool
    share_type: ShareType
    min_price_increment: _common_pb2.Quotation
    api_trade_available_flag: bool
    uid: str
    real_exchange: RealExchange
    position_uid: str
    asset_uid: str
    instrument_exchange: InstrumentExchangeType
    for_iis_flag: bool
    for_qual_investor_flag: bool
    weekend_flag: bool
    blocked_tca_flag: bool
    liquidity_flag: bool
    first_1min_candle_date: _timestamp_pb2.Timestamp
    first_1day_candle_date: _timestamp_pb2.Timestamp
    brand: _common_pb2.BrandData
    def __init__(self, figi: _Optional[str] = ..., ticker: _Optional[str] = ..., class_code: _Optional[str] = ..., isin: _Optional[str] = ..., lot: _Optional[int] = ..., currency: _Optional[str] = ..., klong: _Optional[_Union[_common_pb2.Quotation, _Mapping]] = ..., kshort: _Optional[_Union[_common_pb2.Quotation, _Mapping]] = ..., dlong: _Optional[_Union[_common_pb2.Quotation, _Mapping]] = ..., dshort: _Optional[_Union[_common_pb2.Quotation, _Mapping]] = ..., dlong_min: _Optional[_Union[_common_pb2.Quotation, _Mapping]] = ..., dshort_min: _Optional[_Union[_common_pb2.Quotation, _Mapping]] = ..., short_enabled_flag: bool = ..., name: _Optional[str] = ..., exchange: _Optional[str] = ..., ipo_date: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., issue_size: _Optional[int] = ..., country_of_risk: _Optional[str] = ..., country_of_risk_name: _Optional[str] = ..., sector: _Optional[str] = ..., issue_size_plan: _Optional[int] = ..., nominal: _Optional[_Union[_common_pb2.MoneyValue, _Mapping]] = ..., trading_status: _Optional[_Union[_common_pb2.SecurityTradingStatus, str]] = ..., otc_flag: bool = ..., buy_available_flag: bool = ..., sell_available_flag: bool = ..., div_yield_flag: bool = ..., share_type: _Optional[_Union[ShareType, str]] = ..., min_price_increment: _Optional[_Union[_common_pb2.Quotation, _Mapping]] = ..., api_trade_available_flag: bool = ..., uid: _Optional[str] = ..., real_exchange: _Optional[_Union[RealExchange, str]] = ..., position_uid: _Optional[str] = ..., asset_uid: _Optional[str] = ..., instrument_exchange: _Optional[_Union[InstrumentExchangeType, str]] = ..., for_iis_flag: bool = ..., for_qual_investor_flag: bool = ..., weekend_flag: bool = ..., blocked_tca_flag: bool = ..., liquidity_flag: bool = ..., first_1min_candle_date: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., first_1day_candle_date: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., brand: _Optional[_Union[_common_pb2.BrandData, _Mapping]] = ...) -> None: ...

class GetAccruedInterestsRequest(_message.Message):
    __slots__ = ("figi", "to", "instrument_id")
    FIGI_FIELD_NUMBER: _ClassVar[int]
    FROM_FIELD_NUMBER: _ClassVar[int]
    TO_FIELD_NUMBER: _ClassVar[int]
    INSTRUMENT_ID_FIELD_NUMBER: _ClassVar[int]
    figi: str
    to: _timestamp_pb2.Timestamp
    instrument_id: str
    def __init__(self, figi: _Optional[str] = ..., to: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., instrument_id: _Optional[str] = ..., **kwargs) -> None: ...

class GetAccruedInterestsResponse(_message.Message):
    __slots__ = ("accrued_interests",)
    ACCRUED_INTERESTS_FIELD_NUMBER: _ClassVar[int]
    accrued_interests: _containers.RepeatedCompositeFieldContainer[AccruedInterest]
    def __init__(self, accrued_interests: _Optional[_Iterable[_Union[AccruedInterest, _Mapping]]] = ...) -> None: ...

class AccruedInterest(_message.Message):
    __slots__ = ("date", "value", "value_percent", "nominal")
    DATE_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    VALUE_PERCENT_FIELD_NUMBER: _ClassVar[int]
    NOMINAL_FIELD_NUMBER: _ClassVar[int]
    date: _timestamp_pb2.Timestamp
    value: _common_pb2.Quotation
    value_percent: _common_pb2.Quotation
    nominal: _common_pb2.Quotation
    def __init__(self, date: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., value: _Optional[_Union[_common_pb2.Quotation, _Mapping]] = ..., value_percent: _Optional[_Union[_common_pb2.Quotation, _Mapping]] = ..., nominal: _Optional[_Union[_common_pb2.Quotation, _Mapping]] = ...) -> None: ...

class GetFuturesMarginRequest(_message.Message):
    __slots__ = ("figi", "instrument_id")
    FIGI_FIELD_NUMBER: _ClassVar[int]
    INSTRUMENT_ID_FIELD_NUMBER: _ClassVar[int]
    figi: str
    instrument_id: str
    def __init__(self, figi: _Optional[str] = ..., instrument_id: _Optional[str] = ...) -> None: ...

class GetFuturesMarginResponse(_message.Message):
    __slots__ = ("initial_margin_on_buy", "initial_margin_on_sell", "min_price_increment", "min_price_increment_amount")
    INITIAL_MARGIN_ON_BUY_FIELD_NUMBER: _ClassVar[int]
    INITIAL_MARGIN_ON_SELL_FIELD_NUMBER: _ClassVar[int]
    MIN_PRICE_INCREMENT_FIELD_NUMBER: _ClassVar[int]
    MIN_PRICE_INCREMENT_AMOUNT_FIELD_NUMBER: _ClassVar[int]
    initial_margin_on_buy: _common_pb2.MoneyValue
    initial_margin_on_sell: _common_pb2.MoneyValue
    min_price_increment: _common_pb2.Quotation
    min_price_increment_amount: _common_pb2.Quotation
    def __init__(self, initial_margin_on_buy: _Optional[_Union[_common_pb2.MoneyValue, _Mapping]] = ..., initial_margin_on_sell: _Optional[_Union[_common_pb2.MoneyValue, _Mapping]] = ..., min_price_increment: _Optional[_Union[_common_pb2.Quotation, _Mapping]] = ..., min_price_increment_amount: _Optional[_Union[_common_pb2.Quotation, _Mapping]] = ...) -> None: ...

class InstrumentResponse(_message.Message):
    __slots__ = ("instrument",)
    INSTRUMENT_FIELD_NUMBER: _ClassVar[int]
    instrument: Instrument
    def __init__(self, instrument: _Optional[_Union[Instrument, _Mapping]] = ...) -> None: ...

class Instrument(_message.Message):
    __slots__ = ("figi", "ticker", "class_code", "isin", "lot", "currency", "klong", "kshort", "dlong", "dshort", "dlong_min", "dshort_min", "short_enabled_flag", "name", "exchange", "country_of_risk", "country_of_risk_name", "instrument_type", "trading_status", "otc_flag", "buy_available_flag", "sell_available_flag", "min_price_increment", "api_trade_available_flag", "uid", "real_exchange", "position_uid", "asset_uid", "for_iis_flag", "for_qual_investor_flag", "weekend_flag", "blocked_tca_flag", "instrument_kind", "first_1min_candle_date", "first_1day_candle_date", "brand")
    FIGI_FIELD_NUMBER: _ClassVar[int]
    TICKER_FIELD_NUMBER: _ClassVar[int]
    CLASS_CODE_FIELD_NUMBER: _ClassVar[int]
    ISIN_FIELD_NUMBER: _ClassVar[int]
    LOT_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_FIELD_NUMBER: _ClassVar[int]
    KLONG_FIELD_NUMBER: _ClassVar[int]
    KSHORT_FIELD_NUMBER: _ClassVar[int]
    DLONG_FIELD_NUMBER: _ClassVar[int]
    DSHORT_FIELD_NUMBER: _ClassVar[int]
    DLONG_MIN_FIELD_NUMBER: _ClassVar[int]
    DSHORT_MIN_FIELD_NUMBER: _ClassVar[int]
    SHORT_ENABLED_FLAG_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    EXCHANGE_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_OF_RISK_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_OF_RISK_NAME_FIELD_NUMBER: _ClassVar[int]
    INSTRUMENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    TRADING_STATUS_FIELD_NUMBER: _ClassVar[int]
    OTC_FLAG_FIELD_NUMBER: _ClassVar[int]
    BUY_AVAILABLE_FLAG_FIELD_NUMBER: _ClassVar[int]
    SELL_AVAILABLE_FLAG_FIELD_NUMBER: _ClassVar[int]
    MIN_PRICE_INCREMENT_FIELD_NUMBER: _ClassVar[int]
    API_TRADE_AVAILABLE_FLAG_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    REAL_EXCHANGE_FIELD_NUMBER: _ClassVar[int]
    POSITION_UID_FIELD_NUMBER: _ClassVar[int]
    ASSET_UID_FIELD_NUMBER: _ClassVar[int]
    FOR_IIS_FLAG_FIELD_NUMBER: _ClassVar[int]
    FOR_QUAL_INVESTOR_FLAG_FIELD_NUMBER: _ClassVar[int]
    WEEKEND_FLAG_FIELD_NUMBER: _ClassVar[int]
    BLOCKED_TCA_FLAG_FIELD_NUMBER: _ClassVar[int]
    INSTRUMENT_KIND_FIELD_NUMBER: _ClassVar[int]
    FIRST_1MIN_CANDLE_DATE_FIELD_NUMBER: _ClassVar[int]
    FIRST_1DAY_CANDLE_DATE_FIELD_NUMBER: _ClassVar[int]
    BRAND_FIELD_NUMBER: _ClassVar[int]
    figi: str
    ticker: str
    class_code: str
    isin: str
    lot: int
    currency: str
    klong: _common_pb2.Quotation
    kshort: _common_pb2.Quotation
    dlong: _common_pb2.Quotation
    dshort: _common_pb2.Quotation
    dlong_min: _common_pb2.Quotation
    dshort_min: _common_pb2.Quotation
    short_enabled_flag: bool
    name: str
    exchange: str
    country_of_risk: str
    country_of_risk_name: str
    instrument_type: str
    trading_status: _common_pb2.SecurityTradingStatus
    otc_flag: bool
    buy_available_flag: bool
    sell_available_flag: bool
    min_price_increment: _common_pb2.Quotation
    api_trade_available_flag: bool
    uid: str
    real_exchange: RealExchange
    position_uid: str
    asset_uid: str
    for_iis_flag: bool
    for_qual_investor_flag: bool
    weekend_flag: bool
    blocked_tca_flag: bool
    instrument_kind: _common_pb2.InstrumentType
    first_1min_candle_date: _timestamp_pb2.Timestamp
    first_1day_candle_date: _timestamp_pb2.Timestamp
    brand: _common_pb2.BrandData
    def __init__(self, figi: _Optional[str] = ..., ticker: _Optional[str] = ..., class_code: _Optional[str] = ..., isin: _Optional[str] = ..., lot: _Optional[int] = ..., currency: _Optional[str] = ..., klong: _Optional[_Union[_common_pb2.Quotation, _Mapping]] = ..., kshort: _Optional[_Union[_common_pb2.Quotation, _Mapping]] = ..., dlong: _Optional[_Union[_common_pb2.Quotation, _Mapping]] = ..., dshort: _Optional[_Union[_common_pb2.Quotation, _Mapping]] = ..., dlong_min: _Optional[_Union[_common_pb2.Quotation, _Mapping]] = ..., dshort_min: _Optional[_Union[_common_pb2.Quotation, _Mapping]] = ..., short_enabled_flag: bool = ..., name: _Optional[str] = ..., exchange: _Optional[str] = ..., country_of_risk: _Optional[str] = ..., country_of_risk_name: _Optional[str] = ..., instrument_type: _Optional[str] = ..., trading_status: _Optional[_Union[_common_pb2.SecurityTradingStatus, str]] = ..., otc_flag: bool = ..., buy_available_flag: bool = ..., sell_available_flag: bool = ..., min_price_increment: _Optional[_Union[_common_pb2.Quotation, _Mapping]] = ..., api_trade_available_flag: bool = ..., uid: _Optional[str] = ..., real_exchange: _Optional[_Union[RealExchange, str]] = ..., position_uid: _Optional[str] = ..., asset_uid: _Optional[str] = ..., for_iis_flag: bool = ..., for_qual_investor_flag: bool = ..., weekend_flag: bool = ..., blocked_tca_flag: bool = ..., instrument_kind: _Optional[_Union[_common_pb2.InstrumentType, str]] = ..., first_1min_candle_date: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., first_1day_candle_date: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., brand: _Optional[_Union[_common_pb2.BrandData, _Mapping]] = ...) -> None: ...

class GetDividendsRequest(_message.Message):
    __slots__ = ("figi", "to", "instrument_id")
    FIGI_FIELD_NUMBER: _ClassVar[int]
    FROM_FIELD_NUMBER: _ClassVar[int]
    TO_FIELD_NUMBER: _ClassVar[int]
    INSTRUMENT_ID_FIELD_NUMBER: _ClassVar[int]
    figi: str
    to: _timestamp_pb2.Timestamp
    instrument_id: str
    def __init__(self, figi: _Optional[str] = ..., to: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., instrument_id: _Optional[str] = ..., **kwargs) -> None: ...

class GetDividendsResponse(_message.Message):
    __slots__ = ("dividends",)
    DIVIDENDS_FIELD_NUMBER: _ClassVar[int]
    dividends: _containers.RepeatedCompositeFieldContainer[Dividend]
    def __init__(self, dividends: _Optional[_Iterable[_Union[Dividend, _Mapping]]] = ...) -> None: ...

class Dividend(_message.Message):
    __slots__ = ("dividend_net", "payment_date", "declared_date", "last_buy_date", "dividend_type", "record_date", "regularity", "close_price", "yield_value", "created_at")
    DIVIDEND_NET_FIELD_NUMBER: _ClassVar[int]
    PAYMENT_DATE_FIELD_NUMBER: _ClassVar[int]
    DECLARED_DATE_FIELD_NUMBER: _ClassVar[int]
    LAST_BUY_DATE_FIELD_NUMBER: _ClassVar[int]
    DIVIDEND_TYPE_FIELD_NUMBER: _ClassVar[int]
    RECORD_DATE_FIELD_NUMBER: _ClassVar[int]
    REGULARITY_FIELD_NUMBER: _ClassVar[int]
    CLOSE_PRICE_FIELD_NUMBER: _ClassVar[int]
    YIELD_VALUE_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    dividend_net: _common_pb2.MoneyValue
    payment_date: _timestamp_pb2.Timestamp
    declared_date: _timestamp_pb2.Timestamp
    last_buy_date: _timestamp_pb2.Timestamp
    dividend_type: str
    record_date: _timestamp_pb2.Timestamp
    regularity: str
    close_price: _common_pb2.MoneyValue
    yield_value: _common_pb2.Quotation
    created_at: _timestamp_pb2.Timestamp
    def __init__(self, dividend_net: _Optional[_Union[_common_pb2.MoneyValue, _Mapping]] = ..., payment_date: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., declared_date: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., last_buy_date: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., dividend_type: _Optional[str] = ..., record_date: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., regularity: _Optional[str] = ..., close_price: _Optional[_Union[_common_pb2.MoneyValue, _Mapping]] = ..., yield_value: _Optional[_Union[_common_pb2.Quotation, _Mapping]] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class AssetRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class AssetResponse(_message.Message):
    __slots__ = ("asset",)
    ASSET_FIELD_NUMBER: _ClassVar[int]
    asset: AssetFull
    def __init__(self, asset: _Optional[_Union[AssetFull, _Mapping]] = ...) -> None: ...

class AssetsRequest(_message.Message):
    __slots__ = ("instrument_type",)
    INSTRUMENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    instrument_type: _common_pb2.InstrumentType
    def __init__(self, instrument_type: _Optional[_Union[_common_pb2.InstrumentType, str]] = ...) -> None: ...

class AssetsResponse(_message.Message):
    __slots__ = ("assets",)
    ASSETS_FIELD_NUMBER: _ClassVar[int]
    assets: _containers.RepeatedCompositeFieldContainer[Asset]
    def __init__(self, assets: _Optional[_Iterable[_Union[Asset, _Mapping]]] = ...) -> None: ...

class AssetFull(_message.Message):
    __slots__ = ("uid", "type", "name", "name_brief", "description", "deleted_at", "required_tests", "currency", "security", "gos_reg_code", "cfi", "code_nsd", "status", "brand", "updated_at", "br_code", "br_code_name", "instruments")
    UID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    NAME_BRIEF_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    DELETED_AT_FIELD_NUMBER: _ClassVar[int]
    REQUIRED_TESTS_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_FIELD_NUMBER: _ClassVar[int]
    SECURITY_FIELD_NUMBER: _ClassVar[int]
    GOS_REG_CODE_FIELD_NUMBER: _ClassVar[int]
    CFI_FIELD_NUMBER: _ClassVar[int]
    CODE_NSD_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    BRAND_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    BR_CODE_FIELD_NUMBER: _ClassVar[int]
    BR_CODE_NAME_FIELD_NUMBER: _ClassVar[int]
    INSTRUMENTS_FIELD_NUMBER: _ClassVar[int]
    uid: str
    type: AssetType
    name: str
    name_brief: str
    description: str
    deleted_at: _timestamp_pb2.Timestamp
    required_tests: _containers.RepeatedScalarFieldContainer[str]
    currency: AssetCurrency
    security: AssetSecurity
    gos_reg_code: str
    cfi: str
    code_nsd: str
    status: str
    brand: Brand
    updated_at: _timestamp_pb2.Timestamp
    br_code: str
    br_code_name: str
    instruments: _containers.RepeatedCompositeFieldContainer[AssetInstrument]
    def __init__(self, uid: _Optional[str] = ..., type: _Optional[_Union[AssetType, str]] = ..., name: _Optional[str] = ..., name_brief: _Optional[str] = ..., description: _Optional[str] = ..., deleted_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., required_tests: _Optional[_Iterable[str]] = ..., currency: _Optional[_Union[AssetCurrency, _Mapping]] = ..., security: _Optional[_Union[AssetSecurity, _Mapping]] = ..., gos_reg_code: _Optional[str] = ..., cfi: _Optional[str] = ..., code_nsd: _Optional[str] = ..., status: _Optional[str] = ..., brand: _Optional[_Union[Brand, _Mapping]] = ..., updated_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., br_code: _Optional[str] = ..., br_code_name: _Optional[str] = ..., instruments: _Optional[_Iterable[_Union[AssetInstrument, _Mapping]]] = ...) -> None: ...

class Asset(_message.Message):
    __slots__ = ("uid", "type", "name", "instruments")
    UID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    INSTRUMENTS_FIELD_NUMBER: _ClassVar[int]
    uid: str
    type: AssetType
    name: str
    instruments: _containers.RepeatedCompositeFieldContainer[AssetInstrument]
    def __init__(self, uid: _Optional[str] = ..., type: _Optional[_Union[AssetType, str]] = ..., name: _Optional[str] = ..., instruments: _Optional[_Iterable[_Union[AssetInstrument, _Mapping]]] = ...) -> None: ...

class AssetCurrency(_message.Message):
    __slots__ = ("base_currency",)
    BASE_CURRENCY_FIELD_NUMBER: _ClassVar[int]
    base_currency: str
    def __init__(self, base_currency: _Optional[str] = ...) -> None: ...

class AssetSecurity(_message.Message):
    __slots__ = ("isin", "type", "instrument_kind", "share", "bond", "sp", "etf", "clearing_certificate")
    ISIN_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    INSTRUMENT_KIND_FIELD_NUMBER: _ClassVar[int]
    SHARE_FIELD_NUMBER: _ClassVar[int]
    BOND_FIELD_NUMBER: _ClassVar[int]
    SP_FIELD_NUMBER: _ClassVar[int]
    ETF_FIELD_NUMBER: _ClassVar[int]
    CLEARING_CERTIFICATE_FIELD_NUMBER: _ClassVar[int]
    isin: str
    type: str
    instrument_kind: _common_pb2.InstrumentType
    share: AssetShare
    bond: AssetBond
    sp: AssetStructuredProduct
    etf: AssetEtf
    clearing_certificate: AssetClearingCertificate
    def __init__(self, isin: _Optional[str] = ..., type: _Optional[str] = ..., instrument_kind: _Optional[_Union[_common_pb2.InstrumentType, str]] = ..., share: _Optional[_Union[AssetShare, _Mapping]] = ..., bond: _Optional[_Union[AssetBond, _Mapping]] = ..., sp: _Optional[_Union[AssetStructuredProduct, _Mapping]] = ..., etf: _Optional[_Union[AssetEtf, _Mapping]] = ..., clearing_certificate: _Optional[_Union[AssetClearingCertificate, _Mapping]] = ...) -> None: ...

class AssetShare(_message.Message):
    __slots__ = ("type", "issue_size", "nominal", "nominal_currency", "primary_index", "dividend_rate", "preferred_share_type", "ipo_date", "registry_date", "div_yield_flag", "issue_kind", "placement_date", "repres_isin", "issue_size_plan", "total_float")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ISSUE_SIZE_FIELD_NUMBER: _ClassVar[int]
    NOMINAL_FIELD_NUMBER: _ClassVar[int]
    NOMINAL_CURRENCY_FIELD_NUMBER: _ClassVar[int]
    PRIMARY_INDEX_FIELD_NUMBER: _ClassVar[int]
    DIVIDEND_RATE_FIELD_NUMBER: _ClassVar[int]
    PREFERRED_SHARE_TYPE_FIELD_NUMBER: _ClassVar[int]
    IPO_DATE_FIELD_NUMBER: _ClassVar[int]
    REGISTRY_DATE_FIELD_NUMBER: _ClassVar[int]
    DIV_YIELD_FLAG_FIELD_NUMBER: _ClassVar[int]
    ISSUE_KIND_FIELD_NUMBER: _ClassVar[int]
    PLACEMENT_DATE_FIELD_NUMBER: _ClassVar[int]
    REPRES_ISIN_FIELD_NUMBER: _ClassVar[int]
    ISSUE_SIZE_PLAN_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FLOAT_FIELD_NUMBER: _ClassVar[int]
    type: ShareType
    issue_size: _common_pb2.Quotation
    nominal: _common_pb2.Quotation
    nominal_currency: str
    primary_index: str
    dividend_rate: _common_pb2.Quotation
    preferred_share_type: str
    ipo_date: _timestamp_pb2.Timestamp
    registry_date: _timestamp_pb2.Timestamp
    div_yield_flag: bool
    issue_kind: str
    placement_date: _timestamp_pb2.Timestamp
    repres_isin: str
    issue_size_plan: _common_pb2.Quotation
    total_float: _common_pb2.Quotation
    def __init__(self, type: _Optional[_Union[ShareType, str]] = ..., issue_size: _Optional[_Union[_common_pb2.Quotation, _Mapping]] = ..., nominal: _Optional[_Union[_common_pb2.Quotation, _Mapping]] = ..., nominal_currency: _Optional[str] = ..., primary_index: _Optional[str] = ..., dividend_rate: _Optional[_Union[_common_pb2.Quotation, _Mapping]] = ..., preferred_share_type: _Optional[str] = ..., ipo_date: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., registry_date: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., div_yield_flag: bool = ..., issue_kind: _Optional[str] = ..., placement_date: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., repres_isin: _Optional[str] = ..., issue_size_plan: _Optional[_Union[_common_pb2.Quotation, _Mapping]] = ..., total_float: _Optional[_Union[_common_pb2.Quotation, _Mapping]] = ...) -> None: ...

class AssetBond(_message.Message):
    __slots__ = ("current_nominal", "borrow_name", "issue_size", "nominal", "nominal_currency", "issue_kind", "interest_kind", "coupon_quantity_per_year", "indexed_nominal_flag", "subordinated_flag", "collateral_flag", "tax_free_flag", "amortization_flag", "floating_coupon_flag", "perpetual_flag", "maturity_date", "return_condition", "state_reg_date", "placement_date", "placement_price", "issue_size_plan")
    CURRENT_NOMINAL_FIELD_NUMBER: _ClassVar[int]
    BORROW_NAME_FIELD_NUMBER: _ClassVar[int]
    ISSUE_SIZE_FIELD_NUMBER: _ClassVar[int]
    NOMINAL_FIELD_NUMBER: _ClassVar[int]
    NOMINAL_CURRENCY_FIELD_NUMBER: _ClassVar[int]
    ISSUE_KIND_FIELD_NUMBER: _ClassVar[int]
    INTEREST_KIND_FIELD_NUMBER: _ClassVar[int]
    COUPON_QUANTITY_PER_YEAR_FIELD_NUMBER: _ClassVar[int]
    INDEXED_NOMINAL_FLAG_FIELD_NUMBER: _ClassVar[int]
    SUBORDINATED_FLAG_FIELD_NUMBER: _ClassVar[int]
    COLLATERAL_FLAG_FIELD_NUMBER: _ClassVar[int]
    TAX_FREE_FLAG_FIELD_NUMBER: _ClassVar[int]
    AMORTIZATION_FLAG_FIELD_NUMBER: _ClassVar[int]
    FLOATING_COUPON_FLAG_FIELD_NUMBER: _ClassVar[int]
    PERPETUAL_FLAG_FIELD_NUMBER: _ClassVar[int]
    MATURITY_DATE_FIELD_NUMBER: _ClassVar[int]
    RETURN_CONDITION_FIELD_NUMBER: _ClassVar[int]
    STATE_REG_DATE_FIELD_NUMBER: _ClassVar[int]
    PLACEMENT_DATE_FIELD_NUMBER: _ClassVar[int]
    PLACEMENT_PRICE_FIELD_NUMBER: _ClassVar[int]
    ISSUE_SIZE_PLAN_FIELD_NUMBER: _ClassVar[int]
    current_nominal: _common_pb2.Quotation
    borrow_name: str
    issue_size: _common_pb2.Quotation
    nominal: _common_pb2.Quotation
    nominal_currency: str
    issue_kind: str
    interest_kind: str
    coupon_quantity_per_year: int
    indexed_nominal_flag: bool
    subordinated_flag: bool
    collateral_flag: bool
    tax_free_flag: bool
    amortization_flag: bool
    floating_coupon_flag: bool
    perpetual_flag: bool
    maturity_date: _timestamp_pb2.Timestamp
    return_condition: str
    state_reg_date: _timestamp_pb2.Timestamp
    placement_date: _timestamp_pb2.Timestamp
    placement_price: _common_pb2.Quotation
    issue_size_plan: _common_pb2.Quotation
    def __init__(self, current_nominal: _Optional[_Union[_common_pb2.Quotation, _Mapping]] = ..., borrow_name: _Optional[str] = ..., issue_size: _Optional[_Union[_common_pb2.Quotation, _Mapping]] = ..., nominal: _Optional[_Union[_common_pb2.Quotation, _Mapping]] = ..., nominal_currency: _Optional[str] = ..., issue_kind: _Optional[str] = ..., interest_kind: _Optional[str] = ..., coupon_quantity_per_year: _Optional[int] = ..., indexed_nominal_flag: bool = ..., subordinated_flag: bool = ..., collateral_flag: bool = ..., tax_free_flag: bool = ..., amortization_flag: bool = ..., floating_coupon_flag: bool = ..., perpetual_flag: bool = ..., maturity_date: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., return_condition: _Optional[str] = ..., state_reg_date: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., placement_date: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., placement_price: _Optional[_Union[_common_pb2.Quotation, _Mapping]] = ..., issue_size_plan: _Optional[_Union[_common_pb2.Quotation, _Mapping]] = ...) -> None: ...

class AssetStructuredProduct(_message.Message):
    __slots__ = ("borrow_name", "nominal", "nominal_currency", "type", "logic_portfolio", "asset_type", "basic_asset", "safety_barrier", "maturity_date", "issue_size_plan", "issue_size", "placement_date", "issue_kind")
    BORROW_NAME_FIELD_NUMBER: _ClassVar[int]
    NOMINAL_FIELD_NUMBER: _ClassVar[int]
    NOMINAL_CURRENCY_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    LOGIC_PORTFOLIO_FIELD_NUMBER: _ClassVar[int]
    ASSET_TYPE_FIELD_NUMBER: _ClassVar[int]
    BASIC_ASSET_FIELD_NUMBER: _ClassVar[int]
    SAFETY_BARRIER_FIELD_NUMBER: _ClassVar[int]
    MATURITY_DATE_FIELD_NUMBER: _ClassVar[int]
    ISSUE_SIZE_PLAN_FIELD_NUMBER: _ClassVar[int]
    ISSUE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PLACEMENT_DATE_FIELD_NUMBER: _ClassVar[int]
    ISSUE_KIND_FIELD_NUMBER: _ClassVar[int]
    borrow_name: str
    nominal: _common_pb2.Quotation
    nominal_currency: str
    type: StructuredProductType
    logic_portfolio: str
    asset_type: AssetType
    basic_asset: str
    safety_barrier: _common_pb2.Quotation
    maturity_date: _timestamp_pb2.Timestamp
    issue_size_plan: _common_pb2.Quotation
    issue_size: _common_pb2.Quotation
    placement_date: _timestamp_pb2.Timestamp
    issue_kind: str
    def __init__(self, borrow_name: _Optional[str] = ..., nominal: _Optional[_Union[_common_pb2.Quotation, _Mapping]] = ..., nominal_currency: _Optional[str] = ..., type: _Optional[_Union[StructuredProductType, str]] = ..., logic_portfolio: _Optional[str] = ..., asset_type: _Optional[_Union[AssetType, str]] = ..., basic_asset: _Optional[str] = ..., safety_barrier: _Optional[_Union[_common_pb2.Quotation, _Mapping]] = ..., maturity_date: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., issue_size_plan: _Optional[_Union[_common_pb2.Quotation, _Mapping]] = ..., issue_size: _Optional[_Union[_common_pb2.Quotation, _Mapping]] = ..., placement_date: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., issue_kind: _Optional[str] = ...) -> None: ...

class AssetEtf(_message.Message):
    __slots__ = ("total_expense", "hurdle_rate", "performance_fee", "fixed_commission", "payment_type", "watermark_flag", "buy_premium", "sell_discount", "rebalancing_flag", "rebalancing_freq", "management_type", "primary_index", "focus_type", "leveraged_flag", "num_share", "ucits_flag", "released_date", "description", "primary_index_description", "primary_index_company", "index_recovery_period", "inav_code", "div_yield_flag", "expense_commission", "primary_index_tracking_error", "rebalancing_plan", "tax_rate", "rebalancing_dates", "issue_kind", "nominal", "nominal_currency")
    TOTAL_EXPENSE_FIELD_NUMBER: _ClassVar[int]
    HURDLE_RATE_FIELD_NUMBER: _ClassVar[int]
    PERFORMANCE_FEE_FIELD_NUMBER: _ClassVar[int]
    FIXED_COMMISSION_FIELD_NUMBER: _ClassVar[int]
    PAYMENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    WATERMARK_FLAG_FIELD_NUMBER: _ClassVar[int]
    BUY_PREMIUM_FIELD_NUMBER: _ClassVar[int]
    SELL_DISCOUNT_FIELD_NUMBER: _ClassVar[int]
    REBALANCING_FLAG_FIELD_NUMBER: _ClassVar[int]
    REBALANCING_FREQ_FIELD_NUMBER: _ClassVar[int]
    MANAGEMENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    PRIMARY_INDEX_FIELD_NUMBER: _ClassVar[int]
    FOCUS_TYPE_FIELD_NUMBER: _ClassVar[int]
    LEVERAGED_FLAG_FIELD_NUMBER: _ClassVar[int]
    NUM_SHARE_FIELD_NUMBER: _ClassVar[int]
    UCITS_FLAG_FIELD_NUMBER: _ClassVar[int]
    RELEASED_DATE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    PRIMARY_INDEX_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    PRIMARY_INDEX_COMPANY_FIELD_NUMBER: _ClassVar[int]
    INDEX_RECOVERY_PERIOD_FIELD_NUMBER: _ClassVar[int]
    INAV_CODE_FIELD_NUMBER: _ClassVar[int]
    DIV_YIELD_FLAG_FIELD_NUMBER: _ClassVar[int]
    EXPENSE_COMMISSION_FIELD_NUMBER: _ClassVar[int]
    PRIMARY_INDEX_TRACKING_ERROR_FIELD_NUMBER: _ClassVar[int]
    REBALANCING_PLAN_FIELD_NUMBER: _ClassVar[int]
    TAX_RATE_FIELD_NUMBER: _ClassVar[int]
    REBALANCING_DATES_FIELD_NUMBER: _ClassVar[int]
    ISSUE_KIND_FIELD_NUMBER: _ClassVar[int]
    NOMINAL_FIELD_NUMBER: _ClassVar[int]
    NOMINAL_CURRENCY_FIELD_NUMBER: _ClassVar[int]
    total_expense: _common_pb2.Quotation
    hurdle_rate: _common_pb2.Quotation
    performance_fee: _common_pb2.Quotation
    fixed_commission: _common_pb2.Quotation
    payment_type: str
    watermark_flag: bool
    buy_premium: _common_pb2.Quotation
    sell_discount: _common_pb2.Quotation
    rebalancing_flag: bool
    rebalancing_freq: str
    management_type: str
    primary_index: str
    focus_type: str
    leveraged_flag: bool
    num_share: _common_pb2.Quotation
    ucits_flag: bool
    released_date: _timestamp_pb2.Timestamp
    description: str
    primary_index_description: str
    primary_index_company: str
    index_recovery_period: _common_pb2.Quotation
    inav_code: str
    div_yield_flag: bool
    expense_commission: _common_pb2.Quotation
    primary_index_tracking_error: _common_pb2.Quotation
    rebalancing_plan: str
    tax_rate: str
    rebalancing_dates: _containers.RepeatedCompositeFieldContainer[_timestamp_pb2.Timestamp]
    issue_kind: str
    nominal: _common_pb2.Quotation
    nominal_currency: str
    def __init__(self, total_expense: _Optional[_Union[_common_pb2.Quotation, _Mapping]] = ..., hurdle_rate: _Optional[_Union[_common_pb2.Quotation, _Mapping]] = ..., performance_fee: _Optional[_Union[_common_pb2.Quotation, _Mapping]] = ..., fixed_commission: _Optional[_Union[_common_pb2.Quotation, _Mapping]] = ..., payment_type: _Optional[str] = ..., watermark_flag: bool = ..., buy_premium: _Optional[_Union[_common_pb2.Quotation, _Mapping]] = ..., sell_discount: _Optional[_Union[_common_pb2.Quotation, _Mapping]] = ..., rebalancing_flag: bool = ..., rebalancing_freq: _Optional[str] = ..., management_type: _Optional[str] = ..., primary_index: _Optional[str] = ..., focus_type: _Optional[str] = ..., leveraged_flag: bool = ..., num_share: _Optional[_Union[_common_pb2.Quotation, _Mapping]] = ..., ucits_flag: bool = ..., released_date: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., description: _Optional[str] = ..., primary_index_description: _Optional[str] = ..., primary_index_company: _Optional[str] = ..., index_recovery_period: _Optional[_Union[_common_pb2.Quotation, _Mapping]] = ..., inav_code: _Optional[str] = ..., div_yield_flag: bool = ..., expense_commission: _Optional[_Union[_common_pb2.Quotation, _Mapping]] = ..., primary_index_tracking_error: _Optional[_Union[_common_pb2.Quotation, _Mapping]] = ..., rebalancing_plan: _Optional[str] = ..., tax_rate: _Optional[str] = ..., rebalancing_dates: _Optional[_Iterable[_Union[_timestamp_pb2.Timestamp, _Mapping]]] = ..., issue_kind: _Optional[str] = ..., nominal: _Optional[_Union[_common_pb2.Quotation, _Mapping]] = ..., nominal_currency: _Optional[str] = ...) -> None: ...

class AssetClearingCertificate(_message.Message):
    __slots__ = ("nominal", "nominal_currency")
    NOMINAL_FIELD_NUMBER: _ClassVar[int]
    NOMINAL_CURRENCY_FIELD_NUMBER: _ClassVar[int]
    nominal: _common_pb2.Quotation
    nominal_currency: str
    def __init__(self, nominal: _Optional[_Union[_common_pb2.Quotation, _Mapping]] = ..., nominal_currency: _Optional[str] = ...) -> None: ...

class Brand(_message.Message):
    __slots__ = ("uid", "name", "description", "info", "company", "sector", "country_of_risk", "country_of_risk_name")
    UID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    INFO_FIELD_NUMBER: _ClassVar[int]
    COMPANY_FIELD_NUMBER: _ClassVar[int]
    SECTOR_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_OF_RISK_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_OF_RISK_NAME_FIELD_NUMBER: _ClassVar[int]
    uid: str
    name: str
    description: str
    info: str
    company: str
    sector: str
    country_of_risk: str
    country_of_risk_name: str
    def __init__(self, uid: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., info: _Optional[str] = ..., company: _Optional[str] = ..., sector: _Optional[str] = ..., country_of_risk: _Optional[str] = ..., country_of_risk_name: _Optional[str] = ...) -> None: ...

class AssetInstrument(_message.Message):
    __slots__ = ("uid", "figi", "instrument_type", "ticker", "class_code", "links", "instrument_kind", "position_uid")
    UID_FIELD_NUMBER: _ClassVar[int]
    FIGI_FIELD_NUMBER: _ClassVar[int]
    INSTRUMENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    TICKER_FIELD_NUMBER: _ClassVar[int]
    CLASS_CODE_FIELD_NUMBER: _ClassVar[int]
    LINKS_FIELD_NUMBER: _ClassVar[int]
    INSTRUMENT_KIND_FIELD_NUMBER: _ClassVar[int]
    POSITION_UID_FIELD_NUMBER: _ClassVar[int]
    uid: str
    figi: str
    instrument_type: str
    ticker: str
    class_code: str
    links: _containers.RepeatedCompositeFieldContainer[InstrumentLink]
    instrument_kind: _common_pb2.InstrumentType
    position_uid: str
    def __init__(self, uid: _Optional[str] = ..., figi: _Optional[str] = ..., instrument_type: _Optional[str] = ..., ticker: _Optional[str] = ..., class_code: _Optional[str] = ..., links: _Optional[_Iterable[_Union[InstrumentLink, _Mapping]]] = ..., instrument_kind: _Optional[_Union[_common_pb2.InstrumentType, str]] = ..., position_uid: _Optional[str] = ...) -> None: ...

class InstrumentLink(_message.Message):
    __slots__ = ("type", "instrument_uid")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    INSTRUMENT_UID_FIELD_NUMBER: _ClassVar[int]
    type: str
    instrument_uid: str
    def __init__(self, type: _Optional[str] = ..., instrument_uid: _Optional[str] = ...) -> None: ...

class GetFavoritesRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetFavoritesResponse(_message.Message):
    __slots__ = ("favorite_instruments",)
    FAVORITE_INSTRUMENTS_FIELD_NUMBER: _ClassVar[int]
    favorite_instruments: _containers.RepeatedCompositeFieldContainer[FavoriteInstrument]
    def __init__(self, favorite_instruments: _Optional[_Iterable[_Union[FavoriteInstrument, _Mapping]]] = ...) -> None: ...

class FavoriteInstrument(_message.Message):
    __slots__ = ("figi", "ticker", "class_code", "isin", "instrument_type", "name", "uid", "otc_flag", "api_trade_available_flag", "instrument_kind")
    FIGI_FIELD_NUMBER: _ClassVar[int]
    TICKER_FIELD_NUMBER: _ClassVar[int]
    CLASS_CODE_FIELD_NUMBER: _ClassVar[int]
    ISIN_FIELD_NUMBER: _ClassVar[int]
    INSTRUMENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    OTC_FLAG_FIELD_NUMBER: _ClassVar[int]
    API_TRADE_AVAILABLE_FLAG_FIELD_NUMBER: _ClassVar[int]
    INSTRUMENT_KIND_FIELD_NUMBER: _ClassVar[int]
    figi: str
    ticker: str
    class_code: str
    isin: str
    instrument_type: str
    name: str
    uid: str
    otc_flag: bool
    api_trade_available_flag: bool
    instrument_kind: _common_pb2.InstrumentType
    def __init__(self, figi: _Optional[str] = ..., ticker: _Optional[str] = ..., class_code: _Optional[str] = ..., isin: _Optional[str] = ..., instrument_type: _Optional[str] = ..., name: _Optional[str] = ..., uid: _Optional[str] = ..., otc_flag: bool = ..., api_trade_available_flag: bool = ..., instrument_kind: _Optional[_Union[_common_pb2.InstrumentType, str]] = ...) -> None: ...

class EditFavoritesRequest(_message.Message):
    __slots__ = ("instruments", "action_type")
    INSTRUMENTS_FIELD_NUMBER: _ClassVar[int]
    ACTION_TYPE_FIELD_NUMBER: _ClassVar[int]
    instruments: _containers.RepeatedCompositeFieldContainer[EditFavoritesRequestInstrument]
    action_type: EditFavoritesActionType
    def __init__(self, instruments: _Optional[_Iterable[_Union[EditFavoritesRequestInstrument, _Mapping]]] = ..., action_type: _Optional[_Union[EditFavoritesActionType, str]] = ...) -> None: ...

class EditFavoritesRequestInstrument(_message.Message):
    __slots__ = ("figi", "instrument_id")
    FIGI_FIELD_NUMBER: _ClassVar[int]
    INSTRUMENT_ID_FIELD_NUMBER: _ClassVar[int]
    figi: str
    instrument_id: str
    def __init__(self, figi: _Optional[str] = ..., instrument_id: _Optional[str] = ...) -> None: ...

class EditFavoritesResponse(_message.Message):
    __slots__ = ("favorite_instruments",)
    FAVORITE_INSTRUMENTS_FIELD_NUMBER: _ClassVar[int]
    favorite_instruments: _containers.RepeatedCompositeFieldContainer[FavoriteInstrument]
    def __init__(self, favorite_instruments: _Optional[_Iterable[_Union[FavoriteInstrument, _Mapping]]] = ...) -> None: ...

class GetCountriesRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetCountriesResponse(_message.Message):
    __slots__ = ("countries",)
    COUNTRIES_FIELD_NUMBER: _ClassVar[int]
    countries: _containers.RepeatedCompositeFieldContainer[CountryResponse]
    def __init__(self, countries: _Optional[_Iterable[_Union[CountryResponse, _Mapping]]] = ...) -> None: ...

class IndicativesRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class IndicativesResponse(_message.Message):
    __slots__ = ("instruments",)
    INSTRUMENTS_FIELD_NUMBER: _ClassVar[int]
    instruments: _containers.RepeatedCompositeFieldContainer[IndicativeResponse]
    def __init__(self, instruments: _Optional[_Iterable[_Union[IndicativeResponse, _Mapping]]] = ...) -> None: ...

class IndicativeResponse(_message.Message):
    __slots__ = ("figi", "ticker", "class_code", "currency", "instrument_kind", "name", "exchange", "uid", "buy_available_flag", "sell_available_flag")
    FIGI_FIELD_NUMBER: _ClassVar[int]
    TICKER_FIELD_NUMBER: _ClassVar[int]
    CLASS_CODE_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_FIELD_NUMBER: _ClassVar[int]
    INSTRUMENT_KIND_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    EXCHANGE_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    BUY_AVAILABLE_FLAG_FIELD_NUMBER: _ClassVar[int]
    SELL_AVAILABLE_FLAG_FIELD_NUMBER: _ClassVar[int]
    figi: str
    ticker: str
    class_code: str
    currency: str
    instrument_kind: _common_pb2.InstrumentType
    name: str
    exchange: str
    uid: str
    buy_available_flag: bool
    sell_available_flag: bool
    def __init__(self, figi: _Optional[str] = ..., ticker: _Optional[str] = ..., class_code: _Optional[str] = ..., currency: _Optional[str] = ..., instrument_kind: _Optional[_Union[_common_pb2.InstrumentType, str]] = ..., name: _Optional[str] = ..., exchange: _Optional[str] = ..., uid: _Optional[str] = ..., buy_available_flag: bool = ..., sell_available_flag: bool = ...) -> None: ...

class CountryResponse(_message.Message):
    __slots__ = ("alfa_two", "alfa_three", "name", "name_brief")
    ALFA_TWO_FIELD_NUMBER: _ClassVar[int]
    ALFA_THREE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    NAME_BRIEF_FIELD_NUMBER: _ClassVar[int]
    alfa_two: str
    alfa_three: str
    name: str
    name_brief: str
    def __init__(self, alfa_two: _Optional[str] = ..., alfa_three: _Optional[str] = ..., name: _Optional[str] = ..., name_brief: _Optional[str] = ...) -> None: ...

class FindInstrumentRequest(_message.Message):
    __slots__ = ("query", "instrument_kind", "api_trade_available_flag")
    QUERY_FIELD_NUMBER: _ClassVar[int]
    INSTRUMENT_KIND_FIELD_NUMBER: _ClassVar[int]
    API_TRADE_AVAILABLE_FLAG_FIELD_NUMBER: _ClassVar[int]
    query: str
    instrument_kind: _common_pb2.InstrumentType
    api_trade_available_flag: bool
    def __init__(self, query: _Optional[str] = ..., instrument_kind: _Optional[_Union[_common_pb2.InstrumentType, str]] = ..., api_trade_available_flag: bool = ...) -> None: ...

class FindInstrumentResponse(_message.Message):
    __slots__ = ("instruments",)
    INSTRUMENTS_FIELD_NUMBER: _ClassVar[int]
    instruments: _containers.RepeatedCompositeFieldContainer[InstrumentShort]
    def __init__(self, instruments: _Optional[_Iterable[_Union[InstrumentShort, _Mapping]]] = ...) -> None: ...

class InstrumentShort(_message.Message):
    __slots__ = ("isin", "figi", "ticker", "class_code", "instrument_type", "name", "uid", "position_uid", "instrument_kind", "api_trade_available_flag", "for_iis_flag", "first_1min_candle_date", "first_1day_candle_date", "for_qual_investor_flag", "weekend_flag", "blocked_tca_flag")
    ISIN_FIELD_NUMBER: _ClassVar[int]
    FIGI_FIELD_NUMBER: _ClassVar[int]
    TICKER_FIELD_NUMBER: _ClassVar[int]
    CLASS_CODE_FIELD_NUMBER: _ClassVar[int]
    INSTRUMENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    POSITION_UID_FIELD_NUMBER: _ClassVar[int]
    INSTRUMENT_KIND_FIELD_NUMBER: _ClassVar[int]
    API_TRADE_AVAILABLE_FLAG_FIELD_NUMBER: _ClassVar[int]
    FOR_IIS_FLAG_FIELD_NUMBER: _ClassVar[int]
    FIRST_1MIN_CANDLE_DATE_FIELD_NUMBER: _ClassVar[int]
    FIRST_1DAY_CANDLE_DATE_FIELD_NUMBER: _ClassVar[int]
    FOR_QUAL_INVESTOR_FLAG_FIELD_NUMBER: _ClassVar[int]
    WEEKEND_FLAG_FIELD_NUMBER: _ClassVar[int]
    BLOCKED_TCA_FLAG_FIELD_NUMBER: _ClassVar[int]
    isin: str
    figi: str
    ticker: str
    class_code: str
    instrument_type: str
    name: str
    uid: str
    position_uid: str
    instrument_kind: _common_pb2.InstrumentType
    api_trade_available_flag: bool
    for_iis_flag: bool
    first_1min_candle_date: _timestamp_pb2.Timestamp
    first_1day_candle_date: _timestamp_pb2.Timestamp
    for_qual_investor_flag: bool
    weekend_flag: bool
    blocked_tca_flag: bool
    def __init__(self, isin: _Optional[str] = ..., figi: _Optional[str] = ..., ticker: _Optional[str] = ..., class_code: _Optional[str] = ..., instrument_type: _Optional[str] = ..., name: _Optional[str] = ..., uid: _Optional[str] = ..., position_uid: _Optional[str] = ..., instrument_kind: _Optional[_Union[_common_pb2.InstrumentType, str]] = ..., api_trade_available_flag: bool = ..., for_iis_flag: bool = ..., first_1min_candle_date: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., first_1day_candle_date: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., for_qual_investor_flag: bool = ..., weekend_flag: bool = ..., blocked_tca_flag: bool = ...) -> None: ...

class GetBrandsRequest(_message.Message):
    __slots__ = ("paging",)
    PAGING_FIELD_NUMBER: _ClassVar[int]
    paging: _common_pb2.Page
    def __init__(self, paging: _Optional[_Union[_common_pb2.Page, _Mapping]] = ...) -> None: ...

class GetBrandRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class GetBrandsResponse(_message.Message):
    __slots__ = ("brands", "paging")
    BRANDS_FIELD_NUMBER: _ClassVar[int]
    PAGING_FIELD_NUMBER: _ClassVar[int]
    brands: _containers.RepeatedCompositeFieldContainer[Brand]
    paging: _common_pb2.PageResponse
    def __init__(self, brands: _Optional[_Iterable[_Union[Brand, _Mapping]]] = ..., paging: _Optional[_Union[_common_pb2.PageResponse, _Mapping]] = ...) -> None: ...

class GetAssetFundamentalsRequest(_message.Message):
    __slots__ = ("assets",)
    ASSETS_FIELD_NUMBER: _ClassVar[int]
    assets: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, assets: _Optional[_Iterable[str]] = ...) -> None: ...

class GetAssetFundamentalsResponse(_message.Message):
    __slots__ = ("fundamentals",)
    class StatisticResponse(_message.Message):
        __slots__ = ("asset_uid", "currency", "market_capitalization", "high_price_last_52_weeks", "low_price_last_52_weeks", "average_daily_volume_last_10_days", "average_daily_volume_last_4_weeks", "beta", "free_float", "forward_annual_dividend_yield", "shares_outstanding", "revenue_ttm", "ebitda_ttm", "net_income_ttm", "eps_ttm", "diluted_eps_ttm", "free_cash_flow_ttm", "five_year_annual_revenue_growth_rate", "three_year_annual_revenue_growth_rate", "pe_ratio_ttm", "price_to_sales_ttm", "price_to_book_ttm", "price_to_free_cash_flow_ttm", "total_enterprise_value_mrq", "ev_to_ebitda_mrq", "net_margin_mrq", "net_interest_margin_mrq", "roe", "roa", "roic", "total_debt_mrq", "total_debt_to_equity_mrq", "total_debt_to_ebitda_mrq", "free_cash_flow_to_price", "net_debt_to_ebitda", "current_ratio_mrq", "fixed_charge_coverage_ratio_fy", "dividend_yield_daily_ttm", "dividend_rate_ttm", "dividends_per_share", "five_years_average_dividend_yield", "five_year_annual_dividend_growth_rate", "dividend_payout_ratio_fy", "buy_back_ttm", "one_year_annual_revenue_growth_rate", "domicile_indicator_code", "adr_to_common_share_ratio", "number_of_employees", "ex_dividend_date", "fiscal_period_start_date", "fiscal_period_end_date", "revenue_change_five_years", "eps_change_five_years", "ebitda_change_five_years", "total_debt_change_five_years", "ev_to_sales")
        ASSET_UID_FIELD_NUMBER: _ClassVar[int]
        CURRENCY_FIELD_NUMBER: _ClassVar[int]
        MARKET_CAPITALIZATION_FIELD_NUMBER: _ClassVar[int]
        HIGH_PRICE_LAST_52_WEEKS_FIELD_NUMBER: _ClassVar[int]
        LOW_PRICE_LAST_52_WEEKS_FIELD_NUMBER: _ClassVar[int]
        AVERAGE_DAILY_VOLUME_LAST_10_DAYS_FIELD_NUMBER: _ClassVar[int]
        AVERAGE_DAILY_VOLUME_LAST_4_WEEKS_FIELD_NUMBER: _ClassVar[int]
        BETA_FIELD_NUMBER: _ClassVar[int]
        FREE_FLOAT_FIELD_NUMBER: _ClassVar[int]
        FORWARD_ANNUAL_DIVIDEND_YIELD_FIELD_NUMBER: _ClassVar[int]
        SHARES_OUTSTANDING_FIELD_NUMBER: _ClassVar[int]
        REVENUE_TTM_FIELD_NUMBER: _ClassVar[int]
        EBITDA_TTM_FIELD_NUMBER: _ClassVar[int]
        NET_INCOME_TTM_FIELD_NUMBER: _ClassVar[int]
        EPS_TTM_FIELD_NUMBER: _ClassVar[int]
        DILUTED_EPS_TTM_FIELD_NUMBER: _ClassVar[int]
        FREE_CASH_FLOW_TTM_FIELD_NUMBER: _ClassVar[int]
        FIVE_YEAR_ANNUAL_REVENUE_GROWTH_RATE_FIELD_NUMBER: _ClassVar[int]
        THREE_YEAR_ANNUAL_REVENUE_GROWTH_RATE_FIELD_NUMBER: _ClassVar[int]
        PE_RATIO_TTM_FIELD_NUMBER: _ClassVar[int]
        PRICE_TO_SALES_TTM_FIELD_NUMBER: _ClassVar[int]
        PRICE_TO_BOOK_TTM_FIELD_NUMBER: _ClassVar[int]
        PRICE_TO_FREE_CASH_FLOW_TTM_FIELD_NUMBER: _ClassVar[int]
        TOTAL_ENTERPRISE_VALUE_MRQ_FIELD_NUMBER: _ClassVar[int]
        EV_TO_EBITDA_MRQ_FIELD_NUMBER: _ClassVar[int]
        NET_MARGIN_MRQ_FIELD_NUMBER: _ClassVar[int]
        NET_INTEREST_MARGIN_MRQ_FIELD_NUMBER: _ClassVar[int]
        ROE_FIELD_NUMBER: _ClassVar[int]
        ROA_FIELD_NUMBER: _ClassVar[int]
        ROIC_FIELD_NUMBER: _ClassVar[int]
        TOTAL_DEBT_MRQ_FIELD_NUMBER: _ClassVar[int]
        TOTAL_DEBT_TO_EQUITY_MRQ_FIELD_NUMBER: _ClassVar[int]
        TOTAL_DEBT_TO_EBITDA_MRQ_FIELD_NUMBER: _ClassVar[int]
        FREE_CASH_FLOW_TO_PRICE_FIELD_NUMBER: _ClassVar[int]
        NET_DEBT_TO_EBITDA_FIELD_NUMBER: _ClassVar[int]
        CURRENT_RATIO_MRQ_FIELD_NUMBER: _ClassVar[int]
        FIXED_CHARGE_COVERAGE_RATIO_FY_FIELD_NUMBER: _ClassVar[int]
        DIVIDEND_YIELD_DAILY_TTM_FIELD_NUMBER: _ClassVar[int]
        DIVIDEND_RATE_TTM_FIELD_NUMBER: _ClassVar[int]
        DIVIDENDS_PER_SHARE_FIELD_NUMBER: _ClassVar[int]
        FIVE_YEARS_AVERAGE_DIVIDEND_YIELD_FIELD_NUMBER: _ClassVar[int]
        FIVE_YEAR_ANNUAL_DIVIDEND_GROWTH_RATE_FIELD_NUMBER: _ClassVar[int]
        DIVIDEND_PAYOUT_RATIO_FY_FIELD_NUMBER: _ClassVar[int]
        BUY_BACK_TTM_FIELD_NUMBER: _ClassVar[int]
        ONE_YEAR_ANNUAL_REVENUE_GROWTH_RATE_FIELD_NUMBER: _ClassVar[int]
        DOMICILE_INDICATOR_CODE_FIELD_NUMBER: _ClassVar[int]
        ADR_TO_COMMON_SHARE_RATIO_FIELD_NUMBER: _ClassVar[int]
        NUMBER_OF_EMPLOYEES_FIELD_NUMBER: _ClassVar[int]
        EX_DIVIDEND_DATE_FIELD_NUMBER: _ClassVar[int]
        FISCAL_PERIOD_START_DATE_FIELD_NUMBER: _ClassVar[int]
        FISCAL_PERIOD_END_DATE_FIELD_NUMBER: _ClassVar[int]
        REVENUE_CHANGE_FIVE_YEARS_FIELD_NUMBER: _ClassVar[int]
        EPS_CHANGE_FIVE_YEARS_FIELD_NUMBER: _ClassVar[int]
        EBITDA_CHANGE_FIVE_YEARS_FIELD_NUMBER: _ClassVar[int]
        TOTAL_DEBT_CHANGE_FIVE_YEARS_FIELD_NUMBER: _ClassVar[int]
        EV_TO_SALES_FIELD_NUMBER: _ClassVar[int]
        asset_uid: str
        currency: str
        market_capitalization: float
        high_price_last_52_weeks: float
        low_price_last_52_weeks: float
        average_daily_volume_last_10_days: float
        average_daily_volume_last_4_weeks: float
        beta: float
        free_float: float
        forward_annual_dividend_yield: float
        shares_outstanding: float
        revenue_ttm: float
        ebitda_ttm: float
        net_income_ttm: float
        eps_ttm: float
        diluted_eps_ttm: float
        free_cash_flow_ttm: float
        five_year_annual_revenue_growth_rate: float
        three_year_annual_revenue_growth_rate: float
        pe_ratio_ttm: float
        price_to_sales_ttm: float
        price_to_book_ttm: float
        price_to_free_cash_flow_ttm: float
        total_enterprise_value_mrq: float
        ev_to_ebitda_mrq: float
        net_margin_mrq: float
        net_interest_margin_mrq: float
        roe: float
        roa: float
        roic: float
        total_debt_mrq: float
        total_debt_to_equity_mrq: float
        total_debt_to_ebitda_mrq: float
        free_cash_flow_to_price: float
        net_debt_to_ebitda: float
        current_ratio_mrq: float
        fixed_charge_coverage_ratio_fy: float
        dividend_yield_daily_ttm: float
        dividend_rate_ttm: float
        dividends_per_share: float
        five_years_average_dividend_yield: float
        five_year_annual_dividend_growth_rate: float
        dividend_payout_ratio_fy: float
        buy_back_ttm: float
        one_year_annual_revenue_growth_rate: float
        domicile_indicator_code: str
        adr_to_common_share_ratio: float
        number_of_employees: float
        ex_dividend_date: _timestamp_pb2.Timestamp
        fiscal_period_start_date: _timestamp_pb2.Timestamp
        fiscal_period_end_date: _timestamp_pb2.Timestamp
        revenue_change_five_years: float
        eps_change_five_years: float
        ebitda_change_five_years: float
        total_debt_change_five_years: float
        ev_to_sales: float
        def __init__(self, asset_uid: _Optional[str] = ..., currency: _Optional[str] = ..., market_capitalization: _Optional[float] = ..., high_price_last_52_weeks: _Optional[float] = ..., low_price_last_52_weeks: _Optional[float] = ..., average_daily_volume_last_10_days: _Optional[float] = ..., average_daily_volume_last_4_weeks: _Optional[float] = ..., beta: _Optional[float] = ..., free_float: _Optional[float] = ..., forward_annual_dividend_yield: _Optional[float] = ..., shares_outstanding: _Optional[float] = ..., revenue_ttm: _Optional[float] = ..., ebitda_ttm: _Optional[float] = ..., net_income_ttm: _Optional[float] = ..., eps_ttm: _Optional[float] = ..., diluted_eps_ttm: _Optional[float] = ..., free_cash_flow_ttm: _Optional[float] = ..., five_year_annual_revenue_growth_rate: _Optional[float] = ..., three_year_annual_revenue_growth_rate: _Optional[float] = ..., pe_ratio_ttm: _Optional[float] = ..., price_to_sales_ttm: _Optional[float] = ..., price_to_book_ttm: _Optional[float] = ..., price_to_free_cash_flow_ttm: _Optional[float] = ..., total_enterprise_value_mrq: _Optional[float] = ..., ev_to_ebitda_mrq: _Optional[float] = ..., net_margin_mrq: _Optional[float] = ..., net_interest_margin_mrq: _Optional[float] = ..., roe: _Optional[float] = ..., roa: _Optional[float] = ..., roic: _Optional[float] = ..., total_debt_mrq: _Optional[float] = ..., total_debt_to_equity_mrq: _Optional[float] = ..., total_debt_to_ebitda_mrq: _Optional[float] = ..., free_cash_flow_to_price: _Optional[float] = ..., net_debt_to_ebitda: _Optional[float] = ..., current_ratio_mrq: _Optional[float] = ..., fixed_charge_coverage_ratio_fy: _Optional[float] = ..., dividend_yield_daily_ttm: _Optional[float] = ..., dividend_rate_ttm: _Optional[float] = ..., dividends_per_share: _Optional[float] = ..., five_years_average_dividend_yield: _Optional[float] = ..., five_year_annual_dividend_growth_rate: _Optional[float] = ..., dividend_payout_ratio_fy: _Optional[float] = ..., buy_back_ttm: _Optional[float] = ..., one_year_annual_revenue_growth_rate: _Optional[float] = ..., domicile_indicator_code: _Optional[str] = ..., adr_to_common_share_ratio: _Optional[float] = ..., number_of_employees: _Optional[float] = ..., ex_dividend_date: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., fiscal_period_start_date: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., fiscal_period_end_date: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., revenue_change_five_years: _Optional[float] = ..., eps_change_five_years: _Optional[float] = ..., ebitda_change_five_years: _Optional[float] = ..., total_debt_change_five_years: _Optional[float] = ..., ev_to_sales: _Optional[float] = ...) -> None: ...
    FUNDAMENTALS_FIELD_NUMBER: _ClassVar[int]
    fundamentals: _containers.RepeatedCompositeFieldContainer[GetAssetFundamentalsResponse.StatisticResponse]
    def __init__(self, fundamentals: _Optional[_Iterable[_Union[GetAssetFundamentalsResponse.StatisticResponse, _Mapping]]] = ...) -> None: ...

class GetAssetReportsRequest(_message.Message):
    __slots__ = ("instrument_id", "to")
    INSTRUMENT_ID_FIELD_NUMBER: _ClassVar[int]
    FROM_FIELD_NUMBER: _ClassVar[int]
    TO_FIELD_NUMBER: _ClassVar[int]
    instrument_id: str
    to: _timestamp_pb2.Timestamp
    def __init__(self, instrument_id: _Optional[str] = ..., to: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., **kwargs) -> None: ...

class GetAssetReportsResponse(_message.Message):
    __slots__ = ("events",)
    class AssetReportPeriodType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        PERIOD_TYPE_UNSPECIFIED: _ClassVar[GetAssetReportsResponse.AssetReportPeriodType]
        PERIOD_TYPE_QUARTER: _ClassVar[GetAssetReportsResponse.AssetReportPeriodType]
        PERIOD_TYPE_SEMIANNUAL: _ClassVar[GetAssetReportsResponse.AssetReportPeriodType]
        PERIOD_TYPE_ANNUAL: _ClassVar[GetAssetReportsResponse.AssetReportPeriodType]
    PERIOD_TYPE_UNSPECIFIED: GetAssetReportsResponse.AssetReportPeriodType
    PERIOD_TYPE_QUARTER: GetAssetReportsResponse.AssetReportPeriodType
    PERIOD_TYPE_SEMIANNUAL: GetAssetReportsResponse.AssetReportPeriodType
    PERIOD_TYPE_ANNUAL: GetAssetReportsResponse.AssetReportPeriodType
    class GetAssetReportsEvent(_message.Message):
        __slots__ = ("instrument_id", "report_date", "period_year", "period_num", "period_type", "created_at")
        INSTRUMENT_ID_FIELD_NUMBER: _ClassVar[int]
        REPORT_DATE_FIELD_NUMBER: _ClassVar[int]
        PERIOD_YEAR_FIELD_NUMBER: _ClassVar[int]
        PERIOD_NUM_FIELD_NUMBER: _ClassVar[int]
        PERIOD_TYPE_FIELD_NUMBER: _ClassVar[int]
        CREATED_AT_FIELD_NUMBER: _ClassVar[int]
        instrument_id: str
        report_date: _timestamp_pb2.Timestamp
        period_year: int
        period_num: int
        period_type: GetAssetReportsResponse.AssetReportPeriodType
        created_at: _timestamp_pb2.Timestamp
        def __init__(self, instrument_id: _Optional[str] = ..., report_date: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., period_year: _Optional[int] = ..., period_num: _Optional[int] = ..., period_type: _Optional[_Union[GetAssetReportsResponse.AssetReportPeriodType, str]] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
    EVENTS_FIELD_NUMBER: _ClassVar[int]
    events: _containers.RepeatedCompositeFieldContainer[GetAssetReportsResponse.GetAssetReportsEvent]
    def __init__(self, events: _Optional[_Iterable[_Union[GetAssetReportsResponse.GetAssetReportsEvent, _Mapping]]] = ...) -> None: ...

class GetConsensusForecastsRequest(_message.Message):
    __slots__ = ("paging",)
    PAGING_FIELD_NUMBER: _ClassVar[int]
    paging: _common_pb2.Page
    def __init__(self, paging: _Optional[_Union[_common_pb2.Page, _Mapping]] = ...) -> None: ...

class GetConsensusForecastsResponse(_message.Message):
    __slots__ = ("items", "page")
    class ConsensusForecastsItem(_message.Message):
        __slots__ = ("uid", "asset_uid", "created_at", "best_target_price", "best_target_low", "best_target_high", "total_buy_recommend", "total_hold_recommend", "total_sell_recommend", "currency", "consensus", "prognosis_date")
        UID_FIELD_NUMBER: _ClassVar[int]
        ASSET_UID_FIELD_NUMBER: _ClassVar[int]
        CREATED_AT_FIELD_NUMBER: _ClassVar[int]
        BEST_TARGET_PRICE_FIELD_NUMBER: _ClassVar[int]
        BEST_TARGET_LOW_FIELD_NUMBER: _ClassVar[int]
        BEST_TARGET_HIGH_FIELD_NUMBER: _ClassVar[int]
        TOTAL_BUY_RECOMMEND_FIELD_NUMBER: _ClassVar[int]
        TOTAL_HOLD_RECOMMEND_FIELD_NUMBER: _ClassVar[int]
        TOTAL_SELL_RECOMMEND_FIELD_NUMBER: _ClassVar[int]
        CURRENCY_FIELD_NUMBER: _ClassVar[int]
        CONSENSUS_FIELD_NUMBER: _ClassVar[int]
        PROGNOSIS_DATE_FIELD_NUMBER: _ClassVar[int]
        uid: str
        asset_uid: str
        created_at: _timestamp_pb2.Timestamp
        best_target_price: _common_pb2.Quotation
        best_target_low: _common_pb2.Quotation
        best_target_high: _common_pb2.Quotation
        total_buy_recommend: int
        total_hold_recommend: int
        total_sell_recommend: int
        currency: str
        consensus: Recommendation
        prognosis_date: _timestamp_pb2.Timestamp
        def __init__(self, uid: _Optional[str] = ..., asset_uid: _Optional[str] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., best_target_price: _Optional[_Union[_common_pb2.Quotation, _Mapping]] = ..., best_target_low: _Optional[_Union[_common_pb2.Quotation, _Mapping]] = ..., best_target_high: _Optional[_Union[_common_pb2.Quotation, _Mapping]] = ..., total_buy_recommend: _Optional[int] = ..., total_hold_recommend: _Optional[int] = ..., total_sell_recommend: _Optional[int] = ..., currency: _Optional[str] = ..., consensus: _Optional[_Union[Recommendation, str]] = ..., prognosis_date: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[GetConsensusForecastsResponse.ConsensusForecastsItem]
    page: _common_pb2.PageResponse
    def __init__(self, items: _Optional[_Iterable[_Union[GetConsensusForecastsResponse.ConsensusForecastsItem, _Mapping]]] = ..., page: _Optional[_Union[_common_pb2.PageResponse, _Mapping]] = ...) -> None: ...

class GetForecastRequest(_message.Message):
    __slots__ = ("instrument_id",)
    INSTRUMENT_ID_FIELD_NUMBER: _ClassVar[int]
    instrument_id: str
    def __init__(self, instrument_id: _Optional[str] = ...) -> None: ...

class GetForecastResponse(_message.Message):
    __slots__ = ("targets", "consensus")
    class TargetItem(_message.Message):
        __slots__ = ("uid", "ticker", "company", "recommendation", "recommendation_date", "currency", "current_price", "target_price", "price_change", "price_change_rel", "show_name")
        UID_FIELD_NUMBER: _ClassVar[int]
        TICKER_FIELD_NUMBER: _ClassVar[int]
        COMPANY_FIELD_NUMBER: _ClassVar[int]
        RECOMMENDATION_FIELD_NUMBER: _ClassVar[int]
        RECOMMENDATION_DATE_FIELD_NUMBER: _ClassVar[int]
        CURRENCY_FIELD_NUMBER: _ClassVar[int]
        CURRENT_PRICE_FIELD_NUMBER: _ClassVar[int]
        TARGET_PRICE_FIELD_NUMBER: _ClassVar[int]
        PRICE_CHANGE_FIELD_NUMBER: _ClassVar[int]
        PRICE_CHANGE_REL_FIELD_NUMBER: _ClassVar[int]
        SHOW_NAME_FIELD_NUMBER: _ClassVar[int]
        uid: str
        ticker: str
        company: str
        recommendation: Recommendation
        recommendation_date: _timestamp_pb2.Timestamp
        currency: str
        current_price: _common_pb2.Quotation
        target_price: _common_pb2.Quotation
        price_change: _common_pb2.Quotation
        price_change_rel: _common_pb2.Quotation
        show_name: str
        def __init__(self, uid: _Optional[str] = ..., ticker: _Optional[str] = ..., company: _Optional[str] = ..., recommendation: _Optional[_Union[Recommendation, str]] = ..., recommendation_date: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., currency: _Optional[str] = ..., current_price: _Optional[_Union[_common_pb2.Quotation, _Mapping]] = ..., target_price: _Optional[_Union[_common_pb2.Quotation, _Mapping]] = ..., price_change: _Optional[_Union[_common_pb2.Quotation, _Mapping]] = ..., price_change_rel: _Optional[_Union[_common_pb2.Quotation, _Mapping]] = ..., show_name: _Optional[str] = ...) -> None: ...
    class ConsensusItem(_message.Message):
        __slots__ = ("uid", "ticker", "recommendation", "currency", "current_price", "consensus", "min_target", "max_target", "price_change", "price_change_rel")
        UID_FIELD_NUMBER: _ClassVar[int]
        TICKER_FIELD_NUMBER: _ClassVar[int]
        RECOMMENDATION_FIELD_NUMBER: _ClassVar[int]
        CURRENCY_FIELD_NUMBER: _ClassVar[int]
        CURRENT_PRICE_FIELD_NUMBER: _ClassVar[int]
        CONSENSUS_FIELD_NUMBER: _ClassVar[int]
        MIN_TARGET_FIELD_NUMBER: _ClassVar[int]
        MAX_TARGET_FIELD_NUMBER: _ClassVar[int]
        PRICE_CHANGE_FIELD_NUMBER: _ClassVar[int]
        PRICE_CHANGE_REL_FIELD_NUMBER: _ClassVar[int]
        uid: str
        ticker: str
        recommendation: Recommendation
        currency: str
        current_price: _common_pb2.Quotation
        consensus: _common_pb2.Quotation
        min_target: _common_pb2.Quotation
        max_target: _common_pb2.Quotation
        price_change: _common_pb2.Quotation
        price_change_rel: _common_pb2.Quotation
        def __init__(self, uid: _Optional[str] = ..., ticker: _Optional[str] = ..., recommendation: _Optional[_Union[Recommendation, str]] = ..., currency: _Optional[str] = ..., current_price: _Optional[_Union[_common_pb2.Quotation, _Mapping]] = ..., consensus: _Optional[_Union[_common_pb2.Quotation, _Mapping]] = ..., min_target: _Optional[_Union[_common_pb2.Quotation, _Mapping]] = ..., max_target: _Optional[_Union[_common_pb2.Quotation, _Mapping]] = ..., price_change: _Optional[_Union[_common_pb2.Quotation, _Mapping]] = ..., price_change_rel: _Optional[_Union[_common_pb2.Quotation, _Mapping]] = ...) -> None: ...
    TARGETS_FIELD_NUMBER: _ClassVar[int]
    CONSENSUS_FIELD_NUMBER: _ClassVar[int]
    targets: _containers.RepeatedCompositeFieldContainer[GetForecastResponse.TargetItem]
    consensus: GetForecastResponse.ConsensusItem
    def __init__(self, targets: _Optional[_Iterable[_Union[GetForecastResponse.TargetItem, _Mapping]]] = ..., consensus: _Optional[_Union[GetForecastResponse.ConsensusItem, _Mapping]] = ...) -> None: ...

class TradingInterval(_message.Message):
    __slots__ = ("type", "interval")
    class TimeInterval(_message.Message):
        __slots__ = ("start_ts", "end_ts")
        START_TS_FIELD_NUMBER: _ClassVar[int]
        END_TS_FIELD_NUMBER: _ClassVar[int]
        start_ts: _timestamp_pb2.Timestamp
        end_ts: _timestamp_pb2.Timestamp
        def __init__(self, start_ts: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., end_ts: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
    TYPE_FIELD_NUMBER: _ClassVar[int]
    INTERVAL_FIELD_NUMBER: _ClassVar[int]
    type: str
    interval: TradingInterval.TimeInterval
    def __init__(self, type: _Optional[str] = ..., interval: _Optional[_Union[TradingInterval.TimeInterval, _Mapping]] = ...) -> None: ...
