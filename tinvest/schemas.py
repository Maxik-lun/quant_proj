# pylint:disable=too-many-lines
# pylint:disable=too-many-instance-attributes
from dataclasses import dataclass
from datetime import datetime
from typing import List, Optional, SupportsAbs
from utils import ts_to_datetime

from enum import Enum


class SecurityTradingStatus(Enum):
    SECURITY_TRADING_STATUS_UNSPECIFIED = 0
    SECURITY_TRADING_STATUS_NOT_AVAILABLE_FOR_TRADING = 1
    SECURITY_TRADING_STATUS_OPENING_PERIOD = 2
    SECURITY_TRADING_STATUS_CLOSING_PERIOD = 3
    SECURITY_TRADING_STATUS_BREAK_IN_TRADING = 4
    SECURITY_TRADING_STATUS_NORMAL_TRADING = 5
    SECURITY_TRADING_STATUS_CLOSING_AUCTION = 6
    SECURITY_TRADING_STATUS_DARK_POOL_AUCTION = 7
    SECURITY_TRADING_STATUS_DISCRETE_AUCTION = 8
    SECURITY_TRADING_STATUS_OPENING_AUCTION_PERIOD = 9
    SECURITY_TRADING_STATUS_TRADING_AT_CLOSING_AUCTION_PRICE = 10
    SECURITY_TRADING_STATUS_SESSION_ASSIGNED = 11
    SECURITY_TRADING_STATUS_SESSION_CLOSE = 12
    SECURITY_TRADING_STATUS_SESSION_OPEN = 13
    SECURITY_TRADING_STATUS_DEALER_NORMAL_TRADING = 14
    SECURITY_TRADING_STATUS_DEALER_BREAK_IN_TRADING = 15
    SECURITY_TRADING_STATUS_DEALER_NOT_AVAILABLE_FOR_TRADING = 16


class InstrumentIdType(Enum):
    INSTRUMENT_ID_UNSPECIFIED = 0
    INSTRUMENT_ID_TYPE_FIGI = 1
    INSTRUMENT_ID_TYPE_TICKER = 2
    INSTRUMENT_ID_TYPE_UID = 3
    INSTRUMENT_ID_TYPE_POSITION_UID = 4


class InstrumentStatus(Enum):
    INSTRUMENT_STATUS_UNSPECIFIED = 0
    INSTRUMENT_STATUS_BASE = 1
    INSTRUMENT_STATUS_ALL = 2


class ShareType(Enum):
    SHARE_TYPE_UNSPECIFIED = 0
    SHARE_TYPE_COMMON = 1
    SHARE_TYPE_PREFERRED = 2
    SHARE_TYPE_ADR = 3
    SHARE_TYPE_GDR = 4
    SHARE_TYPE_MLP = 5
    SHARE_TYPE_NY_REG_SHRS = 6
    SHARE_TYPE_CLOSED_END_FUND = 7
    SHARE_TYPE_REIT = 8


class SubscriptionAction(Enum):
    SUBSCRIPTION_ACTION_UNSPECIFIED = 0
    SUBSCRIPTION_ACTION_SUBSCRIBE = 1
    SUBSCRIPTION_ACTION_UNSUBSCRIBE = 2


class SubscriptionInterval(Enum):
    SUBSCRIPTION_INTERVAL_UNSPECIFIED = 0
    SUBSCRIPTION_INTERVAL_ONE_MINUTE = 1
    SUBSCRIPTION_INTERVAL_FIVE_MINUTES = 2
    SUBSCRIPTION_INTERVAL_FIFTEEN_MINUTES = 3
    SUBSCRIPTION_INTERVAL_ONE_HOUR = 4
    SUBSCRIPTION_INTERVAL_ONE_DAY = 5
    SUBSCRIPTION_INTERVAL_2_MIN = 6
    SUBSCRIPTION_INTERVAL_3_MIN = 7
    SUBSCRIPTION_INTERVAL_10_MIN = 8
    SUBSCRIPTION_INTERVAL_30_MIN = 9
    SUBSCRIPTION_INTERVAL_2_HOUR = 10
    SUBSCRIPTION_INTERVAL_4_HOUR = 11
    SUBSCRIPTION_INTERVAL_WEEK = 12
    SUBSCRIPTION_INTERVAL_MONTH = 13


class SubscriptionStatus(Enum):
    SUBSCRIPTION_STATUS_UNSPECIFIED = 0
    SUBSCRIPTION_STATUS_SUCCESS = 1
    SUBSCRIPTION_STATUS_INSTRUMENT_NOT_FOUND = 2
    SUBSCRIPTION_STATUS_SUBSCRIPTION_ACTION_IS_INVALID = 3
    SUBSCRIPTION_STATUS_DEPTH_IS_INVALID = 4
    SUBSCRIPTION_STATUS_INTERVAL_IS_INVALID = 5
    SUBSCRIPTION_STATUS_LIMIT_IS_EXCEEDED = 6
    SUBSCRIPTION_STATUS_INTERNAL_ERROR = 7
    SUBSCRIPTION_STATUS_TOO_MANY_REQUESTS = 8
    SUBSCRIPTION_STATUS_SUBSCRIPTION_NOT_FOUND = 9


class TradeDirection(Enum):
    TRADE_DIRECTION_UNSPECIFIED = 0
    TRADE_DIRECTION_BUY = 1
    TRADE_DIRECTION_SELL = 2


class CandleInterval(Enum):
    CANDLE_INTERVAL_UNSPECIFIED = 0
    CANDLE_INTERVAL_1_MIN = 1
    CANDLE_INTERVAL_2_MIN = 6
    CANDLE_INTERVAL_3_MIN = 7
    CANDLE_INTERVAL_5_MIN = 2
    CANDLE_INTERVAL_10_MIN = 8
    CANDLE_INTERVAL_15_MIN = 3
    CANDLE_INTERVAL_30_MIN = 9
    CANDLE_INTERVAL_HOUR = 4
    CANDLE_INTERVAL_2_HOUR = 10
    CANDLE_INTERVAL_4_HOUR = 11
    CANDLE_INTERVAL_DAY = 5
    CANDLE_INTERVAL_WEEK = 12
    CANDLE_INTERVAL_MONTH = 13


class CandleSource(Enum):
    CANDLE_SOURCE_UNSPECIFIED = 0
    CANDLE_SOURCE_EXCHANGE = 1
    CANDLE_SOURCE_DEALER_WEEKEND = 2
    CANDLE_SOURCE_INCLUDE_WEEKEND = 3


class OperationState(Enum):
    OPERATION_STATE_UNSPECIFIED = 0
    OPERATION_STATE_EXECUTED = 1
    OPERATION_STATE_CANCELED = 2
    OPERATION_STATE_PROGRESS = 3


class OrderDirection(Enum):
    ORDER_DIRECTION_UNSPECIFIED = 0
    ORDER_DIRECTION_BUY = 1
    ORDER_DIRECTION_SELL = 2


class OrderType(Enum):
    ORDER_TYPE_UNSPECIFIED = 0
    ORDER_TYPE_LIMIT = 1
    ORDER_TYPE_MARKET = 2
    ORDER_TYPE_BESTPRICE = 3


class OrderExecutionReportStatus(Enum):
    EXECUTION_REPORT_STATUS_UNSPECIFIED = 0
    EXECUTION_REPORT_STATUS_FILL = 1
    EXECUTION_REPORT_STATUS_REJECTED = 2
    EXECUTION_REPORT_STATUS_CANCELLED = 3
    EXECUTION_REPORT_STATUS_NEW = 4
    EXECUTION_REPORT_STATUS_PARTIALLYFILL = 5


class AccountType(Enum):
    ACCOUNT_TYPE_UNSPECIFIED = 0
    ACCOUNT_TYPE_TINKOFF = 1
    ACCOUNT_TYPE_TINKOFF_IIS = 2
    ACCOUNT_TYPE_INVEST_BOX = 3
    ACCOUNT_TYPE_INVEST_FUND = 4


class AccountStatus(Enum):
    ACCOUNT_STATUS_UNSPECIFIED = 0
    ACCOUNT_STATUS_NEW = 1
    ACCOUNT_STATUS_OPEN = 2
    ACCOUNT_STATUS_CLOSED = 3


class StopOrderDirection(Enum):
    STOP_ORDER_DIRECTION_UNSPECIFIED = 0
    STOP_ORDER_DIRECTION_BUY = 1
    STOP_ORDER_DIRECTION_SELL = 2


class StopOrderExpirationType(Enum):
    STOP_ORDER_EXPIRATION_TYPE_UNSPECIFIED = 0
    STOP_ORDER_EXPIRATION_TYPE_GOOD_TILL_CANCEL = 1
    STOP_ORDER_EXPIRATION_TYPE_GOOD_TILL_DATE = 2


class StopOrderType(Enum):
    STOP_ORDER_TYPE_UNSPECIFIED = 0
    STOP_ORDER_TYPE_TAKE_PROFIT = 1
    STOP_ORDER_TYPE_STOP_LOSS = 2
    STOP_ORDER_TYPE_STOP_LIMIT = 3


