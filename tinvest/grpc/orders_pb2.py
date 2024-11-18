# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: tinvest/grpc/orders.proto
# Protobuf Python Version: 5.27.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    27,
    2,
    '',
    'tinvest/grpc/orders.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from tinvest.grpc import common_pb2 as tinvest_dot_grpc_dot_common__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from tinvest.grpc.google.api import field_behavior_pb2 as tinvest_dot_grpc_dot_google_dot_api_dot_field__behavior__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x19tinvest/grpc/orders.proto\x12%tinkoff.public.invest.api.contract.v1\x1a\x19tinvest/grpc/common.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a,tinvest/grpc/google/api/field_behavior.proto\"\'\n\x13TradesStreamRequest\x12\x10\n\x08\x61\x63\x63ounts\x18\x01 \x03(\t\"\xff\x01\n\x14TradesStreamResponse\x12J\n\x0corder_trades\x18\x01 \x01(\x0b\x32\x32.tinkoff.public.invest.api.contract.v1.OrderTradesH\x00\x12;\n\x04ping\x18\x02 \x01(\x0b\x32+.tinkoff.public.invest.api.contract.v1.PingH\x00\x12S\n\x0csubscription\x18\x03 \x01(\x0b\x32;.tinkoff.public.invest.api.contract.v1.SubscriptionResponseH\x00\x42\t\n\x07payload\"\x96\x02\n\x0bOrderTrades\x12\x10\n\x08order_id\x18\x01 \x01(\t\x12.\n\ncreated_at\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12H\n\tdirection\x18\x03 \x01(\x0e\x32\x35.tinkoff.public.invest.api.contract.v1.OrderDirection\x12\x0c\n\x04\x66igi\x18\x04 \x01(\t\x12\x41\n\x06trades\x18\x05 \x03(\x0b\x32\x31.tinkoff.public.invest.api.contract.v1.OrderTrade\x12\x12\n\naccount_id\x18\x06 \x01(\t\x12\x16\n\x0einstrument_uid\x18\x07 \x01(\t\"\xa0\x01\n\nOrderTrade\x12-\n\tdate_time\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12?\n\x05price\x18\x02 \x01(\x0b\x32\x30.tinkoff.public.invest.api.contract.v1.Quotation\x12\x10\n\x08quantity\x18\x03 \x01(\x03\x12\x10\n\x08trade_id\x18\x04 \x01(\t\"\x94\x04\n\x10PostOrderRequest\x12\x15\n\x04\x66igi\x18\x01 \x01(\tB\x02\x18\x01H\x00\x88\x01\x01\x12\x16\n\x08quantity\x18\x02 \x01(\x03\x42\x04\xe2\x41\x01\x02\x12\x44\n\x05price\x18\x03 \x01(\x0b\x32\x30.tinkoff.public.invest.api.contract.v1.QuotationH\x01\x88\x01\x01\x12N\n\tdirection\x18\x04 \x01(\x0e\x32\x35.tinkoff.public.invest.api.contract.v1.OrderDirectionB\x04\xe2\x41\x01\x02\x12\x18\n\naccount_id\x18\x05 \x01(\tB\x04\xe2\x41\x01\x02\x12J\n\norder_type\x18\x06 \x01(\x0e\x32\x30.tinkoff.public.invest.api.contract.v1.OrderTypeB\x04\xe2\x41\x01\x02\x12\x16\n\x08order_id\x18\x07 \x01(\tB\x04\xe2\x41\x01\x02\x12\x15\n\rinstrument_id\x18\x08 \x01(\t\x12M\n\rtime_in_force\x18\t \x01(\x0e\x32\x36.tinkoff.public.invest.api.contract.v1.TimeInForceType\x12\x44\n\nprice_type\x18\n \x01(\x0e\x32\x30.tinkoff.public.invest.api.contract.v1.PriceTypeB\x07\n\x05_figiB\x08\n\x06_price\"\xe8\x08\n\x11PostOrderResponse\x12\x10\n\x08order_id\x18\x01 \x01(\t\x12\x62\n\x17\x65xecution_report_status\x18\x02 \x01(\x0e\x32\x41.tinkoff.public.invest.api.contract.v1.OrderExecutionReportStatus\x12\x16\n\x0elots_requested\x18\x03 \x01(\x03\x12\x15\n\rlots_executed\x18\x04 \x01(\x03\x12N\n\x13initial_order_price\x18\x05 \x01(\x0b\x32\x31.tinkoff.public.invest.api.contract.v1.MoneyValue\x12O\n\x14\x65xecuted_order_price\x18\x06 \x01(\x0b\x32\x31.tinkoff.public.invest.api.contract.v1.MoneyValue\x12M\n\x12total_order_amount\x18\x07 \x01(\x0b\x32\x31.tinkoff.public.invest.api.contract.v1.MoneyValue\x12M\n\x12initial_commission\x18\x08 \x01(\x0b\x32\x31.tinkoff.public.invest.api.contract.v1.MoneyValue\x12N\n\x13\x65xecuted_commission\x18\t \x01(\x0b\x32\x31.tinkoff.public.invest.api.contract.v1.MoneyValue\x12\x44\n\taci_value\x18\n \x01(\x0b\x32\x31.tinkoff.public.invest.api.contract.v1.MoneyValue\x12\x0c\n\x04\x66igi\x18\x0b \x01(\t\x12H\n\tdirection\x18\x0c \x01(\x0e\x32\x35.tinkoff.public.invest.api.contract.v1.OrderDirection\x12Q\n\x16initial_security_price\x18\r \x01(\x0b\x32\x31.tinkoff.public.invest.api.contract.v1.MoneyValue\x12\x44\n\norder_type\x18\x0e \x01(\x0e\x32\x30.tinkoff.public.invest.api.contract.v1.OrderType\x12\x0f\n\x07message\x18\x0f \x01(\t\x12P\n\x16initial_order_price_pt\x18\x10 \x01(\x0b\x32\x30.tinkoff.public.invest.api.contract.v1.Quotation\x12\x16\n\x0einstrument_uid\x18\x11 \x01(\t\x12\x18\n\x10order_request_id\x18\x14 \x01(\t\x12S\n\x11response_metadata\x18\xfe\x01 \x01(\x0b\x32\x37.tinkoff.public.invest.api.contract.v1.ResponseMetadata\"\xaa\x04\n\x15PostOrderAsyncRequest\x12\x1b\n\rinstrument_id\x18\x01 \x01(\tB\x04\xe2\x41\x01\x02\x12\x16\n\x08quantity\x18\x02 \x01(\x03\x42\x04\xe2\x41\x01\x02\x12\x44\n\x05price\x18\x03 \x01(\x0b\x32\x30.tinkoff.public.invest.api.contract.v1.QuotationH\x00\x88\x01\x01\x12N\n\tdirection\x18\x04 \x01(\x0e\x32\x35.tinkoff.public.invest.api.contract.v1.OrderDirectionB\x04\xe2\x41\x01\x02\x12\x18\n\naccount_id\x18\x05 \x01(\tB\x04\xe2\x41\x01\x02\x12J\n\norder_type\x18\x06 \x01(\x0e\x32\x30.tinkoff.public.invest.api.contract.v1.OrderTypeB\x04\xe2\x41\x01\x02\x12\x16\n\x08order_id\x18\x07 \x01(\tB\x04\xe2\x41\x01\x02\x12R\n\rtime_in_force\x18\x08 \x01(\x0e\x32\x36.tinkoff.public.invest.api.contract.v1.TimeInForceTypeH\x01\x88\x01\x01\x12I\n\nprice_type\x18\t \x01(\x0e\x32\x30.tinkoff.public.invest.api.contract.v1.PriceTypeH\x02\x88\x01\x01\x42\x08\n\x06_priceB\x10\n\x0e_time_in_forceB\r\n\x0b_price_type\"\xd4\x01\n\x16PostOrderAsyncResponse\x12\x1e\n\x10order_request_id\x18\x01 \x01(\tB\x04\xe2\x41\x01\x02\x12h\n\x17\x65xecution_report_status\x18\x02 \x01(\x0e\x32\x41.tinkoff.public.invest.api.contract.v1.OrderExecutionReportStatusB\x04\xe2\x41\x01\x02\x12\x1c\n\x0ftrade_intent_id\x18\x03 \x01(\tH\x00\x88\x01\x01\x42\x12\n\x10_trade_intent_id\"\xa8\x01\n\x12\x43\x61ncelOrderRequest\x12\x18\n\naccount_id\x18\x01 \x01(\tB\x04\xe2\x41\x01\x02\x12\x16\n\x08order_id\x18\x02 \x01(\tB\x04\xe2\x41\x01\x02\x12N\n\rorder_id_type\x18\x03 \x01(\x0e\x32\x32.tinkoff.public.invest.api.contract.v1.OrderIdTypeH\x00\x88\x01\x01\x42\x10\n\x0e_order_id_type\"\x94\x01\n\x13\x43\x61ncelOrderResponse\x12(\n\x04time\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12S\n\x11response_metadata\x18\xfe\x01 \x01(\x0b\x32\x37.tinkoff.public.invest.api.contract.v1.ResponseMetadata\"\xf0\x01\n\x14GetOrderStateRequest\x12\x18\n\naccount_id\x18\x01 \x01(\tB\x04\xe2\x41\x01\x02\x12\x16\n\x08order_id\x18\x02 \x01(\tB\x04\xe2\x41\x01\x02\x12\x44\n\nprice_type\x18\x03 \x01(\x0e\x32\x30.tinkoff.public.invest.api.contract.v1.PriceType\x12N\n\rorder_id_type\x18\x04 \x01(\x0e\x32\x32.tinkoff.public.invest.api.contract.v1.OrderIdTypeH\x00\x88\x01\x01\x42\x10\n\x0e_order_id_type\",\n\x10GetOrdersRequest\x12\x18\n\naccount_id\x18\x01 \x01(\tB\x04\xe2\x41\x01\x02\"V\n\x11GetOrdersResponse\x12\x41\n\x06orders\x18\x01 \x03(\x0b\x32\x31.tinkoff.public.invest.api.contract.v1.OrderState\"\x8a\t\n\nOrderState\x12\x10\n\x08order_id\x18\x01 \x01(\t\x12\x62\n\x17\x65xecution_report_status\x18\x02 \x01(\x0e\x32\x41.tinkoff.public.invest.api.contract.v1.OrderExecutionReportStatus\x12\x16\n\x0elots_requested\x18\x03 \x01(\x03\x12\x15\n\rlots_executed\x18\x04 \x01(\x03\x12N\n\x13initial_order_price\x18\x05 \x01(\x0b\x32\x31.tinkoff.public.invest.api.contract.v1.MoneyValue\x12O\n\x14\x65xecuted_order_price\x18\x06 \x01(\x0b\x32\x31.tinkoff.public.invest.api.contract.v1.MoneyValue\x12M\n\x12total_order_amount\x18\x07 \x01(\x0b\x32\x31.tinkoff.public.invest.api.contract.v1.MoneyValue\x12Q\n\x16\x61verage_position_price\x18\x08 \x01(\x0b\x32\x31.tinkoff.public.invest.api.contract.v1.MoneyValue\x12M\n\x12initial_commission\x18\t \x01(\x0b\x32\x31.tinkoff.public.invest.api.contract.v1.MoneyValue\x12N\n\x13\x65xecuted_commission\x18\n \x01(\x0b\x32\x31.tinkoff.public.invest.api.contract.v1.MoneyValue\x12\x0c\n\x04\x66igi\x18\x0b \x01(\t\x12H\n\tdirection\x18\x0c \x01(\x0e\x32\x35.tinkoff.public.invest.api.contract.v1.OrderDirection\x12Q\n\x16initial_security_price\x18\r \x01(\x0b\x32\x31.tinkoff.public.invest.api.contract.v1.MoneyValue\x12\x41\n\x06stages\x18\x0e \x03(\x0b\x32\x31.tinkoff.public.invest.api.contract.v1.OrderStage\x12M\n\x12service_commission\x18\x0f \x01(\x0b\x32\x31.tinkoff.public.invest.api.contract.v1.MoneyValue\x12\x10\n\x08\x63urrency\x18\x10 \x01(\t\x12\x44\n\norder_type\x18\x11 \x01(\x0e\x32\x30.tinkoff.public.invest.api.contract.v1.OrderType\x12.\n\norder_date\x18\x12 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x16\n\x0einstrument_uid\x18\x13 \x01(\t\x12\x18\n\x10order_request_id\x18\x14 \x01(\t\"\xa6\x01\n\nOrderStage\x12@\n\x05price\x18\x01 \x01(\x0b\x32\x31.tinkoff.public.invest.api.contract.v1.MoneyValue\x12\x10\n\x08quantity\x18\x02 \x01(\x03\x12\x10\n\x08trade_id\x18\x03 \x01(\t\x12\x32\n\x0e\x65xecution_time\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"\xa8\x02\n\x13ReplaceOrderRequest\x12\x18\n\naccount_id\x18\x01 \x01(\tB\x04\xe2\x41\x01\x02\x12\x16\n\x08order_id\x18\x06 \x01(\tB\x04\xe2\x41\x01\x02\x12\x1d\n\x0fidempotency_key\x18\x07 \x01(\tB\x04\xe2\x41\x01\x02\x12\x16\n\x08quantity\x18\x0b \x01(\x03\x42\x04\xe2\x41\x01\x02\x12\x44\n\x05price\x18\x0c \x01(\x0b\x32\x30.tinkoff.public.invest.api.contract.v1.QuotationH\x00\x88\x01\x01\x12I\n\nprice_type\x18\r \x01(\x0e\x32\x30.tinkoff.public.invest.api.contract.v1.PriceTypeH\x01\x88\x01\x01\x42\x08\n\x06_priceB\r\n\x0b_price_type\"\x9a\x01\n\x11GetMaxLotsRequest\x12\x18\n\naccount_id\x18\x01 \x01(\tB\x04\xe2\x41\x01\x02\x12\x1b\n\rinstrument_id\x18\x02 \x01(\tB\x04\xe2\x41\x01\x02\x12\x44\n\x05price\x18\x03 \x01(\x0b\x32\x30.tinkoff.public.invest.api.contract.v1.QuotationH\x00\x88\x01\x01\x42\x08\n\x06_price\"\xe6\x04\n\x12GetMaxLotsResponse\x12\x10\n\x08\x63urrency\x18\x01 \x01(\t\x12[\n\nbuy_limits\x18\x02 \x01(\x0b\x32G.tinkoff.public.invest.api.contract.v1.GetMaxLotsResponse.BuyLimitsView\x12\x62\n\x11\x62uy_margin_limits\x18\x03 \x01(\x0b\x32G.tinkoff.public.invest.api.contract.v1.GetMaxLotsResponse.BuyLimitsView\x12]\n\x0bsell_limits\x18\x04 \x01(\x0b\x32H.tinkoff.public.invest.api.contract.v1.GetMaxLotsResponse.SellLimitsView\x12\x64\n\x12sell_margin_limits\x18\x05 \x01(\x0b\x32H.tinkoff.public.invest.api.contract.v1.GetMaxLotsResponse.SellLimitsView\x1a\x8e\x01\n\rBuyLimitsView\x12J\n\x10\x62uy_money_amount\x18\x01 \x01(\x0b\x32\x30.tinkoff.public.invest.api.contract.v1.Quotation\x12\x14\n\x0c\x62uy_max_lots\x18\x02 \x01(\x03\x12\x1b\n\x13\x62uy_max_market_lots\x18\x03 \x01(\x03\x1a\'\n\x0eSellLimitsView\x12\x15\n\rsell_max_lots\x18\x01 \x01(\x03\"\xde\x01\n\x14GetOrderPriceRequest\x12\x12\n\naccount_id\x18\x01 \x01(\t\x12\x15\n\rinstrument_id\x18\x02 \x01(\t\x12?\n\x05price\x18\x03 \x01(\x0b\x32\x30.tinkoff.public.invest.api.contract.v1.Quotation\x12H\n\tdirection\x18\x0c \x01(\x0e\x32\x35.tinkoff.public.invest.api.contract.v1.OrderDirection\x12\x10\n\x08quantity\x18\r \x01(\x03\"\xe3\x07\n\x15GetOrderPriceResponse\x12M\n\x12total_order_amount\x18\x01 \x01(\x0b\x32\x31.tinkoff.public.invest.api.contract.v1.MoneyValue\x12O\n\x14initial_order_amount\x18\x05 \x01(\x0b\x32\x31.tinkoff.public.invest.api.contract.v1.MoneyValue\x12\x16\n\x0elots_requested\x18\x03 \x01(\x03\x12N\n\x13\x65xecuted_commission\x18\x07 \x01(\x0b\x32\x31.tinkoff.public.invest.api.contract.v1.MoneyValue\x12R\n\x17\x65xecuted_commission_rub\x18\x08 \x01(\x0b\x32\x31.tinkoff.public.invest.api.contract.v1.MoneyValue\x12M\n\x12service_commission\x18\t \x01(\x0b\x32\x31.tinkoff.public.invest.api.contract.v1.MoneyValue\x12J\n\x0f\x64\x65\x61l_commission\x18\n \x01(\x0b\x32\x31.tinkoff.public.invest.api.contract.v1.MoneyValue\x12\\\n\nextra_bond\x18\x0c \x01(\x0b\x32\x46.tinkoff.public.invest.api.contract.v1.GetOrderPriceResponse.ExtraBondH\x00\x12`\n\x0c\x65xtra_future\x18\r \x01(\x0b\x32H.tinkoff.public.invest.api.contract.v1.GetOrderPriceResponse.ExtraFutureH\x00\x1a\xa4\x01\n\tExtraBond\x12\x44\n\taci_value\x18\x02 \x01(\x0b\x32\x31.tinkoff.public.invest.api.contract.v1.MoneyValue\x12Q\n\x17nominal_conversion_rate\x18\x03 \x01(\x0b\x32\x30.tinkoff.public.invest.api.contract.v1.Quotation\x1aX\n\x0b\x45xtraFuture\x12I\n\x0einitial_margin\x18\x02 \x01(\x0b\x32\x31.tinkoff.public.invest.api.contract.v1.MoneyValueB\x12\n\x10instrument_extra\"a\n\x17OrderStateStreamRequest\x12\x10\n\x08\x61\x63\x63ounts\x18\x01 \x03(\t\x12\x1e\n\x11ping_delay_millis\x18\x0f \x01(\x05H\x00\x88\x01\x01\x42\x14\n\x12_ping_delay_millis\"\xf3\x01\n\x14SubscriptionResponse\x12\x13\n\x0btracking_id\x18\x01 \x01(\t\x12O\n\x06status\x18\x02 \x01(\x0e\x32?.tinkoff.public.invest.api.contract.v1.ResultSubscriptionStatus\x12\x11\n\tstream_id\x18\x04 \x01(\t\x12\x10\n\x08\x61\x63\x63ounts\x18\x05 \x03(\t\x12\x46\n\x05\x65rror\x18\x07 \x01(\x0b\x32\x32.tinkoff.public.invest.api.contract.v1.ErrorDetailH\x00\x88\x01\x01\x42\x08\n\x06_error\"\xba\x10\n\x18OrderStateStreamResponse\x12\x61\n\x0border_state\x18\x01 \x01(\x0b\x32J.tinkoff.public.invest.api.contract.v1.OrderStateStreamResponse.OrderStateH\x00\x12;\n\x04ping\x18\x02 \x01(\x0b\x32+.tinkoff.public.invest.api.contract.v1.PingH\x00\x12S\n\x0csubscription\x18\x03 \x01(\x0b\x32;.tinkoff.public.invest.api.contract.v1.SubscriptionResponseH\x00\x1a\xd5\n\n\nOrderState\x12\x10\n\x08order_id\x18\x01 \x01(\t\x12\x1d\n\x10order_request_id\x18\x02 \x01(\tH\x00\x88\x01\x01\x12\x13\n\x0b\x63lient_code\x18\x03 \x01(\t\x12.\n\ncreated_at\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x62\n\x17\x65xecution_report_status\x18\x05 \x01(\x0e\x32\x41.tinkoff.public.invest.api.contract.v1.OrderExecutionReportStatus\x12i\n\x0bstatus_info\x18\x06 \x01(\x0e\x32O.tinkoff.public.invest.api.contract.v1.OrderStateStreamResponse.StatusCauseInfoH\x01\x88\x01\x01\x12\x0e\n\x06ticker\x18\x07 \x01(\t\x12\x12\n\nclass_code\x18\x08 \x01(\t\x12\x10\n\x08lot_size\x18\t \x01(\x05\x12H\n\tdirection\x18\n \x01(\x0e\x32\x35.tinkoff.public.invest.api.contract.v1.OrderDirection\x12M\n\rtime_in_force\x18\x0b \x01(\x0e\x32\x36.tinkoff.public.invest.api.contract.v1.TimeInForceType\x12\x44\n\norder_type\x18\x0c \x01(\x0e\x32\x30.tinkoff.public.invest.api.contract.v1.OrderType\x12\x12\n\naccount_id\x18\r \x01(\t\x12N\n\x13initial_order_price\x18\x16 \x01(\x0b\x32\x31.tinkoff.public.invest.api.contract.v1.MoneyValue\x12\x46\n\x0border_price\x18\x17 \x01(\x0b\x32\x31.tinkoff.public.invest.api.contract.v1.MoneyValue\x12\x46\n\x06\x61mount\x18\x18 \x01(\x0b\x32\x31.tinkoff.public.invest.api.contract.v1.MoneyValueH\x02\x88\x01\x01\x12O\n\x14\x65xecuted_order_price\x18\x19 \x01(\x0b\x32\x31.tinkoff.public.invest.api.contract.v1.MoneyValue\x12\x10\n\x08\x63urrency\x18\x1a \x01(\t\x12\x16\n\x0elots_requested\x18\x1b \x01(\x03\x12\x15\n\rlots_executed\x18\x1c \x01(\x03\x12\x11\n\tlots_left\x18\x1d \x01(\x03\x12\x16\n\x0elots_cancelled\x18\x1e \x01(\x03\x12_\n\x06marker\x18\x1f \x01(\x0e\x32J.tinkoff.public.invest.api.contract.v1.OrderStateStreamResponse.MarkerTypeH\x03\x88\x01\x01\x12\x41\n\x06trades\x18! \x03(\x0b\x32\x31.tinkoff.public.invest.api.contract.v1.OrderTrade\x12\x33\n\x0f\x63ompletion_time\x18# \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x10\n\x08\x65xchange\x18$ \x01(\t\x12\x16\n\x0einstrument_uid\x18) \x01(\tB\x13\n\x11_order_request_idB\x0e\n\x0c_status_infoB\t\n\x07_amountB\t\n\x07_marker\"\xaf\x01\n\nMarkerType\x12\x12\n\x0eMARKER_UNKNOWN\x10\x00\x12\x11\n\rMARKER_BROKER\x10\x01\x12\x0f\n\x0bMARKER_CHAT\x10\x02\x12\x10\n\x0cMARKER_PAPER\x10\x03\x12\x11\n\rMARKER_MARGIN\x10\x04\x12\x10\n\x0cMARKER_TKBNM\x10\x05\x12\x10\n\x0cMARKER_SHORT\x10\x06\x12\x11\n\rMARKER_SPECMM\x10\x07\x12\r\n\tMARKER_PO\x10\x08\"\x93\x02\n\x0fStatusCauseInfo\x12\x15\n\x11\x43\x41USE_UNSPECIFIED\x10\x00\x12\x1d\n\x19\x43\x41USE_CANCELLED_BY_CLIENT\x10\x0f\x12\x1f\n\x1b\x43\x41USE_CANCELLED_BY_EXCHANGE\x10\x01\x12\'\n#CAUSE_CANCELLED_NOT_ENOUGH_POSITION\x10\x02\x12#\n\x1f\x43\x41USE_CANCELLED_BY_CLIENT_BLOCK\x10\x03\x12\x1c\n\x18\x43\x41USE_REJECTED_BY_BROKER\x10\x04\x12\x1e\n\x1a\x43\x41USE_REJECTED_BY_EXCHANGE\x10\x05\x12\x1d\n\x19\x43\x41USE_CANCELLED_BY_BROKER\x10\x06\x42\t\n\x07payload*d\n\x0eOrderDirection\x12\x1f\n\x1bORDER_DIRECTION_UNSPECIFIED\x10\x00\x12\x17\n\x13ORDER_DIRECTION_BUY\x10\x01\x12\x18\n\x14ORDER_DIRECTION_SELL\x10\x02*n\n\tOrderType\x12\x1a\n\x16ORDER_TYPE_UNSPECIFIED\x10\x00\x12\x14\n\x10ORDER_TYPE_LIMIT\x10\x01\x12\x15\n\x11ORDER_TYPE_MARKET\x10\x02\x12\x18\n\x14ORDER_TYPE_BESTPRICE\x10\x03*\x80\x02\n\x1aOrderExecutionReportStatus\x12\'\n#EXECUTION_REPORT_STATUS_UNSPECIFIED\x10\x00\x12 \n\x1c\x45XECUTION_REPORT_STATUS_FILL\x10\x01\x12$\n EXECUTION_REPORT_STATUS_REJECTED\x10\x02\x12%\n!EXECUTION_REPORT_STATUS_CANCELLED\x10\x03\x12\x1f\n\x1b\x45XECUTION_REPORT_STATUS_NEW\x10\x04\x12)\n%EXECUTION_REPORT_STATUS_PARTIALLYFILL\x10\x05*\x88\x01\n\x0fTimeInForceType\x12\x1d\n\x19TIME_IN_FORCE_UNSPECIFIED\x10\x00\x12\x15\n\x11TIME_IN_FORCE_DAY\x10\x01\x12\x1f\n\x1bTIME_IN_FORCE_FILL_AND_KILL\x10\x02\x12\x1e\n\x1aTIME_IN_FORCE_FILL_OR_KILL\x10\x03*c\n\x0bOrderIdType\x12\x1d\n\x19ORDER_ID_TYPE_UNSPECIFIED\x10\x00\x12\x1a\n\x16ORDER_ID_TYPE_EXCHANGE\x10\x01\x12\x19\n\x15ORDER_ID_TYPE_REQUEST\x10\x02\x32\xb9\x02\n\x13OrdersStreamService\x12\x89\x01\n\x0cTradesStream\x12:.tinkoff.public.invest.api.contract.v1.TradesStreamRequest\x1a;.tinkoff.public.invest.api.contract.v1.TradesStreamResponse0\x01\x12\x95\x01\n\x10OrderStateStream\x12>.tinkoff.public.invest.api.contract.v1.OrderStateStreamRequest\x1a?.tinkoff.public.invest.api.contract.v1.OrderStateStreamResponse0\x01\x32\xbf\x08\n\rOrdersService\x12~\n\tPostOrder\x12\x37.tinkoff.public.invest.api.contract.v1.PostOrderRequest\x1a\x38.tinkoff.public.invest.api.contract.v1.PostOrderResponse\x12\x8d\x01\n\x0ePostOrderAsync\x12<.tinkoff.public.invest.api.contract.v1.PostOrderAsyncRequest\x1a=.tinkoff.public.invest.api.contract.v1.PostOrderAsyncResponse\x12\x84\x01\n\x0b\x43\x61ncelOrder\x12\x39.tinkoff.public.invest.api.contract.v1.CancelOrderRequest\x1a:.tinkoff.public.invest.api.contract.v1.CancelOrderResponse\x12\x7f\n\rGetOrderState\x12;.tinkoff.public.invest.api.contract.v1.GetOrderStateRequest\x1a\x31.tinkoff.public.invest.api.contract.v1.OrderState\x12~\n\tGetOrders\x12\x37.tinkoff.public.invest.api.contract.v1.GetOrdersRequest\x1a\x38.tinkoff.public.invest.api.contract.v1.GetOrdersResponse\x12\x84\x01\n\x0cReplaceOrder\x12:.tinkoff.public.invest.api.contract.v1.ReplaceOrderRequest\x1a\x38.tinkoff.public.invest.api.contract.v1.PostOrderResponse\x12\x81\x01\n\nGetMaxLots\x12\x38.tinkoff.public.invest.api.contract.v1.GetMaxLotsRequest\x1a\x39.tinkoff.public.invest.api.contract.v1.GetMaxLotsResponse\x12\x8a\x01\n\rGetOrderPrice\x12;.tinkoff.public.invest.api.contract.v1.GetOrderPriceRequest\x1a<.tinkoff.public.invest.api.contract.v1.GetOrderPriceResponseBa\n\x1cru.tinkoff.piapi.contract.v1P\x01Z\x0c./;investapi\xa2\x02\x05TIAPI\xaa\x02\x14Tinkoff.InvestApi.V1\xca\x02\x11Tinkoff\\Invest\\V1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'tinvest.grpc.orders_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\034ru.tinkoff.piapi.contract.v1P\001Z\014./;investapi\242\002\005TIAPI\252\002\024Tinkoff.InvestApi.V1\312\002\021Tinkoff\\Invest\\V1'
  _globals['_POSTORDERREQUEST'].fields_by_name['figi']._loaded_options = None
  _globals['_POSTORDERREQUEST'].fields_by_name['figi']._serialized_options = b'\030\001'
  _globals['_POSTORDERREQUEST'].fields_by_name['quantity']._loaded_options = None
  _globals['_POSTORDERREQUEST'].fields_by_name['quantity']._serialized_options = b'\342A\001\002'
  _globals['_POSTORDERREQUEST'].fields_by_name['direction']._loaded_options = None
  _globals['_POSTORDERREQUEST'].fields_by_name['direction']._serialized_options = b'\342A\001\002'
  _globals['_POSTORDERREQUEST'].fields_by_name['account_id']._loaded_options = None
  _globals['_POSTORDERREQUEST'].fields_by_name['account_id']._serialized_options = b'\342A\001\002'
  _globals['_POSTORDERREQUEST'].fields_by_name['order_type']._loaded_options = None
  _globals['_POSTORDERREQUEST'].fields_by_name['order_type']._serialized_options = b'\342A\001\002'
  _globals['_POSTORDERREQUEST'].fields_by_name['order_id']._loaded_options = None
  _globals['_POSTORDERREQUEST'].fields_by_name['order_id']._serialized_options = b'\342A\001\002'
  _globals['_POSTORDERASYNCREQUEST'].fields_by_name['instrument_id']._loaded_options = None
  _globals['_POSTORDERASYNCREQUEST'].fields_by_name['instrument_id']._serialized_options = b'\342A\001\002'
  _globals['_POSTORDERASYNCREQUEST'].fields_by_name['quantity']._loaded_options = None
  _globals['_POSTORDERASYNCREQUEST'].fields_by_name['quantity']._serialized_options = b'\342A\001\002'
  _globals['_POSTORDERASYNCREQUEST'].fields_by_name['direction']._loaded_options = None
  _globals['_POSTORDERASYNCREQUEST'].fields_by_name['direction']._serialized_options = b'\342A\001\002'
  _globals['_POSTORDERASYNCREQUEST'].fields_by_name['account_id']._loaded_options = None
  _globals['_POSTORDERASYNCREQUEST'].fields_by_name['account_id']._serialized_options = b'\342A\001\002'
  _globals['_POSTORDERASYNCREQUEST'].fields_by_name['order_type']._loaded_options = None
  _globals['_POSTORDERASYNCREQUEST'].fields_by_name['order_type']._serialized_options = b'\342A\001\002'
  _globals['_POSTORDERASYNCREQUEST'].fields_by_name['order_id']._loaded_options = None
  _globals['_POSTORDERASYNCREQUEST'].fields_by_name['order_id']._serialized_options = b'\342A\001\002'
  _globals['_POSTORDERASYNCRESPONSE'].fields_by_name['order_request_id']._loaded_options = None
  _globals['_POSTORDERASYNCRESPONSE'].fields_by_name['order_request_id']._serialized_options = b'\342A\001\002'
  _globals['_POSTORDERASYNCRESPONSE'].fields_by_name['execution_report_status']._loaded_options = None
  _globals['_POSTORDERASYNCRESPONSE'].fields_by_name['execution_report_status']._serialized_options = b'\342A\001\002'
  _globals['_CANCELORDERREQUEST'].fields_by_name['account_id']._loaded_options = None
  _globals['_CANCELORDERREQUEST'].fields_by_name['account_id']._serialized_options = b'\342A\001\002'
  _globals['_CANCELORDERREQUEST'].fields_by_name['order_id']._loaded_options = None
  _globals['_CANCELORDERREQUEST'].fields_by_name['order_id']._serialized_options = b'\342A\001\002'
  _globals['_GETORDERSTATEREQUEST'].fields_by_name['account_id']._loaded_options = None
  _globals['_GETORDERSTATEREQUEST'].fields_by_name['account_id']._serialized_options = b'\342A\001\002'
  _globals['_GETORDERSTATEREQUEST'].fields_by_name['order_id']._loaded_options = None
  _globals['_GETORDERSTATEREQUEST'].fields_by_name['order_id']._serialized_options = b'\342A\001\002'
  _globals['_GETORDERSREQUEST'].fields_by_name['account_id']._loaded_options = None
  _globals['_GETORDERSREQUEST'].fields_by_name['account_id']._serialized_options = b'\342A\001\002'
  _globals['_REPLACEORDERREQUEST'].fields_by_name['account_id']._loaded_options = None
  _globals['_REPLACEORDERREQUEST'].fields_by_name['account_id']._serialized_options = b'\342A\001\002'
  _globals['_REPLACEORDERREQUEST'].fields_by_name['order_id']._loaded_options = None
  _globals['_REPLACEORDERREQUEST'].fields_by_name['order_id']._serialized_options = b'\342A\001\002'
  _globals['_REPLACEORDERREQUEST'].fields_by_name['idempotency_key']._loaded_options = None
  _globals['_REPLACEORDERREQUEST'].fields_by_name['idempotency_key']._serialized_options = b'\342A\001\002'
  _globals['_REPLACEORDERREQUEST'].fields_by_name['quantity']._loaded_options = None
  _globals['_REPLACEORDERREQUEST'].fields_by_name['quantity']._serialized_options = b'\342A\001\002'
  _globals['_GETMAXLOTSREQUEST'].fields_by_name['account_id']._loaded_options = None
  _globals['_GETMAXLOTSREQUEST'].fields_by_name['account_id']._serialized_options = b'\342A\001\002'
  _globals['_GETMAXLOTSREQUEST'].fields_by_name['instrument_id']._loaded_options = None
  _globals['_GETMAXLOTSREQUEST'].fields_by_name['instrument_id']._serialized_options = b'\342A\001\002'
  _globals['_ORDERDIRECTION']._serialized_start=10138
  _globals['_ORDERDIRECTION']._serialized_end=10238
  _globals['_ORDERTYPE']._serialized_start=10240
  _globals['_ORDERTYPE']._serialized_end=10350
  _globals['_ORDEREXECUTIONREPORTSTATUS']._serialized_start=10353
  _globals['_ORDEREXECUTIONREPORTSTATUS']._serialized_end=10609
  _globals['_TIMEINFORCETYPE']._serialized_start=10612
  _globals['_TIMEINFORCETYPE']._serialized_end=10748
  _globals['_ORDERIDTYPE']._serialized_start=10750
  _globals['_ORDERIDTYPE']._serialized_end=10849
  _globals['_TRADESSTREAMREQUEST']._serialized_start=174
  _globals['_TRADESSTREAMREQUEST']._serialized_end=213
  _globals['_TRADESSTREAMRESPONSE']._serialized_start=216
  _globals['_TRADESSTREAMRESPONSE']._serialized_end=471
  _globals['_ORDERTRADES']._serialized_start=474
  _globals['_ORDERTRADES']._serialized_end=752
  _globals['_ORDERTRADE']._serialized_start=755
  _globals['_ORDERTRADE']._serialized_end=915
  _globals['_POSTORDERREQUEST']._serialized_start=918
  _globals['_POSTORDERREQUEST']._serialized_end=1450
  _globals['_POSTORDERRESPONSE']._serialized_start=1453
  _globals['_POSTORDERRESPONSE']._serialized_end=2581
  _globals['_POSTORDERASYNCREQUEST']._serialized_start=2584
  _globals['_POSTORDERASYNCREQUEST']._serialized_end=3138
  _globals['_POSTORDERASYNCRESPONSE']._serialized_start=3141
  _globals['_POSTORDERASYNCRESPONSE']._serialized_end=3353
  _globals['_CANCELORDERREQUEST']._serialized_start=3356
  _globals['_CANCELORDERREQUEST']._serialized_end=3524
  _globals['_CANCELORDERRESPONSE']._serialized_start=3527
  _globals['_CANCELORDERRESPONSE']._serialized_end=3675
  _globals['_GETORDERSTATEREQUEST']._serialized_start=3678
  _globals['_GETORDERSTATEREQUEST']._serialized_end=3918
  _globals['_GETORDERSREQUEST']._serialized_start=3920
  _globals['_GETORDERSREQUEST']._serialized_end=3964
  _globals['_GETORDERSRESPONSE']._serialized_start=3966
  _globals['_GETORDERSRESPONSE']._serialized_end=4052
  _globals['_ORDERSTATE']._serialized_start=4055
  _globals['_ORDERSTATE']._serialized_end=5217
  _globals['_ORDERSTAGE']._serialized_start=5220
  _globals['_ORDERSTAGE']._serialized_end=5386
  _globals['_REPLACEORDERREQUEST']._serialized_start=5389
  _globals['_REPLACEORDERREQUEST']._serialized_end=5685
  _globals['_GETMAXLOTSREQUEST']._serialized_start=5688
  _globals['_GETMAXLOTSREQUEST']._serialized_end=5842
  _globals['_GETMAXLOTSRESPONSE']._serialized_start=5845
  _globals['_GETMAXLOTSRESPONSE']._serialized_end=6459
  _globals['_GETMAXLOTSRESPONSE_BUYLIMITSVIEW']._serialized_start=6276
  _globals['_GETMAXLOTSRESPONSE_BUYLIMITSVIEW']._serialized_end=6418
  _globals['_GETMAXLOTSRESPONSE_SELLLIMITSVIEW']._serialized_start=6420
  _globals['_GETMAXLOTSRESPONSE_SELLLIMITSVIEW']._serialized_end=6459
  _globals['_GETORDERPRICEREQUEST']._serialized_start=6462
  _globals['_GETORDERPRICEREQUEST']._serialized_end=6684
  _globals['_GETORDERPRICERESPONSE']._serialized_start=6687
  _globals['_GETORDERPRICERESPONSE']._serialized_end=7682
  _globals['_GETORDERPRICERESPONSE_EXTRABOND']._serialized_start=7408
  _globals['_GETORDERPRICERESPONSE_EXTRABOND']._serialized_end=7572
  _globals['_GETORDERPRICERESPONSE_EXTRAFUTURE']._serialized_start=7574
  _globals['_GETORDERPRICERESPONSE_EXTRAFUTURE']._serialized_end=7662
  _globals['_ORDERSTATESTREAMREQUEST']._serialized_start=7684
  _globals['_ORDERSTATESTREAMREQUEST']._serialized_end=7781
  _globals['_SUBSCRIPTIONRESPONSE']._serialized_start=7784
  _globals['_SUBSCRIPTIONRESPONSE']._serialized_end=8027
  _globals['_ORDERSTATESTREAMRESPONSE']._serialized_start=8030
  _globals['_ORDERSTATESTREAMRESPONSE']._serialized_end=10136
  _globals['_ORDERSTATESTREAMRESPONSE_ORDERSTATE']._serialized_start=8304
  _globals['_ORDERSTATESTREAMRESPONSE_ORDERSTATE']._serialized_end=9669
  _globals['_ORDERSTATESTREAMRESPONSE_MARKERTYPE']._serialized_start=9672
  _globals['_ORDERSTATESTREAMRESPONSE_MARKERTYPE']._serialized_end=9847
  _globals['_ORDERSTATESTREAMRESPONSE_STATUSCAUSEINFO']._serialized_start=9850
  _globals['_ORDERSTATESTREAMRESPONSE_STATUSCAUSEINFO']._serialized_end=10125
  _globals['_ORDERSSTREAMSERVICE']._serialized_start=10852
  _globals['_ORDERSSTREAMSERVICE']._serialized_end=11165
  _globals['_ORDERSSERVICE']._serialized_start=11168
  _globals['_ORDERSSERVICE']._serialized_end=12255
# @@protoc_insertion_point(module_scope)