class OperationType(Enum):
    OPERATION_TYPE_UNSPECIFIED = 0
    OPERATION_TYPE_INPUT = 1
    OPERATION_TYPE_BOND_TAX = 2
    OPERATION_TYPE_OUTPUT_SECURITIES = 3
    OPERATION_TYPE_OVERNIGHT = 4
    OPERATION_TYPE_TAX = 5
    OPERATION_TYPE_BOND_REPAYMENT_FULL = 6
    OPERATION_TYPE_SELL_CARD = 7
    OPERATION_TYPE_DIVIDEND_TAX = 8
    OPERATION_TYPE_OUTPUT = 9
    OPERATION_TYPE_BOND_REPAYMENT = 10
    OPERATION_TYPE_TAX_CORRECTION = 11
    OPERATION_TYPE_SERVICE_FEE = 12
    OPERATION_TYPE_BENEFIT_TAX = 13
    OPERATION_TYPE_MARGIN_FEE = 14
    OPERATION_TYPE_BUY = 15
    OPERATION_TYPE_BUY_CARD = 16
    OPERATION_TYPE_INPUT_SECURITIES = 17
    OPERATION_TYPE_SELL_MARGIN = 18
    OPERATION_TYPE_BROKER_FEE = 19
    OPERATION_TYPE_BUY_MARGIN = 20
    OPERATION_TYPE_DIVIDEND = 21
    OPERATION_TYPE_SELL = 22
    OPERATION_TYPE_COUPON = 23
    OPERATION_TYPE_SUCCESS_FEE = 24
    OPERATION_TYPE_DIVIDEND_TRANSFER = 25
    OPERATION_TYPE_ACCRUING_VARMARGIN = 26
    OPERATION_TYPE_WRITING_OFF_VARMARGIN = 27
    OPERATION_TYPE_DELIVERY_BUY = 28
    OPERATION_TYPE_DELIVERY_SELL = 29
    OPERATION_TYPE_TRACK_MFEE = 30
    OPERATION_TYPE_TRACK_PFEE = 31
    OPERATION_TYPE_TAX_PROGRESSIVE = 32
    OPERATION_TYPE_BOND_TAX_PROGRESSIVE = 33
    OPERATION_TYPE_DIVIDEND_TAX_PROGRESSIVE = 34
    OPERATION_TYPE_BENEFIT_TAX_PROGRESSIVE = 35
    OPERATION_TYPE_TAX_CORRECTION_PROGRESSIVE = 36
    OPERATION_TYPE_TAX_REPO_PROGRESSIVE = 37
    OPERATION_TYPE_TAX_REPO = 38
    OPERATION_TYPE_TAX_REPO_HOLD = 39
    OPERATION_TYPE_TAX_REPO_REFUND = 40
    OPERATION_TYPE_TAX_REPO_HOLD_PROGRESSIVE = 41
    OPERATION_TYPE_TAX_REPO_REFUND_PROGRESSIVE = 42
    OPERATION_TYPE_DIV_EXT = 43
    OPERATION_TYPE_TAX_CORRECTION_COUPON = 44
    OPERATION_TYPE_CASH_FEE = 45
    OPERATION_TYPE_OUT_FEE = 46
    OPERATION_TYPE_OUT_STAMP_DUTY = 47
    OPERATION_TYPE_OUTPUT_SWIFT = 50
    OPERATION_TYPE_INPUT_SWIFT = 51
    OPERATION_TYPE_OUTPUT_ACQUIRING = 53
    OPERATION_TYPE_INPUT_ACQUIRING = 54
    OPERATION_TYPE_OUTPUT_PENALTY = 55
    OPERATION_TYPE_ADVICE_FEE = 56
    OPERATION_TYPE_TRANS_IIS_BS = 57
    OPERATION_TYPE_TRANS_BS_BS = 58
    OPERATION_TYPE_OUT_MULTI = 59
    OPERATION_TYPE_INP_MULTI = 60
    OPERATION_TYPE_OVER_PLACEMENT = 61
    OPERATION_TYPE_OVER_COM = 62
    OPERATION_TYPE_OVER_INCOME = 63
    OPERATION_TYPE_OPTION_EXPIRATION = 64
    OPERATION_TYPE_FUTURE_EXPIRATION = 65


class AccessLevel(Enum):
    ACCOUNT_ACCESS_LEVEL_UNSPECIFIED = 0
    ACCOUNT_ACCESS_LEVEL_FULL_ACCESS = 1
    ACCOUNT_ACCESS_LEVEL_READ_ONLY = 2
    ACCOUNT_ACCESS_LEVEL_NO_ACCESS = 3


class CouponType(Enum):
    COUPON_TYPE_UNSPECIFIED = 0
    COUPON_TYPE_CONSTANT = 1
    COUPON_TYPE_FLOATING = 2
    COUPON_TYPE_DISCOUNT = 3
    COUPON_TYPE_MORTGAGE = 4
    COUPON_TYPE_FIX = 5
    COUPON_TYPE_VARIABLE = 6
    COUPON_TYPE_OTHER = 7


class AssetType(Enum):
    ASSET_TYPE_UNSPECIFIED = 0
    ASSET_TYPE_CURRENCY = 1
    ASSET_TYPE_COMMODITY = 2
    ASSET_TYPE_INDEX = 3
    ASSET_TYPE_SECURITY = 4


class StructuredProductType(Enum):
    SP_TYPE_UNSPECIFIED = 0
    SP_TYPE_DELIVERABLE = 1
    SP_TYPE_NON_DELIVERABLE = 2


class EditFavoritesActionType(Enum):
    EDIT_FAVORITES_ACTION_TYPE_UNSPECIFIED = 0
    EDIT_FAVORITES_ACTION_TYPE_ADD = 1
    EDIT_FAVORITES_ACTION_TYPE_DEL = 2


class RealExchange(Enum):
    REAL_EXCHANGE_UNSPECIFIED = 0
    REAL_EXCHANGE_MOEX = 1
    REAL_EXCHANGE_RTS = 2
    REAL_EXCHANGE_OTC = 3
    REAL_EXCHANGE_DEALER = 4


class PortfolioSubscriptionStatus(Enum):
    PORTFOLIO_SUBSCRIPTION_STATUS_UNSPECIFIED = 0
    PORTFOLIO_SUBSCRIPTION_STATUS_SUCCESS = 1
    PORTFOLIO_SUBSCRIPTION_STATUS_ACCOUNT_NOT_FOUND = 2
    PORTFOLIO_SUBSCRIPTION_STATUS_INTERNAL_ERROR = 3


class InstrumentType(Enum):
    INSTRUMENT_TYPE_UNSPECIFIED = 0
    INSTRUMENT_TYPE_BOND = 1
    INSTRUMENT_TYPE_SHARE = 2
    INSTRUMENT_TYPE_CURRENCY = 3
    INSTRUMENT_TYPE_ETF = 4
    INSTRUMENT_TYPE_FUTURES = 5
    INSTRUMENT_TYPE_SP = 6
    INSTRUMENT_TYPE_OPTION = 7
    INSTRUMENT_TYPE_CLEARING_CERTIFICATE = 8
    INSTRUMENT_TYPE_INDEX = 9
    INSTRUMENT_TYPE_COMMODITY = 10


class OptionDirection(Enum):
    OPTION_DIRECTION_UNSPECIFIED = 0
    OPTION_DIRECTION_PUT = 1
    OPTION_DIRECTION_CALL = 2


class OptionPaymentType(Enum):
    OPTION_PAYMENT_TYPE_UNSPECIFIED = 0
    OPTION_PAYMENT_TYPE_PREMIUM = 1
    OPTION_PAYMENT_TYPE_MARGINAL = 2


class OptionStyle(Enum):
    OPTION_STYLE_UNSPECIFIED = 0
    OPTION_STYLE_AMERICAN = 1
    OPTION_STYLE_EUROPEAN = 2


class OptionSettlementType(Enum):
    OPTION_EXECUTION_TYPE_UNSPECIFIED = 0
    OPTION_EXECUTION_TYPE_PHYSICAL_DELIVERY = 1
    OPTION_EXECUTION_TYPE_CASH_SETTLEMENT = 2


class PositionsAccountSubscriptionStatus(Enum):
    POSITIONS_SUBSCRIPTION_STATUS_UNSPECIFIED = 0
    POSITIONS_SUBSCRIPTION_STATUS_SUCCESS = 1
    POSITIONS_SUBSCRIPTION_STATUS_ACCOUNT_NOT_FOUND = 2
    POSITIONS_SUBSCRIPTION_STATUS_INTERNAL_ERROR = 3


class RiskLevel(Enum):
    RISK_LEVEL_UNSPECIFIED = 0
    RISK_LEVEL_LOW = 1
    RISK_LEVEL_MODERATE = 2
    RISK_LEVEL_HIGH = 3


class StopOrderStatusOption(Enum):
    STOP_ORDER_STATUS_UNSPECIFIED = 0
    STOP_ORDER_STATUS_ALL = 1
    STOP_ORDER_STATUS_ACTIVE = 2
    STOP_ORDER_STATUS_EXECUTED = 3
    STOP_ORDER_STATUS_CANCELED = 4
    STOP_ORDER_STATUS_EXPIRED = 5


class ExchangeOrderType(Enum):
    EXCHANGE_ORDER_TYPE_UNSPECIFIED = 0
    EXCHANGE_ORDER_TYPE_MARKET = 1
    EXCHANGE_ORDER_TYPE_LIMIT = 2


class TakeProfitType(Enum):
    TAKE_PROFIT_TYPE_UNSPECIFIED = 0
    TAKE_PROFIT_TYPE_REGULAR = 1
    TAKE_PROFIT_TYPE_TRAILING = 2


class TrailingValueType(Enum):
    TRAILING_VALUE_UNSPECIFIED = 0
    TRAILING_VALUE_ABSOLUTE = 1
    TRAILING_VALUE_RELATIVE = 2


class TrailingStopStatus(Enum):
    TRAILING_STOP_UNSPECIFIED = 0
    TRAILING_STOP_ACTIVE = 1
    TRAILING_STOP_ACTIVATED = 2


class PriceType(Enum):
    PRICE_TYPE_UNSPECIFIED = 0
    PRICE_TYPE_POINT = 1
    PRICE_TYPE_CURRENCY = 2


class TimeInForceType(Enum):
    TIME_IN_FORCE_UNSPECIFIED = 0
    TIME_IN_FORCE_DAY = 1
    TIME_IN_FORCE_FILL_AND_KILL = 2
    TIME_IN_FORCE_FILL_OR_KILL = 3


class OrderIdType(Enum):
    ORDER_ID_TYPE_UNSPECIFIED = 0
    ORDER_ID_TYPE_EXCHANGE = 1
    ORDER_ID_TYPE_REQUEST = 2


class EventType(Enum):
    EVENT_TYPE_UNSPECIFIED = 0
    EVENT_TYPE_CPN = 1
    EVENT_TYPE_CALL = 2
    EVENT_TYPE_MTY = 3
    EVENT_TYPE_CONV = 4


class AssetReportPeriodType(Enum):
    PERIOD_TYPE_UNSPECIFIED = 0
    PERIOD_TYPE_QUARTER = 1
    PERIOD_TYPE_SEMIANNUAL = 2
    PERIOD_TYPE_ANNUAL = 3


class Recommendation(Enum):
    RECOMMENDATION_UNSPECIFIED = 0
    RECOMMENDATION_BUY = 1
    RECOMMENDATION_HOLD = 2
    RECOMMENDATION_SELL = 3


class OrderBookType(Enum):
    ORDERBOOK_TYPE_UNSPECIFIED = 0
    ORDERBOOK_TYPE_EXCHANGE = 1
    ORDERBOOK_TYPE_DEALER = 2


class BondType(Enum):
    BOND_TYPE_UNSPECIFIED = 0
    BOND_TYPE_REPLACED = 1


class InstrumentExchangeType(Enum):
    INSTRUMENT_EXCHANGE_UNSPECIFIED = 0
    INSTRUMENT_EXCHANGE_DEALER = 1


class TradeSourceType(Enum):
    TRADE_SOURCE_UNSPECIFIED = 0
    TRADE_SOURCE_EXCHANGE = 1
    TRADE_SOURCE_DEALER = 2
    TRADE_SOURCE_ALL = 3


class ResultSubscriptionStatus(Enum):
    RESULT_SUBSCRIPTION_STATUS_UNSPECIFIED = 0
    RESULT_SUBSCRIPTION_STATUS_OK = 1
    RESULT_SUBSCRIPTION_STATUS_ERROR = 13


class MarkerType(Enum):
    MARKER_UNKNOWN = 0
    MARKER_BROKER = 1
    MARKER_CHAT = 2
    MARKER_PAPER = 3
    MARKER_MARGIN = 4
    MARKER_TKBNM = 5
    MARKER_SHORT = 6
    MARKER_SPECMM = 7
    MARKER_PO = 8


class StatusCauseInfo(Enum):
    CAUSE_UNSPECIFIED = 0
    CAUSE_CANCELLED_BY_CLIENT = 15
    CAUSE_CANCELLED_BY_EXCHANGE = 1
    CAUSE_CANCELLED_NOT_ENOUGH_POSITION = 2
    CAUSE_CANCELLED_BY_CLIENT_BLOCK = 3
    CAUSE_REJECTED_BY_BROKER = 4
    CAUSE_REJECTED_BY_EXCHANGE = 5
    CAUSE_CANCELLED_BY_BROKER = 6


class LastPriceType(Enum):
    LAST_PRICE_UNSPECIFIED = 0
    LAST_PRICE_EXCHANGE = 1
    LAST_PRICE_DEALER = 2


@dataclass(eq=False, repr=True)
class MoneyValue:
    currency: str 
    units: int
    nano: int


@dataclass(eq=False, repr=True)
class Quotation(SupportsAbs):
    units: int
    nano: int

    def __init__(self, units: int, nano: int):
        max_quotation_nano = 1_000_000_000
        self.units = units + nano // max_quotation_nano
        self.nano = nano % max_quotation_nano

    def __add__(self, other: "Quotation") -> "Quotation":
        return Quotation(
            units=self.units + other.units,
            nano=self.nano + other.nano,
        )

    def __sub__(self, other: "Quotation") -> "Quotation":
        return Quotation(
            units=self.units - other.units,
            nano=self.nano - other.nano,
        )

    def __hash__(self) -> int:
        return hash((self.units, self.nano))

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Quotation):
            return NotImplemented
        return self.units == other.units and self.nano == other.nano

    def __lt__(self, other: "Quotation") -> bool:
        return self.units < other.units or (
            self.units == other.units and self.nano < other.nano
        )

    def __le__(self, other: "Quotation") -> bool:
        return self.units < other.units or (
            self.units == other.units and self.nano <= other.nano
        )

    def __gt__(self, other: "Quotation") -> bool:
        return self.units > other.units or (
            self.units == other.units and self.nano > other.nano
        )

    def __ge__(self, other: "Quotation") -> bool:
        return self.units > other.units or (
            self.units == other.units and self.nano >= other.nano
        )

    def __abs__(self) -> "Quotation":
        return Quotation(units=abs(self.units), nano=abs(self.nano))


@dataclass(eq=False, repr=True)
class Ping:
    time: datetime
    stream_id: str 


@dataclass(eq=False, repr=True)
class TradingSchedulesRequest:
    exchange: Optional[str] 
    from_: Optional[datetime]
    to: Optional[datetime]


@dataclass(eq=False, repr=True)
class TradingSchedulesResponse:
    exchanges: List["TradingSchedule"]


@dataclass(eq=False, repr=True)
class TradingSchedule:
    exchange: str 
    days: List["TradingDay"]


@dataclass(eq=False, repr=True)
class TradingDay:  # pylint:disable=too-many-instance-attributes
    date: datetime
    is_trading_day: bool
    start_time: datetime
    end_time: datetime
    # reserved 5,6
    opening_auction_start_time: datetime
    closing_auction_end_time: datetime
    evening_opening_auction_start_time: datetime
    evening_start_time: datetime
    evening_end_time: datetime
    clearing_start_time: datetime
    clearing_end_time: datetime
    premarket_start_time: datetime
    premarket_end_time: datetime
    closing_auction_start_time: datetime
    opening_auction_end_time: datetime
    intervals: List["TradingInterval"]


@dataclass(eq=False, repr=True)
class InstrumentRequest:
    id_type: "InstrumentIdType"
    class_code: Optional[str] 
    id: str 


@dataclass(eq=False, repr=True)
class InstrumentsRequest:
    instrument_status: Optional["InstrumentStatus"]
    instrument_exchange: Optional["InstrumentExchangeType"]


@dataclass(eq=False, repr=True)
class FilterOptionsRequest:
    basic_asset_uid: Optional[str] 
    basic_asset_position_uid: Optional[str] 


@dataclass(eq=False, repr=True)
class BondResponse:
    instrument: "Bond"


@dataclass(eq=False, repr=True)
class BondsResponse:
    instruments: List["Bond"]


@dataclass(eq=False, repr=True)
class GetBondCouponsRequest:
    figi: str 
    from_: Optional[datetime]
    to: Optional[datetime]
    instrument_id: str 


@dataclass(eq=False, repr=True)
class GetBondCouponsResponse:
    events: List["Coupon"]


@dataclass(eq=False, repr=True)
class GetBondEventsRequest:
    from_: Optional[datetime]
    to: Optional[datetime]
    instrument_id: str 
    type: "EventType"


@dataclass(eq=False, repr=True)
class BondEvent:
    instrument_id: str 
    event_number: int
    event_date: datetime
    event_type: "EventType"
    event_total_vol: "Quotation"
    fix_date: datetime
    rate_date: datetime
    default_date: datetime
    real_pay_date: datetime
    pay_date: datetime
    pay_one_bond: "MoneyValue"
    money_flow_val: "MoneyValue"
    execution: str
    operation_type: str
    value: "Quotation"
    note: str
    convert_to_fin_tool_id: str
    coupon_start_date: datetime
    coupon_end_date: datetime
    coupon_period: int
    coupon_interest_rate: "Quotation"


@dataclass(eq=False, repr=True)
class GetBondEventsResponse:
    events: List["BondEvent"]


@dataclass(eq=False, repr=True)
class Coupon:
    figi: str 
    coupon_date: datetime
    coupon_number: int
    fix_date: datetime
    pay_one_bond: "MoneyValue"
    coupon_type: "CouponType"
    coupon_start_date: datetime
    coupon_end_date: datetime
    coupon_period: int


@dataclass(eq=False, repr=True)
class CurrencyResponse:
    instrument: "Currency"


@dataclass(eq=False, repr=True)
class CurrenciesResponse:
    instruments: List["Currency"]


@dataclass(eq=False, repr=True)
class EtfResponse:
    instrument: "Etf"


@dataclass(eq=False, repr=True)
class EtfsResponse:
    instruments: List["Etf"]


@dataclass(eq=False, repr=True)
class FutureResponse:
    instrument: "Future"


@dataclass(eq=False, repr=True)
class FuturesResponse:
    instruments: List["Future"]


@dataclass(eq=False, repr=True)
class OptionResponse:
    instrument: "Option"


@dataclass(eq=False, repr=True)
class OptionsResponse:
    instruments: List["Option"]


@dataclass(eq=False, repr=True)
class Option:
    uid: str 
    position_uid: str 
    ticker: str 
    class_code: str 
    basic_asset_position_uid: str 

    trading_status: "SecurityTradingStatus"
    real_exchange: "RealExchange"
    direction: "OptionDirection"
    payment_type: "OptionPaymentType"
    style: "OptionStyle"
    settlement_type: "OptionSettlementType"

    name: str
    currency: str
    settlement_currency: str
    asset_type: str
    basic_asset: str
    exchange: str
    country_of_risk: str
    country_of_risk_name: str
    sector: str
    brand: "BrandData"

    lot: int
    basic_asset_size: "Quotation"
    klong: "Quotation"
    kshort: "Quotation"
    dlong: "Quotation"
    dshort: "Quotation"
    dlong_min: "Quotation"
    dshort_min: "Quotation"
    min_price_increment: "Quotation"
    strike_price: "MoneyValue"

    expiration_date: datetime
    first_trade_date: datetime
    last_trade_date: datetime
    first_1min_candle_date: datetime
    first_1day_candle_date: datetime

    short_enabled_flag: bool
    for_iis_flag: bool
    otc_flag: bool
    buy_available_flag: bool
    sell_available_flag: bool
    for_qual_investor_flag: bool
    weekend_flag: bool
    blocked_tca_flag: bool
    api_trade_available_flag: bool


@dataclass(eq=False, repr=True)
class ShareResponse:
    instrument: "Share"


@dataclass(eq=False, repr=True)
class SharesResponse:
    instruments: List["Share"]


@dataclass(eq=False, repr=True)
class Bond:  # pylint:disable=too-many-instance-attributes
    figi: str 
    ticker: str 
    class_code: str 
    isin: str 
    lot: int
    currency: str
    klong: "Quotation"
    kshort: "Quotation"
    dlong: "Quotation"
    dshort: "Quotation"
    dlong_min: "Quotation"
    dshort_min: "Quotation"
    short_enabled_flag: bool
    name: str
    exchange: str
    coupon_quantity_per_year: int
    maturity_date: datetime
    nominal: "MoneyValue"
    initial_nominal: "MoneyValue"
    state_reg_date: datetime
    placement_date: datetime
    placement_price: "MoneyValue"
    aci_value: "MoneyValue"
    country_of_risk: str
    country_of_risk_name: str
    sector: str
    issue_kind: str
    issue_size: int
    issue_size_plan: int
    trading_status: "SecurityTradingStatus"
    otc_flag: bool
    buy_available_flag: bool
    sell_available_flag: bool
    floating_coupon_flag: bool
    perpetual_flag: bool
    amortization_flag: bool
    min_price_increment: "Quotation"
    api_trade_available_flag: bool
    uid: str
    real_exchange: "RealExchange"
    position_uid: str
    asset_uid: str
    for_iis_flag: bool
    for_qual_investor_flag: bool
    weekend_flag: bool
    blocked_tca_flag: bool
    subordinated_flag: bool
    liquidity_flag: bool
    first_1min_candle_date: datetime
    first_1day_candle_date: datetime
    risk_level: "RiskLevel"
    brand: "BrandData"
    bond_type: "BondType"


@dataclass(eq=False, repr=True)
class Currency:  # pylint:disable=too-many-instance-attributes
    figi: str 
    ticker: str 
    class_code: str 
    isin: str 
    lot: int
    currency: str
    klong: "Quotation"
    kshort: "Quotation"
    dlong: "Quotation"
    dshort: "Quotation"
    dlong_min: "Quotation"
    dshort_min: "Quotation"
    short_enabled_flag: bool
    name: str
    exchange: str
    nominal: "MoneyValue"
    country_of_risk: str
    country_of_risk_name: str
    trading_status: "SecurityTradingStatus"
    otc_flag: bool
    buy_available_flag: bool
    sell_available_flag: bool
    iso_currency_name: str
    min_price_increment: "Quotation"
    api_trade_available_flag: bool
    uid: str
    real_exchange: "RealExchange"
    position_uid: str
    for_iis_flag: bool
    for_qual_investor_flag: bool
    weekend_flag: bool
    blocked_tca_flag: bool
    first_1min_candle_date: datetime
    first_1day_candle_date: datetime
    brand: "BrandData"


@dataclass(eq=False, repr=True)
class Etf:  # pylint:disable=too-many-instance-attributes
    figi: str 
    ticker: str 
    class_code: str 
    isin: str 
    lot: int
    currency: str
    klong: "Quotation"
    kshort: "Quotation"
    dlong: "Quotation"
    dshort: "Quotation"
    dlong_min: "Quotation"
    dshort_min: "Quotation"
    short_enabled_flag: bool
    name: str
    exchange: str
    fixed_commission: "Quotation"
    focus_type: str
    released_date: datetime
    num_shares: "Quotation"
    country_of_risk: str
    country_of_risk_name: str
    sector: str
    rebalancing_freq: str
    trading_status: "SecurityTradingStatus"
    otc_flag: bool
    buy_available_flag: bool
    sell_available_flag: bool
    min_price_increment: "Quotation"
    api_trade_available_flag: bool
    uid: str
    real_exchange: "RealExchange"
    position_uid: str
    asset_uid: str
    instrument_exchange: "InstrumentExchangeType"
    for_iis_flag: bool
    for_qual_investor_flag: bool
    weekend_flag: bool
    blocked_tca_flag: bool
    liquidity_flag: bool
    first_1min_candle_date: datetime
    first_1day_candle_date: datetime
    brand: "BrandData"


@dataclass(eq=False, repr=True)
class Future:  # pylint:disable=too-many-instance-attributes
    figi: str 
    ticker: str 
    class_code: str 
    lot: int
    currency: str 
    klong: "Quotation"
    kshort: "Quotation"
    dlong: "Quotation"
    dshort: "Quotation"
    dlong_min: "Quotation"
    dshort_min: "Quotation"
    short_enabled_flag: bool
    name: str
    exchange: str
    first_trade_date: datetime
    last_trade_date: datetime
    futures_type: str
    asset_type: str
    basic_asset: str
    basic_asset_size: "Quotation"
    country_of_risk: str
    country_of_risk_name: str
    sector: str
    expiration_date: datetime
    trading_status: "SecurityTradingStatus"
    otc_flag: bool
    buy_available_flag: bool
    sell_available_flag: bool
    min_price_increment: "Quotation"
    api_trade_available_flag: bool
    uid: str
    real_exchange: "RealExchange"
    position_uid: str
    basic_asset_position_uid: str
    for_iis_flag: bool
    for_qual_investor_flag: bool
    weekend_flag: bool
    blocked_tca_flag: bool
    first_1min_candle_date: datetime
    first_1day_candle_date: datetime
    initial_margin_on_buy: "MoneyValue"
    initial_margin_on_sell: "MoneyValue"
    min_price_increment_amount: "Quotation"
    brand: "BrandData"


@dataclass(eq=False, repr=True)
class Share:  # pylint:disable=too-many-instance-attributes
    figi: str 
    ticker: str 
    class_code: str 
    isin: str 
    lot: int
    currency: str
    klong: "Quotation"
    kshort: "Quotation"
    dlong: "Quotation"
    dshort: "Quotation"
    dlong_min: "Quotation"
    dshort_min: "Quotation"
    short_enabled_flag: bool
    name: str
    exchange: str
    ipo_date: datetime
    issue_size: int
    country_of_risk: str
    country_of_risk_name: str
    sector: str
    issue_size_plan: int
    nominal: "MoneyValue"
    trading_status: "SecurityTradingStatus"
    otc_flag: bool
    buy_available_flag: bool
    sell_available_flag: bool
    div_yield_flag: bool
    share_type: "ShareType"
    min_price_increment: "Quotation"
    api_trade_available_flag: bool
    uid: str
    real_exchange: "RealExchange"
    position_uid: str
    asset_uid: str
    instrument_exchange: "InstrumentExchangeType"
    for_iis_flag: bool
    for_qual_investor_flag: bool
    weekend_flag: bool
    blocked_tca_flag: bool
    liquidity_flag: bool
    first_1min_candle_date: datetime
    first_1day_candle_date: datetime
    brand: "BrandData"


@dataclass(eq=False, repr=True)
class GetAccruedInterestsRequest:
    figi: str 
    from_: datetime
    to: datetime
    instrument_id: str 


@dataclass(eq=False, repr=True)
class GetAccruedInterestsResponse:
    accrued_interests: List["AccruedInterest"]


@dataclass(eq=False, repr=True)
class AccruedInterest:
    date: datetime
    value: "Quotation"
    value_percent: "Quotation"
    nominal: "Quotation"


@dataclass(eq=False, repr=True)
class GetFuturesMarginRequest:
    figi: str 
    instrument_id: str 


@dataclass(eq=False, repr=True)
class GetFuturesMarginResponse:
    initial_margin_on_buy: "MoneyValue"
    initial_margin_on_sell: "MoneyValue"
    min_price_increment: "Quotation"
    min_price_increment_amount: "Quotation"


@dataclass(eq=False, repr=True)
class InstrumentResponse:
    instrument: "Instrument"


@dataclass(eq=False, repr=True)
class Instrument:  # pylint:disable=too-many-instance-attributes
    figi: str 
    ticker: str 
    class_code: str 
    isin: str 
    lot: int
    currency: str
    klong: "Quotation"
    kshort: "Quotation"
    dlong: "Quotation"
    dshort: "Quotation"
    dlong_min: "Quotation"
    dshort_min: "Quotation"
    short_enabled_flag: bool
    name: str
    exchange: str
    country_of_risk: str
    country_of_risk_name: str
    instrument_type: str
    trading_status: "SecurityTradingStatus"
    otc_flag: bool
    buy_available_flag: bool
    sell_available_flag: bool
    min_price_increment: "Quotation"
    api_trade_available_flag: bool
    uid: str
    real_exchange: "RealExchange"
    position_uid: str
    asset_uid: str
    for_iis_flag: bool
    for_qual_investor_flag: bool
    weekend_flag: bool
    blocked_tca_flag: bool
    instrument_kind: "InstrumentType"
    first_1min_candle_date: datetime
    first_1day_candle_date: datetime
    brand: "BrandData"


@dataclass(eq=False, repr=True)
class GetDividendsRequest:
    figi: str 
    from_: Optional[datetime]
    to: Optional[datetime]
    instrument_id: str 


@dataclass(eq=False, repr=True)
class GetDividendsResponse:
    dividends: List["Dividend"]


@dataclass(eq=False, repr=True)
class Dividend:
    dividend_net: "MoneyValue"
    payment_date: datetime
    declared_date: datetime
    last_buy_date: datetime
    dividend_type: str 
    record_date: datetime
    regularity: str
    close_price: "MoneyValue"
    yield_value: "Quotation"
    created_at: datetime


@dataclass(eq=False, repr=True)
class AssetRequest:
    id: str 


@dataclass(eq=False, repr=True)
class AssetResponse:
    asset: "AssetFull"


@dataclass(eq=False, repr=True)
class AssetsRequest:
    instrument_type: Optional["InstrumentType"]


@dataclass(eq=False, repr=True)
class AssetsResponse:
    assets: List["Asset"]


@dataclass(eq=False, repr=True)
class AssetFull:
    uid: str 
    type: "AssetType"
    name: str 
    name_brief: str 
    description: str 
    deleted_at: datetime
    required_tests: List[str]
    currency: "AssetCurrency"
    security: "AssetSecurity"
    gos_reg_code: str
    cfi: str
    code_nsd: str
    status: str
    brand: "Brand"
    updated_at: datetime
    br_code: str
    br_code_name: str
    instruments: List["AssetInstrument"]


@dataclass(eq=False, repr=True)
class Asset:
    uid: str 
    type: "AssetType"
    name: str 
    instruments: List["AssetInstrument"]


@dataclass(eq=False, repr=True)
class AssetCurrency:
    base_currency: str 


@dataclass(eq=False, repr=True)
class AssetSecurity:
    isin: str 
    type: str 
    instrument_kind: "InstrumentType"
    share: "AssetShare"
    bond: "AssetBond"
    sp: "AssetStructuredProduct"
    etf: "AssetEtf"
    clearing_certificate: "AssetClearingCertificate"


@dataclass(eq=False, repr=True)
class AssetShare:
    type: "ShareType"
    issue_size: "Quotation"
    nominal: "Quotation"
    nominal_currency: str 
    primary_index: str 
    dividend_rate: "Quotation"
    preferred_share_type: str
    ipo_date: datetime
    registry_date: datetime
    div_yield_flag: bool
    issue_kind: str
    placement_date: datetime
    repres_isin: str
    issue_size_plan: "Quotation"
    total_float: "Quotation"


@dataclass(eq=False, repr=True)
class AssetBond:
    current_nominal: "Quotation"
    borrow_name: str 
    issue_size: "Quotation"
    nominal: "Quotation"
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
    maturity_date: datetime
    return_condition: str
    state_reg_date: datetime
    placement_date: datetime
    placement_price: "Quotation"
    issue_size_plan: "Quotation"


@dataclass(eq=False, repr=True)
class AssetStructuredProduct:
    borrow_name: str 
    nominal: "Quotation"
    nominal_currency: str 
    type: "StructuredProductType"
    logic_portfolio: str 
    asset_type: "AssetType"
    basic_asset: str
    safety_barrier: "Quotation"
    maturity_date: datetime
    issue_size_plan: "Quotation"
    issue_size: "Quotation"
    placement_date: datetime
    issue_kind: str


@dataclass(eq=False, repr=True)
class AssetEtf:
    total_expense: "Quotation"
    hurdle_rate: "Quotation"
    performance_fee: "Quotation"
    fixed_commission: "Quotation"
    payment_type: str 
    watermark_flag: bool
    buy_premium: "Quotation"
    sell_discount: "Quotation"
    rebalancing_flag: bool
    rebalancing_freq: str
    management_type: str
    primary_index: str
    focus_type: str
    leveraged_flag: bool
    num_share: "Quotation"
    ucits_flag: bool
    released_date: datetime
    description: str
    primary_index_description: str
    primary_index_company: str
    index_recovery_period: "Quotation"
    inav_code: str
    div_yield_flag: bool
    expense_commission: "Quotation"
    primary_index_tracking_error: "Quotation"
    rebalancing_plan: str
    tax_rate: str
    rebalancing_dates: List[datetime]
    issue_kind: str
    nominal: "Quotation"
    nominal_currency: str


@dataclass(eq=False, repr=True)
class AssetClearingCertificate:
    nominal: "Quotation"
    nominal_currency: str 


@dataclass(eq=False, repr=True)
class Brand:
    uid: str 
    name: str 
    description: str 
    info: str 
    company: str 
    sector: str
    country_of_risk: str
    country_of_risk_name: str


@dataclass(eq=False, repr=True)
class AssetInstrument:
    uid: str 
    figi: str 
    instrument_type: str 
    ticker: str 
    class_code: str 
    links: List["InstrumentLink"]
    instrument_kind: "InstrumentType"
    position_uid: str


@dataclass(eq=False, repr=True)
class InstrumentLink:
    type: str 
    instrument_uid: str 


@dataclass(eq=False, repr=True)
class GetFavoritesRequest:
    pass


@dataclass(eq=False, repr=True)
class GetFavoritesResponse:
    favorite_instruments: List["FavoriteInstrument"]


@dataclass(eq=False, repr=True)
class FavoriteInstrument:
    figi: str 
    ticker: str 
    class_code: str 
    isin: str 
    instrument_type: str
    name: str
    uid: str
    otc_flag: bool
    api_trade_available_flag: bool
    instrument_kind: "InstrumentType"


@dataclass(eq=False, repr=True)
class EditFavoritesRequest:
    instruments: List["EditFavoritesRequestInstrument"]
    action_type: "EditFavoritesActionType"


@dataclass(eq=False, repr=True)
class EditFavoritesRequestInstrument:
    figi: Optional[str] 
    instrument_id: str 


@dataclass(eq=False, repr=True)
class EditFavoritesResponse:
    favorite_instruments: List["FavoriteInstrument"]


@dataclass(eq=False, repr=True)
class GetCountriesRequest:
    pass


@dataclass(eq=False, repr=True)
class GetCountriesResponse:
    countries: List["CountryResponse"]


@dataclass(eq=False, repr=True)
class IndicativesRequest:
    pass


@dataclass(eq=False, repr=True)
class IndicativeResponse:
    figi: str 
    ticker: str 
    class_code: str 
    currency: str 
    instrument_kind: "InstrumentType"
    name: str
    exchange: str
    uid: str
    buy_available_flag: bool
    sell_available_flag: bool


@dataclass(eq=False, repr=True)
class IndicativesResponse:
    instruments: List["IndicativeResponse"]


@dataclass(eq=False, repr=True)
class CountryResponse:
    alfa_two: str 
    alfa_three: str 
    name: str 
    name_brief: str 


@dataclass(eq=False, repr=True)
class FindInstrumentRequest:
    query: str 
    instrument_kind: Optional["InstrumentType"]
    api_trade_available_flag: Optional[bool]


@dataclass(eq=False, repr=True)
class FindInstrumentResponse:
    instruments: List["InstrumentShort"]


@dataclass(eq=False, repr=True)
class InstrumentShort:
    isin: str 
    figi: str 
    ticker: str 
    class_code: str 
    instrument_type: str 
    name: str
    uid: str
    position_uid: str
    instrument_kind: "InstrumentType"
    api_trade_available_flag: str
    for_iis_flag: bool
    first_1min_candle_date: datetime
    first_1day_candle_date: datetime
    for_qual_investor_flag: bool
    weekend_flag: bool
    blocked_tca_flag: bool


@dataclass(eq=False, repr=True)
class GetBrandsRequest:
    paging: "Page"


@dataclass(eq=False, repr=True)
class GetBrandRequest:
    id: str 


@dataclass(eq=False, repr=True)
class GetBrandsResponse:
    brands: List["Brand"]
    paging: "PageResponse"


@dataclass(eq=False, repr=True)
class MarketDataRequest:
    subscribe_candles_request: "SubscribeCandlesRequest"
    subscribe_order_book_request: "SubscribeOrderBookRequest"
    subscribe_trades_request: "SubscribeTradesRequest"
    subscribe_info_request: "SubscribeInfoRequest"
    subscribe_last_price_request: "SubscribeLastPriceRequest" 
    get_my_subscriptions: "GetMySubscriptions"


@dataclass(eq=False, repr=True)
class MarketDataServerSideStreamRequest:
    subscribe_candles_request: "SubscribeCandlesRequest"
    subscribe_order_book_request: "SubscribeOrderBookRequest"
    subscribe_trades_request: "SubscribeTradesRequest"
    subscribe_info_request: "SubscribeInfoRequest"
    subscribe_last_price_request: "SubscribeLastPriceRequest"


@dataclass(eq=False, repr=True)
class MarketDataResponse:  # pylint:disable=too-many-instance-attributes
    subscribe_candles_response: "SubscribeCandlesResponse"
    subscribe_order_book_response: "SubscribeOrderBookResponse"
    subscribe_trades_response: "SubscribeTradesResponse"
    subscribe_info_response: "SubscribeInfoResponse"
    candle: "Candle"
    trade: "Trade"
    orderbook: "OrderBook"
    trading_status: "TradingStatus"
    ping: "Ping"
    subscribe_last_price_response: "SubscribeLastPriceResponse"
    last_price: "LastPrice"


@dataclass(eq=False, repr=True)
class SubscribeCandlesRequest:
    subscription_action: "SubscriptionAction"
    instruments: List["CandleInstrument"]
    waiting_close: bool


@dataclass(eq=False, repr=True)
class CandleInstrument:
    figi: str 
    interval: "SubscriptionInterval"
    instrument_id: str 


@dataclass(eq=False, repr=True)
class SubscribeCandlesResponse:
    tracking_id: str 
    candles_subscriptions: List["CandleSubscription"]


@dataclass(eq=False, repr=True)
class CandleSubscription:
    figi: str 
    interval: "SubscriptionInterval"
    subscription_status: "SubscriptionStatus"
    instrument_uid: str 
    waiting_close: bool
    stream_id: str
    subscription_id: str


@dataclass(eq=False, repr=True)
class SubscribeOrderBookRequest:
    subscription_action: "SubscriptionAction"
    instruments: List["OrderBookInstrument"]


@dataclass(eq=False, repr=True)
class OrderBookInstrument:
    figi: str 
    depth: int
    instrument_id: str 
    order_book_type: "OrderBookType"


@dataclass(eq=False, repr=True)
class SubscribeOrderBookResponse:
    tracking_id: str 
    order_book_subscriptions: List[
        "OrderBookSubscription"
    ]


@dataclass(eq=False, repr=True)
class OrderBookSubscription:
    figi: str 
    depth: int
    subscription_status: "SubscriptionStatus"
    instrument_uid: str 
    stream_id: str 
    subscription_id: str
    order_book_type: "OrderBookType"


@dataclass(eq=False, repr=True)
class SubscribeTradesRequest:
    subscription_action: "SubscriptionAction"
    instruments: List["TradeInstrument"]
    trade_type: "TradeSourceType"


@dataclass(eq=False, repr=True)
class SubscribeLastPriceRequest:
    subscription_action: "SubscriptionAction"
    instruments: List["LastPriceInstrument"]


@dataclass(eq=False, repr=True)
class LastPriceInstrument:
    figi: str 
    instrument_id: str 


@dataclass(eq=False, repr=True)
class SubscribeLastPriceResponse:
    tracking_id: str 
    last_price_subscriptions: List[
        "LastPriceSubscription"
    ]


@dataclass(eq=False, repr=True)
class LastPriceSubscription:
    figi: str 
    subscription_status: "SubscriptionStatus"
    instrument_uid: str 
    stream_id: str 
    subscription_id: str 


@dataclass(eq=False, repr=True)
class TradeInstrument:
    figi: str 
    instrument_id: str 


@dataclass(eq=False, repr=True)
class SubscribeTradesResponse:
    tracking_id: str 
    trade_subscriptions: List["TradeSubscription"]
    trade_type: "TradeSourceType"


@dataclass(eq=False, repr=True)
class TradeSubscription:
    figi: str 
    subscription_status: "SubscriptionStatus"
    instrument_uid: str 
    stream_id: str 
    subscription_id: str 


@dataclass(eq=False, repr=True)
class SubscribeInfoRequest:
    subscription_action: "SubscriptionAction"
    instruments: List["InfoInstrument"]


@dataclass(eq=False, repr=True)
class InfoInstrument:
    figi: str 
    instrument_id: str 


@dataclass(eq=False, repr=True)
class SubscribeInfoResponse:
    tracking_id: str 
    info_subscriptions: List["InfoSubscription"]


@dataclass(eq=False, repr=True)
class InfoSubscription:
    figi: str 
    subscription_status: "SubscriptionStatus"
    instrument_uid: str 
    stream_id: str 
    subscription_id: str 


@dataclass(eq=False, repr=True)
class Candle:
    figi: str 
    interval: "SubscriptionInterval"
    open: "Quotation"
    high: "Quotation"
    low: "Quotation"
    close: "Quotation"
    volume: int
    time: datetime
    last_trade_ts: datetime
    instrument_uid: str


@dataclass(eq=False, repr=True)
class OrderBook:
    figi: str 
    depth: int
    is_consistent: bool
    bids: List["Order"]
    asks: List["Order"]
    time: datetime
    limit_up: "Quotation"
    limit_down: "Quotation"
    instrument_uid: str
    order_book_type: "OrderBookType"


@dataclass(eq=False, repr=True)
class Order:
    price: "Quotation"
    quantity: int


@dataclass(eq=False, repr=True)
class Trade:
    figi: str 
    direction: "TradeDirection"
    price: "Quotation"
    quantity: int
    time: datetime
    instrument_uid: str
    tradeSource: TradeSourceType


@dataclass(eq=False, repr=True)
class TradingStatus:
    figi: str 
    trading_status: "SecurityTradingStatus"
    time: datetime
    limit_order_available_flag: bool
    market_order_available_flag: bool
    instrument_uid: str


@dataclass(eq=False, repr=True)
class GetCandlesRequest:
    figi: Optional[str] 
    from_: datetime
    to: datetime
    interval: "CandleInterval"
    instrument_id: Optional[str] 
    candle_source_type: Optional[CandleSource]
    limit: Optional[int]


@dataclass(eq=False, repr=True)
class GetCandlesResponse:
    candles: List["HistoricCandle"]


@dataclass(eq=True, repr=True, frozen=True)
class HistoricCandle:
    open: Quotation
    high: Quotation
    low: Quotation
    close: Quotation
    volume: int
    time: datetime
    is_complete: bool
    candle_source: CandleSource


@dataclass(eq=False, repr=True)
class GetLastPricesRequest:
    figi: List[str] 
    instrument_id: List[str] 
    last_price_type: LastPriceType


@dataclass(eq=False, repr=True)
class GetLastPricesResponse:
    last_prices: List["LastPrice"]


@dataclass(eq=False, repr=True)
class LastPrice:
    figi: str 
    price: "Quotation"
    time: datetime
    instrument_uid: str
    last_price_type: LastPriceType


@dataclass(eq=False, repr=True)
class GetOrderBookRequest:
    figi: Optional[str] 
    depth: int
    instrument_id: Optional[str] 


@dataclass(eq=False, repr=True)
class GetOrderBookResponse:
    figi: str 
    depth: int
    bids: List["Order"]
    asks: List["Order"]
    last_price: "Quotation"
    close_price: "Quotation"
    limit_up: "Quotation"
    limit_down: "Quotation"
    last_price_ts: datetime
    close_price_ts: datetime
    orderbook_ts: datetime
    instrument_uid: str


@dataclass(eq=False, repr=True)
class GetTradingStatusRequest:
    figi: Optional[str] 
    instrument_id: Optional[str] 


@dataclass(eq=False, repr=True)
class GetTradingStatusesRequest:
    instrument_id: List[str]


@dataclass(eq=False, repr=True)
class GetTradingStatusesResponse:
    trading_statuses: List["GetTradingStatusResponse"]


@dataclass(eq=False, repr=True)
class GetTradingStatusResponse:
    figi: str 
    trading_status: "SecurityTradingStatus"
    limit_order_available_flag: bool
    market_order_available_flag: bool
    api_trade_available_flag: bool
    instrument_uid: str

    bestprice_order_available_flag: bool
    only_best_price: bool


@dataclass(eq=False, repr=True)
class GetLastTradesRequest:
    figi: Optional[str] 
    from_: datetime
    to: datetime
    instrument_id: Optional[str] 


@dataclass(eq=False, repr=True)
class GetLastTradesResponse:
    trades: List["Trade"]


@dataclass(eq=False, repr=True)
class GetMySubscriptions:
    pass


@dataclass(eq=False, repr=True)
class GetClosePricesRequest:
    instruments: List["InstrumentClosePriceRequest"]


@dataclass(eq=False, repr=True)
class InstrumentClosePriceRequest:
    instrument_id: str 


@dataclass(eq=False, repr=True)
class GetClosePricesResponse:
    close_prices: List["InstrumentClosePriceResponse"]


@dataclass(eq=False, repr=True)
class InstrumentClosePriceResponse:
    figi: str 
    instrument_uid: str 
    price: "Quotation"
    evening_session_price: "Quotation"
    time: datetime


@dataclass(eq=False, repr=True)
class Smoothing:
    fast_length: int
    slow_length: int
    signal_smoothing: int


@dataclass(eq=False, repr=True)
class Deviation:
    deviation_multiplier: "Quotation"


class IndicatorInterval(Enum):
    INDICATOR_INTERVAL_UNSPECIFIED = 0
    INDICATOR_INTERVAL_ONE_MINUTE = 1
    INDICATOR_INTERVAL_FIVE_MINUTES = 2
    INDICATOR_INTERVAL_FIFTEEN_MINUTES = 3
    INDICATOR_INTERVAL_ONE_HOUR = 4
    INDICATOR_INTERVAL_ONE_DAY = 5
    INDICATOR_INTERVAL_2_MIN = 6
    INDICATOR_INTERVAL_3_MIN = 7
    INDICATOR_INTERVAL_10_MIN = 8
    INDICATOR_INTERVAL_30_MIN = 9
    INDICATOR_INTERVAL_2_HOUR = 10
    INDICATOR_INTERVAL_4_HOUR = 11
    INDICATOR_INTERVAL_WEEK = 12
    INDICATOR_INTERVAL_MONTH = 13


class TypeOfPrice(Enum):
    TYPE_OF_PRICE_UNSPECIFIED = 0
    TYPE_OF_PRICE_CLOSE = 1
    TYPE_OF_PRICE_OPEN = 2
    TYPE_OF_PRICE_HIGH = 3
    TYPE_OF_PRICE_LOW = 4
    TYPE_OF_PRICE_AVG = 5


class IndicatorType(Enum):
    INDICATOR_TYPE_UNSPECIFIED = 0
    INDICATOR_TYPE_BB = 1
    INDICATOR_TYPE_EMA = 2
    INDICATOR_TYPE_RSI = 3
    INDICATOR_TYPE_MACD = 4
    INDICATOR_TYPE_SMA = 5


@dataclass(eq=False, repr=True)
class GetTechAnalysisRequest:
    indicator_type: "IndicatorType"
    instrument_uid: str 
    from_: datetime
    to: datetime
    interval: "IndicatorInterval"
    type_of_price: "TypeOfPrice"
    length: int
    deviation: "Deviation"
    smoothing: "Smoothing"


@dataclass(eq=False, repr=True)
class TechAnalysisItem:
    timestamp: datetime
    middle_band: Optional["Quotation"]
    upper_band: Optional["Quotation"]
    lower_band: Optional["Quotation"]
    signal: Optional["Quotation"]
    macd: Optional["Quotation"]


@dataclass(eq=False, repr=True)
class GetTechAnalysisResponse:
    technical_indicators: List["TechAnalysisItem"]


@dataclass(eq=False, repr=True)
class OperationsRequest:
    account_id: str 
    from_: Optional[datetime]
    to: Optional[datetime]
    state: Optional["OperationState"]
    figi: Optional[str] 


@dataclass(eq=False, repr=True)
class OperationsResponse:
    operations: List["Operation"]


@dataclass(eq=False, repr=True)
class OperationTrade:
    trade_id: str 
    date_time: datetime
    quantity: int
    price: "MoneyValue"


@dataclass(eq=False, repr=True)
class ChildOperationItem:
    instrument_uid: str 
    payment: "MoneyValue"


@dataclass(eq=False, repr=True)
class Operation:  # pylint:disable=too-many-instance-attributes
    id: str 
    parent_operation_id: str 
    currency: str 
    payment: "MoneyValue"
    price: "MoneyValue"
    state: "OperationState"
    quantity: int
    quantity_rest: int
    figi: str
    instrument_type: str
    date: datetime
    type: str
    operation_type: "OperationType"
    trades: List["OperationTrade"]
    asset_uid: str
    position_uid: str
    instrument_uid: str
    child_operations: List["ChildOperationItem"]


class CurrencyRequest(Enum):
    RUB = 0
    USD = 1
    EUR = 2


@dataclass(eq=False, repr=True)
class PortfolioRequest:
    account_id: str 
    currency: Optional[CurrencyRequest]


@dataclass(eq=False, repr=True)
class VirtualPortfolioPosition:
    position_uid: str 
    instrument_uid: str 
    figi: str 
    instrument_type: str 
    quantity: "Quotation"
    average_position_price: "MoneyValue"
    expected_yield: "Quotation"
    expected_yield_fifo: "Quotation"
    expire_date: datetime
    current_price: "MoneyValue"
    average_position_price_fifo: "MoneyValue"


@dataclass(eq=False, repr=True)
class PortfolioResponse:
    total_amount_shares: "MoneyValue"
    total_amount_bonds: "MoneyValue"
    total_amount_etf: "MoneyValue"
    total_amount_currencies: "MoneyValue"
    total_amount_futures: "MoneyValue"
    expected_yield: "Quotation"
    positions: List["PortfolioPosition"]
    account_id: str

    total_amount_options: MoneyValue
    total_amount_sp: MoneyValue
    total_amount_portfolio: MoneyValue
    virtual_positions: List["VirtualPortfolioPosition"]


@dataclass(eq=False, repr=True)
class PositionsRequest:
    account_id: str 


@dataclass(eq=False, repr=True)
class PositionsResponse:
    money: List["MoneyValue"]
    blocked: List["MoneyValue"]
    securities: List["PositionsSecurities"]
    limits_loading_in_progress: bool
    futures: List["PositionsFutures"]
    options: List["PositionsOptions"]


@dataclass(eq=False, repr=True)
class WithdrawLimitsRequest:
    account_id: str 


@dataclass(eq=False, repr=True)
class WithdrawLimitsResponse:
    money: List["MoneyValue"]
    blocked: List["MoneyValue"]
    blocked_guarantee: List["MoneyValue"]


@dataclass(eq=False, repr=True)
class PortfolioPosition:
    figi: str 
    instrument_type: str 
    quantity: "Quotation"
    average_position_price: "MoneyValue"
    expected_yield: "Quotation"
    current_nkd: "MoneyValue"
    average_position_price_pt: "Quotation"
    current_price: "MoneyValue"
    average_position_price_fifo: "MoneyValue"
    quantity_lots: "Quotation"
    blocked: bool
    blocked_lots: "Quotation"
    position_uid: str
    instrument_uid: str
    var_margin: "MoneyValue"
    expected_yield_fifo: "Quotation"


@dataclass(eq=False, repr=True)
class PositionsSecurities:
    figi: str 
    blocked: int
    balance: int
    position_uid: str 
    instrument_uid: str 
    exchange_blocked: bool
    instrument_type: str


@dataclass(eq=False, repr=True)
class TradesStreamRequest:
    accounts: List[str] 


@dataclass(eq=False, repr=True)
class TradesStreamResponse:
    order_trades: "OrderTrades"
    ping: "Ping"
    subscription: "SubscriptionResponse"


@dataclass(eq=False, repr=True)
class OrderTrades:
    order_id: str 
    created_at: datetime
    direction: "OrderDirection"
    figi: str 
    trades: List["OrderTrade"]
    account_id: str
    instrument_uid: str


@dataclass(eq=False, repr=True)
class OrderTrade:
    date_time: datetime
    price: "Quotation"
    quantity: int
    trade_id: str 


@dataclass(eq=False, repr=True)
class PostOrderRequest:
    figi: Optional[str] 
    quantity: int
    price: Optional["Quotation"]
    direction: "OrderDirection"
    account_id: str 
    order_type: "OrderType"
    order_id: str
    instrument_id: str
    time_in_force: "TimeInForceType"
    price_type: "PriceType"


@dataclass(eq=False, repr=True)
class PostOrderResponse:
    order_id: str 
    execution_report_status: "OrderExecutionReportStatus"
    lots_requested: int
    lots_executed: int
    initial_order_price: "MoneyValue"
    executed_order_price: "MoneyValue"
    total_order_amount: "MoneyValue"
    initial_commission: "MoneyValue"
    executed_commission: "MoneyValue"
    aci_value: "MoneyValue"
    figi: str
    direction: "OrderDirection"
    initial_security_price: "MoneyValue"
    order_type: "OrderType"
    message: str
    initial_order_price_pt: "Quotation"
    instrument_uid: str
    order_request_id: str
    response_metadata: "ResponseMetadata"


@dataclass(eq=False, repr=True)
class PostOrderAsyncRequest:
    instrument_id: str 
    quantity: int
    price: "Quotation"
    direction: "OrderDirection"
    account_id: str 
    order_type: "OrderType"
    order_id: str
    time_in_force: TimeInForceType
    price_type: PriceType


@dataclass(eq=False, repr=True)
class PostOrderAsyncResponse:
    order_request_id: str 
    execution_report_status: "OrderExecutionReportStatus"
    trade_intent_id: str 


@dataclass(eq=False, repr=True)
class CancelOrderRequest:
    account_id: str 
    order_id: str 
    order_id_type: Optional["OrderIdType"]


@dataclass(eq=False, repr=True)
class CancelOrderResponse:
    time: datetime
    response_metadata: "ResponseMetadata"


@dataclass(eq=False, repr=True)
class GetOrderStateRequest:
    account_id: str 
    order_id: str 
    price_type: "PriceType"
    order_id_type: Optional["OrderIdType"]


@dataclass(eq=False, repr=True)
class GetOrdersRequest:
    account_id: str 


@dataclass(eq=False, repr=True)
class GetOrdersResponse:
    orders: List["OrderState"]


@dataclass(eq=False, repr=True)
class OrderState:  # pylint:disable=too-many-instance-attributes
    order_id: str 
    execution_report_status: "OrderExecutionReportStatus"
    lots_requested: int
    lots_executed: int
    initial_order_price: "MoneyValue"
    executed_order_price: "MoneyValue"
    total_order_amount: "MoneyValue"
    average_position_price: "MoneyValue"
    initial_commission: "MoneyValue"
    executed_commission: "MoneyValue"
    figi: str
    direction: "OrderDirection"
    initial_security_price: "MoneyValue"
    stages: List["OrderStage"]
    service_commission: "MoneyValue"
    currency: str
    order_type: "OrderType"
    order_date: datetime
    instrument_uid: str
    order_request_id: str


@dataclass(eq=False, repr=True)
class OrderStage:
    price: "MoneyValue"
    quantity: int
    trade_id: str 
    execution_time: datetime


class ReplaceOrderRequest:
    account_id: str 
    order_id: str
    idempotency_key: str
    quantity: int
    price: Optional["Quotation"]
    price_type: Optional["PriceType"]


@dataclass(eq=False, repr=True)
class GetAccountsRequest:
    status: Optional["AccountStatus"]


@dataclass(eq=False, repr=True)
class GetAccountsResponse:
    accounts: List["Account"]


@dataclass(eq=False, repr=True)
class Account:
    id: str 
    type: "AccountType"
    name: str 
    status: "AccountStatus"
    opened_date: datetime
    closed_date: datetime
    access_level: "AccessLevel"


@dataclass(eq=False, repr=True)
class GetMarginAttributesRequest:
    account_id: str 


@dataclass(eq=False, repr=True)
class GetMarginAttributesResponse:
    liquid_portfolio: "MoneyValue"
    starting_margin: "MoneyValue"
    minimal_margin: "MoneyValue"
    funds_sufficiency_level: "Quotation"
    amount_of_missing_funds: "MoneyValue"
    corrected_margin: "MoneyValue"


@dataclass(eq=False, repr=True)
class GetUserTariffRequest:
    pass


@dataclass(eq=False, repr=True)
class GetUserTariffResponse:
    unary_limits: List["UnaryLimit"]
    stream_limits: List["StreamLimit"]


@dataclass(eq=False, repr=True)
class UnaryLimit:
    limit_per_minute: int
    methods: List[str] 


@dataclass(eq=False, repr=True)
class StreamLimit:
    limit: int
    streams: List[str] 
    open: int


@dataclass(eq=False, repr=True)
class GetInfoRequest:
    pass


@dataclass(eq=False, repr=True)
class GetInfoResponse:
    prem_status: bool
    qual_status: bool
    qualified_for_work_with: List[str] 
    tariff: str 


@dataclass(eq=False, repr=True)
class OpenSandboxAccountRequest:
    name: Optional[str]


@dataclass(eq=False, repr=True)
class OpenSandboxAccountResponse:
    account_id: str 


@dataclass(eq=False, repr=True)
class CloseSandboxAccountRequest:
    account_id: str 


@dataclass(eq=False, repr=True)
class CloseSandboxAccountResponse:
    pass


@dataclass(eq=False, repr=True)
class SandboxPayInRequest:
    account_id: str 
    amount: "MoneyValue"


@dataclass(eq=False, repr=True)
class SandboxPayInResponse:
    balance: "MoneyValue"


@dataclass(eq=False, repr=True)
class PostStopOrderRequest:
    figi: Optional[str] 
    quantity: int
    price: Optional["Quotation"]
    stop_price: Optional["Quotation"]
    direction: "StopOrderDirection"
    account_id: str
    expiration_type: "StopOrderExpirationType"
    stop_order_type: "StopOrderType"
    expire_date: Optional[datetime]
    instrument_id: str
    exchange_order_type: "ExchangeOrderType"
    take_profit_type: "TakeProfitType"
    trailing_data: "PostStopOrderRequestTrailingData"
    price_type: "PriceType"
    order_id: str


@dataclass(eq=False, repr=True)
class PostStopOrderRequestTrailingData:
    indent: "Quotation"
    indent_type: "TrailingValueType"
    spread: "Quotation"
    spread_type: "TrailingValueType"


@dataclass(eq=False, repr=True)
class PostStopOrderResponse:
    stop_order_id: str 
    order_request_id: str 
    response_metadata: "ResponseMetadata"


@dataclass(eq=False, repr=True)
class GetStopOrdersRequest:
    account_id: str 
    status: "StopOrderStatusOption"
    from_: datetime
    to: datetime


@dataclass(eq=False, repr=True)
class GetStopOrdersResponse:
    stop_orders: List["StopOrder"]


@dataclass(eq=False, repr=True)
class CancelStopOrderRequest:
    account_id: str 
    stop_order_id: str 


@dataclass(eq=False, repr=True)
class CancelStopOrderResponse:
    time: datetime


@dataclass(eq=False, repr=True)
class StopOrder:  # pylint:disable=too-many-instance-attributes
    stop_order_id: str 
    lots_requested: int
    figi: str 
    direction: "StopOrderDirection"
    currency: str 
    order_type: "StopOrderType"
    create_date: datetime
    activation_date_time: datetime
    expiration_time: datetime
    price: "MoneyValue"
    stop_price: "MoneyValue"
    instrument_uid: str
    take_profit_type: "TakeProfitType"
    trailing_data: "StopOrderTrailingData"
    status: "StopOrderStatusOption"
    exchange_order_type: "ExchangeOrderType"
    exchange_order_id: Optional[str]


@dataclass(eq=False, repr=True)
class StopOrderTrailingData:
    indent: "Quotation"
    indent_type: "TrailingValueType"
    spread: "Quotation"
    spread_type: "TrailingValueType"
    status: "TrailingStopStatus"
    price: "Quotation"
    extr: "Quotation"


@dataclass(eq=False, repr=True)
class BrokerReportRequest:
    generate_broker_report_request: "GenerateBrokerReportRequest"
    get_broker_report_request: "GetBrokerReportRequest"


@dataclass(eq=False, repr=True)
class BrokerReportResponse:
    generate_broker_report_response: "GenerateBrokerReportResponse"
    get_broker_report_response: "GetBrokerReportResponse"


@dataclass(eq=False, repr=True)
class GenerateBrokerReportRequest:
    account_id: str 
    from_: datetime
    to: datetime


@dataclass(eq=False, repr=True)
class GenerateBrokerReportResponse:
    task_id: str 


@dataclass(eq=False, repr=True)
class GetBrokerReportRequest:
    task_id: str 
    page: Optional[int]


@dataclass(eq=False, repr=True)
class GetBrokerReportResponse:
    broker_report: List["BrokerReport"]
    itemsCount: int
    pagesCount: int
    page: int


@dataclass(eq=False, repr=True)
class BrokerReport:
    trade_id: str 
    order_id: str 
    figi: str 
    execute_sign: str 
    trade_datetime: datetime
    exchange: str
    class_code: str
    direction: str
    name: str
    ticker: str
    price: "MoneyValue"
    quantity: int
    order_amount: "MoneyValue"
    aci_value: float
    total_order_amount: "MoneyValue"
    broker_commission: "MoneyValue"
    exchange_commission: "MoneyValue"
    exchange_clearing_commission: "MoneyValue"
    repo_rate: float
    party: str
    clear_value_date: datetime
    sec_value_date: datetime
    broker_status: str
    separate_agreement_type: str
    separate_agreement_number: str
    separate_agreement_date: str
    delivery_type: str


@dataclass(eq=False, repr=True)
class PositionsFutures:
    figi: str 
    blocked: int
    balance: int
    position_uid: str 
    instrument_uid: str 


@dataclass(eq=False, repr=True)
class PositionsOptions:
    position_uid: str 
    instrument_uid: str 
    blocked: int
    balance: int


@dataclass(eq=False, repr=True)
class GetDividendsForeignIssuerRequest:
    generate_div_foreign_issuer_report: "GenerateDividendsForeignIssuerReportRequest"
    get_div_foreign_issuer_report: "GetDividendsForeignIssuerReportRequest"


@dataclass(eq=False, repr=True)
class GetDividendsForeignIssuerResponse:
    generate_div_foreign_issuer_report_response: "GenerateDividendsForeignIssuerReportResponse"
    div_foreign_issuer_report: "GetDividendsForeignIssuerReportResponse"


@dataclass(eq=False, repr=True)
class GenerateDividendsForeignIssuerReportRequest:
    account_id: str 
    from_: datetime
    to: datetime


@dataclass(eq=False, repr=True)
class GetDividendsForeignIssuerReportRequest:
    task_id: str 
    page: Optional[int]


@dataclass(eq=False, repr=True)
class GenerateDividendsForeignIssuerReportResponse:
    task_id: str 


@dataclass(eq=False, repr=True)
class GetDividendsForeignIssuerReportResponse:
    dividends_foreign_issuer_report: List[
        "DividendsForeignIssuerReport"
    ]
    itemsCount: int
    pagesCount: int
    page: int


@dataclass(eq=False, repr=True)
class DividendsForeignIssuerReport:
    record_date: datetime
    payment_date: datetime
    security_name: str 
    isin: str 
    issuer_country: str 
    quantity: int
    dividend: "Quotation"
    external_commission: "Quotation"
    dividend_gross: "Quotation"
    tax: "Quotation"
    dividend_amount: "Quotation"
    currency: str


@dataclass(eq=False, repr=True)
class PortfolioStreamRequest:
    accounts: List[str]


@dataclass(eq=False, repr=True)
class PortfolioStreamResponse:
    subscriptions: "PortfolioSubscriptionResult"
    portfolio: "PortfolioResponse"
    ping: "Ping"


@dataclass(eq=False, repr=True)
class PortfolioSubscriptionResult:
    accounts: List["AccountSubscriptionStatus"]
    tracking_id: str
    stream_id: str


@dataclass(eq=False, repr=True)
class AccountSubscriptionStatus:
    account_id: str 
    subscription_status: "PortfolioSubscriptionStatus"


@dataclass(eq=False, repr=True)
class GetOperationsByCursorRequest:
    account_id: str 
    instrument_id: Optional[str] 
    from_: Optional[datetime]
    to: Optional[datetime]
    cursor: Optional[str]
    limit: Optional[int]
    operation_types: List["OperationType"]
    state: Optional["OperationState"]
    without_commissions: Optional[bool]
    without_trades: Optional[bool]
    without_overnights: Optional[bool]


@dataclass(eq=False, repr=True)
class GetOperationsByCursorResponse:
    has_next: bool
    next_cursor: str 
    items: List["OperationItem"]


@dataclass(eq=False, repr=True)
class OperationItem:
    cursor: str 
    broker_account_id: str
    id: str
    parent_operation_id: str
    name: str
    date: datetime
    type: "OperationType"
    description: str
    state: "OperationState"
    instrument_uid: str
    figi: str
    instrument_type: str
    instrument_kind: "InstrumentType"
    position_uid: str
    payment: "MoneyValue"
    price: "MoneyValue"
    commission: "MoneyValue"
    yield_: "MoneyValue"
    yield_relative: "Quotation"
    accrued_int: "MoneyValue"
    quantity: int
    quantity_rest: int
    quantity_done: int
    cancel_date_time: datetime
    cancel_reason: str
    trades_info: "OperationItemTrades"
    asset_uid: str
    child_operations: List["ChildOperationItem"]


@dataclass(eq=False, repr=True)
class OperationItemTrades:
    trades: List["OperationItemTrade"]


@dataclass(eq=False, repr=True)
class OperationItemTrade:
    num: str 
    date: datetime
    quantity: int
    price: "MoneyValue"
    yield_: "MoneyValue"
    yield_relative: "Quotation"


@dataclass(eq=False, repr=True)
class PositionsStreamRequest:
    accounts: List[str] 


@dataclass(eq=False, repr=True)
class PositionsStreamResponse:
    subscriptions: "PositionsSubscriptionResult"
    position: "PositionData"
    ping: "Ping"


@dataclass(eq=False, repr=True)
class PositionsSubscriptionResult:
    accounts: List["PositionsSubscriptionStatus"]
    tracking_id: str
    stream_id: str


@dataclass(eq=False, repr=True)
class PositionsSubscriptionStatus:
    account_id: str 
    subscription_status: "PositionsAccountSubscriptionStatus"


@dataclass(eq=False, repr=True)
class PositionData:
    account_id: str 
    money: List["PositionsMoney"]
    securities: List["PositionsSecurities"]
    futures: List["PositionsFutures"]
    options: List["PositionsOptions"]
    date: datetime


@dataclass(eq=False, repr=True)
class PositionsMoney:
    available_value: "MoneyValue"
    blocked_value: "MoneyValue"


@dataclass(eq=False, repr=True)
class Page:
    limit: int
    page_number: int


@dataclass(eq=False, repr=True)
class PageResponse:
    limit: int
    page_number: int
    total_count: int


@dataclass(eq=False, repr=True)
class ResponseMetadata:
    tracking_id: str
    server_time: datetime


@dataclass(eq=False, repr=True)
class BrandData:
    logo_name: str 
    logo_base_color: str 
    text_color: str 


@dataclass(eq=False, repr=True)
class GetAssetFundamentalsRequest:
    assets: List[str]


@dataclass(eq=False, repr=True)
class GetAssetFundamentalsResponse:
    fundamentals: List["StatisticResponse"]


@dataclass(eq=False, repr=True)
class StatisticResponse:
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
    ex_dividend_date: datetime
    fiscal_period_start_date: datetime
    fiscal_period_end_date: datetime
    revenue_change_five_years: float
    eps_change_five_years: float
    ebitda_change_five_years: float
    total_debt_change_five_years: float
    ev_to_sales: float


@dataclass(eq=False, repr=True)
class GetAssetReportsRequest:
    instrument_id: str 
    from_: datetime
    to: datetime


@dataclass(eq=False, repr=True)
class GetAssetReportsEvent:
    instrument_id: str 
    report_date: datetime
    period_year: datetime
    period_num: datetime
    period_type: "AssetReportPeriodType"
    created_at: datetime


@dataclass(eq=False, repr=True)
class GetAssetReportsResponse:
    events: List["GetAssetReportsEvent"]


@dataclass(eq=False, repr=True)
class GetConsensusForecastsRequest:
    paging: Optional["Page"]


@dataclass(eq=False, repr=True)
class ConsensusForecastsItem:
    uid: str 
    asset_uid: str 
    created_at: datetime
    best_target_price: "Quotation"
    best_target_low: "Quotation"
    best_target_high: "Quotation"
    total_buy_recommend: int
    total_hold_recommend: int
    total_sell_recommend: int
    currency: str
    consensus: "Recommendation"
    prognosis_date: datetime


@dataclass(eq=False, repr=True)
class GetConsensusForecastsResponse:
    items: List["ConsensusForecastsItem"]
    page: "PageResponse"


@dataclass(eq=False, repr=True)
class GetForecastRequest:
    instrument_id: str 


@dataclass(eq=False, repr=True)
class TargetItem:
    uid: str 
    ticker: str 
    company: str 
    recommendation: "Recommendation"
    recommendation_date: datetime
    currency: str
    current_price: "Quotation"
    target_price: "Quotation"
    price_change: "Quotation"
    price_change_rel: "Quotation"
    show_name: str


@dataclass(eq=False, repr=True)
class ConsensusItem:
    uid: str 
    ticker: str 
    recommendation: "Recommendation"
    currency: str 
    current_price: "Quotation"
    consensus: "Quotation"
    min_target: "Quotation"
    max_target: "Quotation"
    price_change: "Quotation"
    price_change_rel: "Quotation"


@dataclass(eq=False, repr=True)
class GetForecastResponse:
    targets: List["TargetItem"]
    consensus: "ConsensusItem"


@dataclass(eq=False, repr=True)
class TimeInterval:
    start_ts: datetime
    end_ts: datetime


@dataclass(eq=False, repr=True)
class TradingInterval:
    type: str 
    interval: "TimeInterval"


@dataclass(eq=False, repr=True)
class GetMaxLotsRequest:
    account_id: str 
    instrument_id: str 
    price: Optional["Quotation"]


@dataclass(eq=False, repr=True)
class GetMaxLotsResponse:
    currency: str 
    buy_limits: "BuyLimitsView"
    buy_margin_limits: "BuyLimitsView"
    sell_limits: "SellLimitsView"
    sell_margin_limits: "SellLimitsView"


@dataclass(eq=False, repr=True)
class BuyLimitsView:
    buy_money_amount: "Quotation"
    buy_max_lots: int
    buy_max_market_lots: int


@dataclass(eq=False, repr=True)
class SellLimitsView:
    sell_max_lots: int


@dataclass(eq=False, repr=True)
class GetOrderPriceRequest:
    account_id: str 
    instrument_id: str 
    price: "Quotation"
    direction: "OrderDirection"
    quantity: int


@dataclass(eq=False, repr=True)
class GetOrderPriceResponse:
    total_order_amount: "MoneyValue"
    initial_order_amount: "MoneyValue"
    lots_requested: int
    executed_commission: "MoneyValue"
    executed_commission_rub: "MoneyValue"
    service_commission: "MoneyValue"
    deal_commission: "MoneyValue"
    extra_bond: "ExtraBond"
    extra_future: "ExtraFuture"


@dataclass(eq=False, repr=True)
class OrderStateStreamRequest:
    accounts: List[str]
    ping_delay_millis: Optional[int]


@dataclass(eq=False, repr=True)
class ErrorDetail:
    code: str 
    message: str 


@dataclass(eq=False, repr=True)
class SubscriptionResponse:
    tracking_id: str 
    status: ResultSubscriptionStatus
    stream_id: str
    accounts: List[str]
    error: Optional[ErrorDetail]


@dataclass(eq=False, repr=True)
class OrderStateStreamOrderState:
    order_id: str 
    order_request_id: Optional[str] 
    client_code: str 
    created_at: datetime
    execution_report_status: OrderExecutionReportStatus
    status_info: Optional[StatusCauseInfo]
    ticker: str
    class_code: str
    lot_size: int
    direction: OrderDirection
    time_in_force: TimeInForceType
    order_type: OrderType
    account_id: str
    initial_order_price: MoneyValue
    order_price: MoneyValue
    amount: Optional[MoneyValue]
    executed_order_price: MoneyValue
    currency: str
    lots_requested: int
    lots_executed: int
    lots_left: int
    lots_cancelled: int
    marker: Optional[MarkerType]
    trades: List[OrderTrade]
    completion_time: datetime
    exchange: str
    instrument_uid: str


@dataclass(eq=False, repr=True)
class OrderStateStreamResponse:
    order_state: "OrderStateStreamOrderState"
    ping: "Ping"
    subscription: "SubscriptionResponse"


@dataclass(eq=False, repr=True)
class ExtraBond:
    aci_value: "MoneyValue"
    nominal_conversion_rate: "Quotation"


@dataclass(eq=False, repr=True)
class ExtraFuture:
    initial_margin: "MoneyValue"