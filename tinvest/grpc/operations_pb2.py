# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: tinvest/grpc/operations.proto
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
    'tinvest/grpc/operations.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from tinvest.grpc import common_pb2 as tinvest_dot_grpc_dot_common__pb2
from tinvest.grpc.google.api import field_behavior_pb2 as tinvest_dot_grpc_dot_google_dot_api_dot_field__behavior__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1dtinvest/grpc/operations.proto\x12%tinkoff.public.invest.api.contract.v1\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x19tinvest/grpc/common.proto\x1a,tinvest/grpc/google/api/field_behavior.proto\"\x8a\x02\n\x11OperationsRequest\x12\x18\n\naccount_id\x18\x01 \x01(\tB\x04\xe2\x41\x01\x02\x12-\n\x04\x66rom\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.TimestampH\x00\x88\x01\x01\x12+\n\x02to\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.TimestampH\x01\x88\x01\x01\x12I\n\x05state\x18\x04 \x01(\x0e\x32\x35.tinkoff.public.invest.api.contract.v1.OperationStateH\x02\x88\x01\x01\x12\x11\n\x04\x66igi\x18\x05 \x01(\tH\x03\x88\x01\x01\x42\x07\n\x05_fromB\x05\n\x03_toB\x08\n\x06_stateB\x07\n\x05_figi\"Z\n\x12OperationsResponse\x12\x44\n\noperations\x18\x01 \x03(\x0b\x32\x30.tinkoff.public.invest.api.contract.v1.Operation\"\xc5\x05\n\tOperation\x12\n\n\x02id\x18\x01 \x01(\t\x12\x1b\n\x13parent_operation_id\x18\x02 \x01(\t\x12\x10\n\x08\x63urrency\x18\x03 \x01(\t\x12\x42\n\x07payment\x18\x04 \x01(\x0b\x32\x31.tinkoff.public.invest.api.contract.v1.MoneyValue\x12@\n\x05price\x18\x05 \x01(\x0b\x32\x31.tinkoff.public.invest.api.contract.v1.MoneyValue\x12\x44\n\x05state\x18\x06 \x01(\x0e\x32\x35.tinkoff.public.invest.api.contract.v1.OperationState\x12\x10\n\x08quantity\x18\x07 \x01(\x03\x12\x15\n\rquantity_rest\x18\x08 \x01(\x03\x12\x0c\n\x04\x66igi\x18\t \x01(\t\x12\x17\n\x0finstrument_type\x18\n \x01(\t\x12(\n\x04\x64\x61te\x18\x0b \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0c\n\x04type\x18\x0c \x01(\t\x12L\n\x0eoperation_type\x18\r \x01(\x0e\x32\x34.tinkoff.public.invest.api.contract.v1.OperationType\x12\x45\n\x06trades\x18\x0e \x03(\x0b\x32\x35.tinkoff.public.invest.api.contract.v1.OperationTrade\x12\x11\n\tasset_uid\x18\x10 \x01(\t\x12\x14\n\x0cposition_uid\x18\x11 \x01(\t\x12\x16\n\x0einstrument_uid\x18\x12 \x01(\t\x12S\n\x10\x63hild_operations\x18\x13 \x03(\x0b\x32\x39.tinkoff.public.invest.api.contract.v1.ChildOperationItem\"\xa5\x01\n\x0eOperationTrade\x12\x10\n\x08trade_id\x18\x01 \x01(\t\x12-\n\tdate_time\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x10\n\x08quantity\x18\x03 \x01(\x03\x12@\n\x05price\x18\x04 \x01(\x0b\x32\x31.tinkoff.public.invest.api.contract.v1.MoneyValue\"\xc7\x01\n\x10PortfolioRequest\x12\x18\n\naccount_id\x18\x01 \x01(\tB\x04\xe2\x41\x01\x02\x12^\n\x08\x63urrency\x18\x02 \x01(\x0e\x32G.tinkoff.public.invest.api.contract.v1.PortfolioRequest.CurrencyRequestH\x00\x88\x01\x01\",\n\x0f\x43urrencyRequest\x12\x07\n\x03RUB\x10\x00\x12\x07\n\x03USD\x10\x01\x12\x07\n\x03\x45UR\x10\x02\x42\x0b\n\t_currency\"\x9b\x07\n\x11PortfolioResponse\x12N\n\x13total_amount_shares\x18\x01 \x01(\x0b\x32\x31.tinkoff.public.invest.api.contract.v1.MoneyValue\x12M\n\x12total_amount_bonds\x18\x02 \x01(\x0b\x32\x31.tinkoff.public.invest.api.contract.v1.MoneyValue\x12K\n\x10total_amount_etf\x18\x03 \x01(\x0b\x32\x31.tinkoff.public.invest.api.contract.v1.MoneyValue\x12R\n\x17total_amount_currencies\x18\x04 \x01(\x0b\x32\x31.tinkoff.public.invest.api.contract.v1.MoneyValue\x12O\n\x14total_amount_futures\x18\x05 \x01(\x0b\x32\x31.tinkoff.public.invest.api.contract.v1.MoneyValue\x12H\n\x0e\x65xpected_yield\x18\x06 \x01(\x0b\x32\x30.tinkoff.public.invest.api.contract.v1.Quotation\x12K\n\tpositions\x18\x07 \x03(\x0b\x32\x38.tinkoff.public.invest.api.contract.v1.PortfolioPosition\x12\x12\n\naccount_id\x18\x08 \x01(\t\x12O\n\x14total_amount_options\x18\t \x01(\x0b\x32\x31.tinkoff.public.invest.api.contract.v1.MoneyValue\x12J\n\x0ftotal_amount_sp\x18\n \x01(\x0b\x32\x31.tinkoff.public.invest.api.contract.v1.MoneyValue\x12Q\n\x16total_amount_portfolio\x18\x0b \x01(\x0b\x32\x31.tinkoff.public.invest.api.contract.v1.MoneyValue\x12Z\n\x11virtual_positions\x18\x0c \x03(\x0b\x32?.tinkoff.public.invest.api.contract.v1.VirtualPortfolioPosition\",\n\x10PositionsRequest\x12\x18\n\naccount_id\x18\x01 \x01(\tB\x04\xe2\x41\x01\x02\"\xa1\x03\n\x11PositionsResponse\x12@\n\x05money\x18\x01 \x03(\x0b\x32\x31.tinkoff.public.invest.api.contract.v1.MoneyValue\x12\x42\n\x07\x62locked\x18\x02 \x03(\x0b\x32\x31.tinkoff.public.invest.api.contract.v1.MoneyValue\x12N\n\nsecurities\x18\x03 \x03(\x0b\x32:.tinkoff.public.invest.api.contract.v1.PositionsSecurities\x12\"\n\x1alimits_loading_in_progress\x18\x04 \x01(\x08\x12H\n\x07\x66utures\x18\x05 \x03(\x0b\x32\x37.tinkoff.public.invest.api.contract.v1.PositionsFutures\x12H\n\x07options\x18\x06 \x03(\x0b\x32\x37.tinkoff.public.invest.api.contract.v1.PositionsOptions\"1\n\x15WithdrawLimitsRequest\x12\x18\n\naccount_id\x18\x01 \x01(\tB\x04\xe2\x41\x01\x02\"\xec\x01\n\x16WithdrawLimitsResponse\x12@\n\x05money\x18\x01 \x03(\x0b\x32\x31.tinkoff.public.invest.api.contract.v1.MoneyValue\x12\x42\n\x07\x62locked\x18\x02 \x03(\x0b\x32\x31.tinkoff.public.invest.api.contract.v1.MoneyValue\x12L\n\x11\x62locked_guarantee\x18\x03 \x03(\x0b\x32\x31.tinkoff.public.invest.api.contract.v1.MoneyValue\"\xc8\x07\n\x11PortfolioPosition\x12\x0c\n\x04\x66igi\x18\x01 \x01(\t\x12\x17\n\x0finstrument_type\x18\x02 \x01(\t\x12\x42\n\x08quantity\x18\x03 \x01(\x0b\x32\x30.tinkoff.public.invest.api.contract.v1.Quotation\x12Q\n\x16\x61verage_position_price\x18\x04 \x01(\x0b\x32\x31.tinkoff.public.invest.api.contract.v1.MoneyValue\x12H\n\x0e\x65xpected_yield\x18\x05 \x01(\x0b\x32\x30.tinkoff.public.invest.api.contract.v1.Quotation\x12\x46\n\x0b\x63urrent_nkd\x18\x06 \x01(\x0b\x32\x31.tinkoff.public.invest.api.contract.v1.MoneyValue\x12W\n\x19\x61verage_position_price_pt\x18\x07 \x01(\x0b\x32\x30.tinkoff.public.invest.api.contract.v1.QuotationB\x02\x18\x01\x12H\n\rcurrent_price\x18\x08 \x01(\x0b\x32\x31.tinkoff.public.invest.api.contract.v1.MoneyValue\x12V\n\x1b\x61verage_position_price_fifo\x18\t \x01(\x0b\x32\x31.tinkoff.public.invest.api.contract.v1.MoneyValue\x12K\n\rquantity_lots\x18\n \x01(\x0b\x32\x30.tinkoff.public.invest.api.contract.v1.QuotationB\x02\x18\x01\x12\x0f\n\x07\x62locked\x18\x15 \x01(\x08\x12\x46\n\x0c\x62locked_lots\x18\x16 \x01(\x0b\x32\x30.tinkoff.public.invest.api.contract.v1.Quotation\x12\x14\n\x0cposition_uid\x18\x18 \x01(\t\x12\x16\n\x0einstrument_uid\x18\x19 \x01(\t\x12\x45\n\nvar_margin\x18\x1a \x01(\x0b\x32\x31.tinkoff.public.invest.api.contract.v1.MoneyValue\x12M\n\x13\x65xpected_yield_fifo\x18\x1b \x01(\x0b\x32\x30.tinkoff.public.invest.api.contract.v1.Quotation\"\xf2\x04\n\x18VirtualPortfolioPosition\x12\x14\n\x0cposition_uid\x18\x01 \x01(\t\x12\x16\n\x0einstrument_uid\x18\x02 \x01(\t\x12\x0c\n\x04\x66igi\x18\x03 \x01(\t\x12\x17\n\x0finstrument_type\x18\x04 \x01(\t\x12\x42\n\x08quantity\x18\x05 \x01(\x0b\x32\x30.tinkoff.public.invest.api.contract.v1.Quotation\x12Q\n\x16\x61verage_position_price\x18\x06 \x01(\x0b\x32\x31.tinkoff.public.invest.api.contract.v1.MoneyValue\x12H\n\x0e\x65xpected_yield\x18\x07 \x01(\x0b\x32\x30.tinkoff.public.invest.api.contract.v1.Quotation\x12M\n\x13\x65xpected_yield_fifo\x18\x08 \x01(\x0b\x32\x30.tinkoff.public.invest.api.contract.v1.Quotation\x12/\n\x0b\x65xpire_date\x18\t \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12H\n\rcurrent_price\x18\n \x01(\x0b\x32\x31.tinkoff.public.invest.api.contract.v1.MoneyValue\x12V\n\x1b\x61verage_position_price_fifo\x18\x0b \x01(\x0b\x32\x31.tinkoff.public.invest.api.contract.v1.MoneyValue\"\xa6\x01\n\x13PositionsSecurities\x12\x0c\n\x04\x66igi\x18\x01 \x01(\t\x12\x0f\n\x07\x62locked\x18\x02 \x01(\x03\x12\x0f\n\x07\x62\x61lance\x18\x03 \x01(\x03\x12\x14\n\x0cposition_uid\x18\x04 \x01(\t\x12\x16\n\x0einstrument_uid\x18\x05 \x01(\t\x12\x18\n\x10\x65xchange_blocked\x18\x0b \x01(\x08\x12\x17\n\x0finstrument_type\x18\x10 \x01(\t\"p\n\x10PositionsFutures\x12\x0c\n\x04\x66igi\x18\x01 \x01(\t\x12\x0f\n\x07\x62locked\x18\x02 \x01(\x03\x12\x0f\n\x07\x62\x61lance\x18\x03 \x01(\x03\x12\x14\n\x0cposition_uid\x18\x04 \x01(\t\x12\x16\n\x0einstrument_uid\x18\x05 \x01(\t\"b\n\x10PositionsOptions\x12\x14\n\x0cposition_uid\x18\x01 \x01(\t\x12\x16\n\x0einstrument_uid\x18\x02 \x01(\t\x12\x0f\n\x07\x62locked\x18\x0b \x01(\x03\x12\x0f\n\x07\x62\x61lance\x18\x15 \x01(\x03\"\xf2\x01\n\x13\x42rokerReportRequest\x12l\n\x1egenerate_broker_report_request\x18\x01 \x01(\x0b\x32\x42.tinkoff.public.invest.api.contract.v1.GenerateBrokerReportRequestH\x00\x12\x62\n\x19get_broker_report_request\x18\x02 \x01(\x0b\x32=.tinkoff.public.invest.api.contract.v1.GetBrokerReportRequestH\x00\x42\t\n\x07payload\"\xf7\x01\n\x14\x42rokerReportResponse\x12n\n\x1fgenerate_broker_report_response\x18\x01 \x01(\x0b\x32\x43.tinkoff.public.invest.api.contract.v1.GenerateBrokerReportResponseH\x00\x12\x64\n\x1aget_broker_report_response\x18\x02 \x01(\x0b\x32>.tinkoff.public.invest.api.contract.v1.GetBrokerReportResponseH\x00\x42\t\n\x07payload\"\x95\x01\n\x1bGenerateBrokerReportRequest\x12\x18\n\naccount_id\x18\x01 \x01(\tB\x04\xe2\x41\x01\x02\x12.\n\x04\x66rom\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x04\xe2\x41\x01\x02\x12,\n\x02to\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x04\xe2\x41\x01\x02\"/\n\x1cGenerateBrokerReportResponse\x12\x0f\n\x07task_id\x18\x01 \x01(\t\"K\n\x16GetBrokerReportRequest\x12\x15\n\x07task_id\x18\x01 \x01(\tB\x04\xe2\x41\x01\x02\x12\x11\n\x04page\x18\x02 \x01(\x05H\x00\x88\x01\x01\x42\x07\n\x05_page\"\x9b\x01\n\x17GetBrokerReportResponse\x12J\n\rbroker_report\x18\x01 \x03(\x0b\x32\x33.tinkoff.public.invest.api.contract.v1.BrokerReport\x12\x12\n\nitemsCount\x18\x02 \x01(\x05\x12\x12\n\npagesCount\x18\x03 \x01(\x05\x12\x0c\n\x04page\x18\x04 \x01(\x05\"\xda\x08\n\x0c\x42rokerReport\x12\x10\n\x08trade_id\x18\x01 \x01(\t\x12\x10\n\x08order_id\x18\x02 \x01(\t\x12\x0c\n\x04\x66igi\x18\x03 \x01(\t\x12\x14\n\x0c\x65xecute_sign\x18\x04 \x01(\t\x12\x32\n\x0etrade_datetime\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x10\n\x08\x65xchange\x18\x06 \x01(\t\x12\x12\n\nclass_code\x18\x07 \x01(\t\x12\x11\n\tdirection\x18\x08 \x01(\t\x12\x0c\n\x04name\x18\t \x01(\t\x12\x0e\n\x06ticker\x18\n \x01(\t\x12@\n\x05price\x18\x0b \x01(\x0b\x32\x31.tinkoff.public.invest.api.contract.v1.MoneyValue\x12\x10\n\x08quantity\x18\x0c \x01(\x03\x12G\n\x0corder_amount\x18\r \x01(\x0b\x32\x31.tinkoff.public.invest.api.contract.v1.MoneyValue\x12\x43\n\taci_value\x18\x0e \x01(\x0b\x32\x30.tinkoff.public.invest.api.contract.v1.Quotation\x12M\n\x12total_order_amount\x18\x0f \x01(\x0b\x32\x31.tinkoff.public.invest.api.contract.v1.MoneyValue\x12L\n\x11\x62roker_commission\x18\x10 \x01(\x0b\x32\x31.tinkoff.public.invest.api.contract.v1.MoneyValue\x12N\n\x13\x65xchange_commission\x18\x11 \x01(\x0b\x32\x31.tinkoff.public.invest.api.contract.v1.MoneyValue\x12W\n\x1c\x65xchange_clearing_commission\x18\x12 \x01(\x0b\x32\x31.tinkoff.public.invest.api.contract.v1.MoneyValue\x12\x43\n\trepo_rate\x18\x13 \x01(\x0b\x32\x30.tinkoff.public.invest.api.contract.v1.Quotation\x12\r\n\x05party\x18\x14 \x01(\t\x12\x34\n\x10\x63lear_value_date\x18\x15 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x32\n\x0esec_value_date\x18\x16 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x15\n\rbroker_status\x18\x17 \x01(\t\x12\x1f\n\x17separate_agreement_type\x18\x18 \x01(\t\x12!\n\x19separate_agreement_number\x18\x19 \x01(\t\x12\x1f\n\x17separate_agreement_date\x18\x1a \x01(\t\x12\x15\n\rdelivery_type\x18\x1b \x01(\t\"\xa8\x02\n GetDividendsForeignIssuerRequest\x12\x80\x01\n\"generate_div_foreign_issuer_report\x18\x01 \x01(\x0b\x32R.tinkoff.public.invest.api.contract.v1.GenerateDividendsForeignIssuerReportRequestH\x00\x12v\n\x1dget_div_foreign_issuer_report\x18\x02 \x01(\x0b\x32M.tinkoff.public.invest.api.contract.v1.GetDividendsForeignIssuerReportRequestH\x00\x42\t\n\x07payload\"\xb0\x02\n!GetDividendsForeignIssuerResponse\x12\x8a\x01\n+generate_div_foreign_issuer_report_response\x18\x01 \x01(\x0b\x32S.tinkoff.public.invest.api.contract.v1.GenerateDividendsForeignIssuerReportResponseH\x00\x12s\n\x19\x64iv_foreign_issuer_report\x18\x02 \x01(\x0b\x32N.tinkoff.public.invest.api.contract.v1.GetDividendsForeignIssuerReportResponseH\x00\x42\t\n\x07payload\"\xa5\x01\n+GenerateDividendsForeignIssuerReportRequest\x12\x18\n\naccount_id\x18\x01 \x01(\tB\x04\xe2\x41\x01\x02\x12.\n\x04\x66rom\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x04\xe2\x41\x01\x02\x12,\n\x02to\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x04\xe2\x41\x01\x02\"[\n&GetDividendsForeignIssuerReportRequest\x12\x15\n\x07task_id\x18\x01 \x01(\tB\x04\xe2\x41\x01\x02\x12\x11\n\x04page\x18\x02 \x01(\x05H\x00\x88\x01\x01\x42\x07\n\x05_page\"?\n,GenerateDividendsForeignIssuerReportResponse\x12\x0f\n\x07task_id\x18\x01 \x01(\t\"\xcd\x01\n\'GetDividendsForeignIssuerReportResponse\x12l\n\x1f\x64ividends_foreign_issuer_report\x18\x01 \x03(\x0b\x32\x43.tinkoff.public.invest.api.contract.v1.DividendsForeignIssuerReport\x12\x12\n\nitemsCount\x18\x02 \x01(\x05\x12\x12\n\npagesCount\x18\x03 \x01(\x05\x12\x0c\n\x04page\x18\x04 \x01(\x05\"\xc9\x04\n\x1c\x44ividendsForeignIssuerReport\x12/\n\x0brecord_date\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x30\n\x0cpayment_date\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x15\n\rsecurity_name\x18\x03 \x01(\t\x12\x0c\n\x04isin\x18\x04 \x01(\t\x12\x16\n\x0eissuer_country\x18\x05 \x01(\t\x12\x10\n\x08quantity\x18\x06 \x01(\x03\x12\x42\n\x08\x64ividend\x18\x07 \x01(\x0b\x32\x30.tinkoff.public.invest.api.contract.v1.Quotation\x12M\n\x13\x65xternal_commission\x18\x08 \x01(\x0b\x32\x30.tinkoff.public.invest.api.contract.v1.Quotation\x12H\n\x0e\x64ividend_gross\x18\t \x01(\x0b\x32\x30.tinkoff.public.invest.api.contract.v1.Quotation\x12=\n\x03tax\x18\n \x01(\x0b\x32\x30.tinkoff.public.invest.api.contract.v1.Quotation\x12I\n\x0f\x64ividend_amount\x18\x0b \x01(\x0b\x32\x30.tinkoff.public.invest.api.contract.v1.Quotation\x12\x10\n\x08\x63urrency\x18\x0c \x01(\t\"*\n\x16PortfolioStreamRequest\x12\x10\n\x08\x61\x63\x63ounts\x18\x01 \x03(\t\"\x8d\x02\n\x17PortfolioStreamResponse\x12[\n\rsubscriptions\x18\x01 \x01(\x0b\x32\x42.tinkoff.public.invest.api.contract.v1.PortfolioSubscriptionResultH\x00\x12M\n\tportfolio\x18\x02 \x01(\x0b\x32\x38.tinkoff.public.invest.api.contract.v1.PortfolioResponseH\x00\x12;\n\x04ping\x18\x03 \x01(\x0b\x32+.tinkoff.public.invest.api.contract.v1.PingH\x00\x42\t\n\x07payload\"\x99\x01\n\x1bPortfolioSubscriptionResult\x12R\n\x08\x61\x63\x63ounts\x18\x01 \x03(\x0b\x32@.tinkoff.public.invest.api.contract.v1.AccountSubscriptionStatus\x12\x13\n\x0btracking_id\x18\x07 \x01(\t\x12\x11\n\tstream_id\x18\x08 \x01(\t\"\x90\x01\n\x19\x41\x63\x63ountSubscriptionStatus\x12\x12\n\naccount_id\x18\x01 \x01(\t\x12_\n\x13subscription_status\x18\x06 \x01(\x0e\x32\x42.tinkoff.public.invest.api.contract.v1.PortfolioSubscriptionStatus\"\xd6\x04\n\x1cGetOperationsByCursorRequest\x12\x18\n\naccount_id\x18\x01 \x01(\tB\x04\xe2\x41\x01\x02\x12\x1a\n\rinstrument_id\x18\x02 \x01(\tH\x00\x88\x01\x01\x12-\n\x04\x66rom\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.TimestampH\x01\x88\x01\x01\x12+\n\x02to\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.TimestampH\x02\x88\x01\x01\x12\x13\n\x06\x63ursor\x18\x0b \x01(\tH\x03\x88\x01\x01\x12\x12\n\x05limit\x18\x0c \x01(\x05H\x04\x88\x01\x01\x12M\n\x0foperation_types\x18\r \x03(\x0e\x32\x34.tinkoff.public.invest.api.contract.v1.OperationType\x12I\n\x05state\x18\x0e \x01(\x0e\x32\x35.tinkoff.public.invest.api.contract.v1.OperationStateH\x05\x88\x01\x01\x12 \n\x13without_commissions\x18\x0f \x01(\x08H\x06\x88\x01\x01\x12\x1b\n\x0ewithout_trades\x18\x10 \x01(\x08H\x07\x88\x01\x01\x12\x1f\n\x12without_overnights\x18\x11 \x01(\x08H\x08\x88\x01\x01\x42\x10\n\x0e_instrument_idB\x07\n\x05_fromB\x05\n\x03_toB\t\n\x07_cursorB\x08\n\x06_limitB\x08\n\x06_stateB\x16\n\x14_without_commissionsB\x11\n\x0f_without_tradesB\x15\n\x13_without_overnights\"\x8b\x01\n\x1dGetOperationsByCursorResponse\x12\x10\n\x08has_next\x18\x01 \x01(\x08\x12\x13\n\x0bnext_cursor\x18\x02 \x01(\t\x12\x43\n\x05items\x18\x06 \x03(\x0b\x32\x34.tinkoff.public.invest.api.contract.v1.OperationItem\"\xc6\t\n\rOperationItem\x12\x0e\n\x06\x63ursor\x18\x01 \x01(\t\x12\x19\n\x11\x62roker_account_id\x18\x06 \x01(\t\x12\n\n\x02id\x18\x10 \x01(\t\x12\x1b\n\x13parent_operation_id\x18\x11 \x01(\t\x12\x0c\n\x04name\x18\x12 \x01(\t\x12(\n\x04\x64\x61te\x18\x15 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x42\n\x04type\x18\x16 \x01(\x0e\x32\x34.tinkoff.public.invest.api.contract.v1.OperationType\x12\x13\n\x0b\x64\x65scription\x18\x17 \x01(\t\x12\x44\n\x05state\x18\x18 \x01(\x0e\x32\x35.tinkoff.public.invest.api.contract.v1.OperationState\x12\x16\n\x0einstrument_uid\x18\x1f \x01(\t\x12\x0c\n\x04\x66igi\x18  \x01(\t\x12\x17\n\x0finstrument_type\x18! \x01(\t\x12N\n\x0finstrument_kind\x18\" \x01(\x0e\x32\x35.tinkoff.public.invest.api.contract.v1.InstrumentType\x12\x14\n\x0cposition_uid\x18# \x01(\t\x12\x42\n\x07payment\x18) \x01(\x0b\x32\x31.tinkoff.public.invest.api.contract.v1.MoneyValue\x12@\n\x05price\x18* \x01(\x0b\x32\x31.tinkoff.public.invest.api.contract.v1.MoneyValue\x12\x45\n\ncommission\x18+ \x01(\x0b\x32\x31.tinkoff.public.invest.api.contract.v1.MoneyValue\x12@\n\x05yield\x18, \x01(\x0b\x32\x31.tinkoff.public.invest.api.contract.v1.MoneyValue\x12H\n\x0eyield_relative\x18- \x01(\x0b\x32\x30.tinkoff.public.invest.api.contract.v1.Quotation\x12\x46\n\x0b\x61\x63\x63rued_int\x18. \x01(\x0b\x32\x31.tinkoff.public.invest.api.contract.v1.MoneyValue\x12\x10\n\x08quantity\x18\x33 \x01(\x03\x12\x15\n\rquantity_rest\x18\x34 \x01(\x03\x12\x15\n\rquantity_done\x18\x35 \x01(\x03\x12\x34\n\x10\x63\x61ncel_date_time\x18\x38 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x15\n\rcancel_reason\x18\x39 \x01(\t\x12O\n\x0btrades_info\x18= \x01(\x0b\x32:.tinkoff.public.invest.api.contract.v1.OperationItemTrades\x12\x11\n\tasset_uid\x18@ \x01(\t\x12S\n\x10\x63hild_operations\x18\x41 \x03(\x0b\x32\x39.tinkoff.public.invest.api.contract.v1.ChildOperationItem\"`\n\x13OperationItemTrades\x12I\n\x06trades\x18\x06 \x03(\x0b\x32\x39.tinkoff.public.invest.api.contract.v1.OperationItemTrade\"\xab\x02\n\x12OperationItemTrade\x12\x0b\n\x03num\x18\x01 \x01(\t\x12(\n\x04\x64\x61te\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x10\n\x08quantity\x18\x0b \x01(\x03\x12@\n\x05price\x18\x10 \x01(\x0b\x32\x31.tinkoff.public.invest.api.contract.v1.MoneyValue\x12@\n\x05yield\x18\x15 \x01(\x0b\x32\x31.tinkoff.public.invest.api.contract.v1.MoneyValue\x12H\n\x0eyield_relative\x18\x16 \x01(\x0b\x32\x30.tinkoff.public.invest.api.contract.v1.Quotation\"*\n\x16PositionsStreamRequest\x12\x10\n\x08\x61\x63\x63ounts\x18\x01 \x03(\t\"\x87\x02\n\x17PositionsStreamResponse\x12[\n\rsubscriptions\x18\x01 \x01(\x0b\x32\x42.tinkoff.public.invest.api.contract.v1.PositionsSubscriptionResultH\x00\x12G\n\x08position\x18\x02 \x01(\x0b\x32\x33.tinkoff.public.invest.api.contract.v1.PositionDataH\x00\x12;\n\x04ping\x18\x03 \x01(\x0b\x32+.tinkoff.public.invest.api.contract.v1.PingH\x00\x42\t\n\x07payload\"\x9b\x01\n\x1bPositionsSubscriptionResult\x12T\n\x08\x61\x63\x63ounts\x18\x01 \x03(\x0b\x32\x42.tinkoff.public.invest.api.contract.v1.PositionsSubscriptionStatus\x12\x13\n\x0btracking_id\x18\x07 \x01(\t\x12\x11\n\tstream_id\x18\x08 \x01(\t\"\x99\x01\n\x1bPositionsSubscriptionStatus\x12\x12\n\naccount_id\x18\x01 \x01(\t\x12\x66\n\x13subscription_status\x18\x06 \x01(\x0e\x32I.tinkoff.public.invest.api.contract.v1.PositionsAccountSubscriptionStatus\"\xf6\x02\n\x0cPositionData\x12\x12\n\naccount_id\x18\x01 \x01(\t\x12\x44\n\x05money\x18\x02 \x03(\x0b\x32\x35.tinkoff.public.invest.api.contract.v1.PositionsMoney\x12N\n\nsecurities\x18\x03 \x03(\x0b\x32:.tinkoff.public.invest.api.contract.v1.PositionsSecurities\x12H\n\x07\x66utures\x18\x04 \x03(\x0b\x32\x37.tinkoff.public.invest.api.contract.v1.PositionsFutures\x12H\n\x07options\x18\x05 \x03(\x0b\x32\x37.tinkoff.public.invest.api.contract.v1.PositionsOptions\x12(\n\x04\x64\x61te\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"\xa6\x01\n\x0ePositionsMoney\x12J\n\x0f\x61vailable_value\x18\x01 \x01(\x0b\x32\x31.tinkoff.public.invest.api.contract.v1.MoneyValue\x12H\n\rblocked_value\x18\x02 \x01(\x0b\x32\x31.tinkoff.public.invest.api.contract.v1.MoneyValue\"p\n\x12\x43hildOperationItem\x12\x16\n\x0einstrument_uid\x18\x01 \x01(\t\x12\x42\n\x07payment\x18\x02 \x01(\x0b\x32\x31.tinkoff.public.invest.api.contract.v1.MoneyValue*\x8b\x01\n\x0eOperationState\x12\x1f\n\x1bOPERATION_STATE_UNSPECIFIED\x10\x00\x12\x1c\n\x18OPERATION_STATE_EXECUTED\x10\x01\x12\x1c\n\x18OPERATION_STATE_CANCELED\x10\x02\x12\x1c\n\x18OPERATION_STATE_PROGRESS\x10\x03*\xe0\x10\n\rOperationType\x12\x1e\n\x1aOPERATION_TYPE_UNSPECIFIED\x10\x00\x12\x18\n\x14OPERATION_TYPE_INPUT\x10\x01\x12\x1b\n\x17OPERATION_TYPE_BOND_TAX\x10\x02\x12$\n OPERATION_TYPE_OUTPUT_SECURITIES\x10\x03\x12\x1c\n\x18OPERATION_TYPE_OVERNIGHT\x10\x04\x12\x16\n\x12OPERATION_TYPE_TAX\x10\x05\x12&\n\"OPERATION_TYPE_BOND_REPAYMENT_FULL\x10\x06\x12\x1c\n\x18OPERATION_TYPE_SELL_CARD\x10\x07\x12\x1f\n\x1bOPERATION_TYPE_DIVIDEND_TAX\x10\x08\x12\x19\n\x15OPERATION_TYPE_OUTPUT\x10\t\x12!\n\x1dOPERATION_TYPE_BOND_REPAYMENT\x10\n\x12!\n\x1dOPERATION_TYPE_TAX_CORRECTION\x10\x0b\x12\x1e\n\x1aOPERATION_TYPE_SERVICE_FEE\x10\x0c\x12\x1e\n\x1aOPERATION_TYPE_BENEFIT_TAX\x10\r\x12\x1d\n\x19OPERATION_TYPE_MARGIN_FEE\x10\x0e\x12\x16\n\x12OPERATION_TYPE_BUY\x10\x0f\x12\x1b\n\x17OPERATION_TYPE_BUY_CARD\x10\x10\x12#\n\x1fOPERATION_TYPE_INPUT_SECURITIES\x10\x11\x12\x1e\n\x1aOPERATION_TYPE_SELL_MARGIN\x10\x12\x12\x1d\n\x19OPERATION_TYPE_BROKER_FEE\x10\x13\x12\x1d\n\x19OPERATION_TYPE_BUY_MARGIN\x10\x14\x12\x1b\n\x17OPERATION_TYPE_DIVIDEND\x10\x15\x12\x17\n\x13OPERATION_TYPE_SELL\x10\x16\x12\x19\n\x15OPERATION_TYPE_COUPON\x10\x17\x12\x1e\n\x1aOPERATION_TYPE_SUCCESS_FEE\x10\x18\x12$\n OPERATION_TYPE_DIVIDEND_TRANSFER\x10\x19\x12%\n!OPERATION_TYPE_ACCRUING_VARMARGIN\x10\x1a\x12(\n$OPERATION_TYPE_WRITING_OFF_VARMARGIN\x10\x1b\x12\x1f\n\x1bOPERATION_TYPE_DELIVERY_BUY\x10\x1c\x12 \n\x1cOPERATION_TYPE_DELIVERY_SELL\x10\x1d\x12\x1d\n\x19OPERATION_TYPE_TRACK_MFEE\x10\x1e\x12\x1d\n\x19OPERATION_TYPE_TRACK_PFEE\x10\x1f\x12\"\n\x1eOPERATION_TYPE_TAX_PROGRESSIVE\x10 \x12\'\n#OPERATION_TYPE_BOND_TAX_PROGRESSIVE\x10!\x12+\n\'OPERATION_TYPE_DIVIDEND_TAX_PROGRESSIVE\x10\"\x12*\n&OPERATION_TYPE_BENEFIT_TAX_PROGRESSIVE\x10#\x12-\n)OPERATION_TYPE_TAX_CORRECTION_PROGRESSIVE\x10$\x12\'\n#OPERATION_TYPE_TAX_REPO_PROGRESSIVE\x10%\x12\x1b\n\x17OPERATION_TYPE_TAX_REPO\x10&\x12 \n\x1cOPERATION_TYPE_TAX_REPO_HOLD\x10\'\x12\"\n\x1eOPERATION_TYPE_TAX_REPO_REFUND\x10(\x12,\n(OPERATION_TYPE_TAX_REPO_HOLD_PROGRESSIVE\x10)\x12.\n*OPERATION_TYPE_TAX_REPO_REFUND_PROGRESSIVE\x10*\x12\x1a\n\x16OPERATION_TYPE_DIV_EXT\x10+\x12(\n$OPERATION_TYPE_TAX_CORRECTION_COUPON\x10,\x12\x1b\n\x17OPERATION_TYPE_CASH_FEE\x10-\x12\x1a\n\x16OPERATION_TYPE_OUT_FEE\x10.\x12!\n\x1dOPERATION_TYPE_OUT_STAMP_DUTY\x10/\x12\x1f\n\x1bOPERATION_TYPE_OUTPUT_SWIFT\x10\x32\x12\x1e\n\x1aOPERATION_TYPE_INPUT_SWIFT\x10\x33\x12#\n\x1fOPERATION_TYPE_OUTPUT_ACQUIRING\x10\x35\x12\"\n\x1eOPERATION_TYPE_INPUT_ACQUIRING\x10\x36\x12!\n\x1dOPERATION_TYPE_OUTPUT_PENALTY\x10\x37\x12\x1d\n\x19OPERATION_TYPE_ADVICE_FEE\x10\x38\x12\x1f\n\x1bOPERATION_TYPE_TRANS_IIS_BS\x10\x39\x12\x1e\n\x1aOPERATION_TYPE_TRANS_BS_BS\x10:\x12\x1c\n\x18OPERATION_TYPE_OUT_MULTI\x10;\x12\x1c\n\x18OPERATION_TYPE_INP_MULTI\x10<\x12!\n\x1dOPERATION_TYPE_OVER_PLACEMENT\x10=\x12\x1b\n\x17OPERATION_TYPE_OVER_COM\x10>\x12\x1e\n\x1aOPERATION_TYPE_OVER_INCOME\x10?\x12$\n OPERATION_TYPE_OPTION_EXPIRATION\x10@\x12$\n OPERATION_TYPE_FUTURE_EXPIRATION\x10\x41*\xde\x01\n\x1bPortfolioSubscriptionStatus\x12-\n)PORTFOLIO_SUBSCRIPTION_STATUS_UNSPECIFIED\x10\x00\x12)\n%PORTFOLIO_SUBSCRIPTION_STATUS_SUCCESS\x10\x01\x12\x33\n/PORTFOLIO_SUBSCRIPTION_STATUS_ACCOUNT_NOT_FOUND\x10\x02\x12\x30\n,PORTFOLIO_SUBSCRIPTION_STATUS_INTERNAL_ERROR\x10\x03*\xe5\x01\n\"PositionsAccountSubscriptionStatus\x12-\n)POSITIONS_SUBSCRIPTION_STATUS_UNSPECIFIED\x10\x00\x12)\n%POSITIONS_SUBSCRIPTION_STATUS_SUCCESS\x10\x01\x12\x33\n/POSITIONS_SUBSCRIPTION_STATUS_ACCOUNT_NOT_FOUND\x10\x02\x12\x30\n,POSITIONS_SUBSCRIPTION_STATUS_INTERNAL_ERROR\x10\x03\x32\x98\x08\n\x11OperationsService\x12\x84\x01\n\rGetOperations\x12\x38.tinkoff.public.invest.api.contract.v1.OperationsRequest\x1a\x39.tinkoff.public.invest.api.contract.v1.OperationsResponse\x12\x81\x01\n\x0cGetPortfolio\x12\x37.tinkoff.public.invest.api.contract.v1.PortfolioRequest\x1a\x38.tinkoff.public.invest.api.contract.v1.PortfolioResponse\x12\x81\x01\n\x0cGetPositions\x12\x37.tinkoff.public.invest.api.contract.v1.PositionsRequest\x1a\x38.tinkoff.public.invest.api.contract.v1.PositionsResponse\x12\x90\x01\n\x11GetWithdrawLimits\x12<.tinkoff.public.invest.api.contract.v1.WithdrawLimitsRequest\x1a=.tinkoff.public.invest.api.contract.v1.WithdrawLimitsResponse\x12\x8a\x01\n\x0fGetBrokerReport\x12:.tinkoff.public.invest.api.contract.v1.BrokerReportRequest\x1a;.tinkoff.public.invest.api.contract.v1.BrokerReportResponse\x12\xae\x01\n\x19GetDividendsForeignIssuer\x12G.tinkoff.public.invest.api.contract.v1.GetDividendsForeignIssuerRequest\x1aH.tinkoff.public.invest.api.contract.v1.GetDividendsForeignIssuerResponse\x12\xa2\x01\n\x15GetOperationsByCursor\x12\x43.tinkoff.public.invest.api.contract.v1.GetOperationsByCursorRequest\x1a\x44.tinkoff.public.invest.api.contract.v1.GetOperationsByCursorResponse2\xc3\x02\n\x17OperationsStreamService\x12\x92\x01\n\x0fPortfolioStream\x12=.tinkoff.public.invest.api.contract.v1.PortfolioStreamRequest\x1a>.tinkoff.public.invest.api.contract.v1.PortfolioStreamResponse0\x01\x12\x92\x01\n\x0fPositionsStream\x12=.tinkoff.public.invest.api.contract.v1.PositionsStreamRequest\x1a>.tinkoff.public.invest.api.contract.v1.PositionsStreamResponse0\x01\x42\x61\n\x1cru.tinkoff.piapi.contract.v1P\x01Z\x0c./;investapi\xa2\x02\x05TIAPI\xaa\x02\x14Tinkoff.InvestApi.V1\xca\x02\x11Tinkoff\\Invest\\V1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'tinvest.grpc.operations_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\034ru.tinkoff.piapi.contract.v1P\001Z\014./;investapi\242\002\005TIAPI\252\002\024Tinkoff.InvestApi.V1\312\002\021Tinkoff\\Invest\\V1'
  _globals['_OPERATIONSREQUEST'].fields_by_name['account_id']._loaded_options = None
  _globals['_OPERATIONSREQUEST'].fields_by_name['account_id']._serialized_options = b'\342A\001\002'
  _globals['_PORTFOLIOREQUEST'].fields_by_name['account_id']._loaded_options = None
  _globals['_PORTFOLIOREQUEST'].fields_by_name['account_id']._serialized_options = b'\342A\001\002'
  _globals['_POSITIONSREQUEST'].fields_by_name['account_id']._loaded_options = None
  _globals['_POSITIONSREQUEST'].fields_by_name['account_id']._serialized_options = b'\342A\001\002'
  _globals['_WITHDRAWLIMITSREQUEST'].fields_by_name['account_id']._loaded_options = None
  _globals['_WITHDRAWLIMITSREQUEST'].fields_by_name['account_id']._serialized_options = b'\342A\001\002'
  _globals['_PORTFOLIOPOSITION'].fields_by_name['average_position_price_pt']._loaded_options = None
  _globals['_PORTFOLIOPOSITION'].fields_by_name['average_position_price_pt']._serialized_options = b'\030\001'
  _globals['_PORTFOLIOPOSITION'].fields_by_name['quantity_lots']._loaded_options = None
  _globals['_PORTFOLIOPOSITION'].fields_by_name['quantity_lots']._serialized_options = b'\030\001'
  _globals['_GENERATEBROKERREPORTREQUEST'].fields_by_name['account_id']._loaded_options = None
  _globals['_GENERATEBROKERREPORTREQUEST'].fields_by_name['account_id']._serialized_options = b'\342A\001\002'
  _globals['_GENERATEBROKERREPORTREQUEST'].fields_by_name['from']._loaded_options = None
  _globals['_GENERATEBROKERREPORTREQUEST'].fields_by_name['from']._serialized_options = b'\342A\001\002'
  _globals['_GENERATEBROKERREPORTREQUEST'].fields_by_name['to']._loaded_options = None
  _globals['_GENERATEBROKERREPORTREQUEST'].fields_by_name['to']._serialized_options = b'\342A\001\002'
  _globals['_GETBROKERREPORTREQUEST'].fields_by_name['task_id']._loaded_options = None
  _globals['_GETBROKERREPORTREQUEST'].fields_by_name['task_id']._serialized_options = b'\342A\001\002'
  _globals['_GENERATEDIVIDENDSFOREIGNISSUERREPORTREQUEST'].fields_by_name['account_id']._loaded_options = None
  _globals['_GENERATEDIVIDENDSFOREIGNISSUERREPORTREQUEST'].fields_by_name['account_id']._serialized_options = b'\342A\001\002'
  _globals['_GENERATEDIVIDENDSFOREIGNISSUERREPORTREQUEST'].fields_by_name['from']._loaded_options = None
  _globals['_GENERATEDIVIDENDSFOREIGNISSUERREPORTREQUEST'].fields_by_name['from']._serialized_options = b'\342A\001\002'
  _globals['_GENERATEDIVIDENDSFOREIGNISSUERREPORTREQUEST'].fields_by_name['to']._loaded_options = None
  _globals['_GENERATEDIVIDENDSFOREIGNISSUERREPORTREQUEST'].fields_by_name['to']._serialized_options = b'\342A\001\002'
  _globals['_GETDIVIDENDSFOREIGNISSUERREPORTREQUEST'].fields_by_name['task_id']._loaded_options = None
  _globals['_GETDIVIDENDSFOREIGNISSUERREPORTREQUEST'].fields_by_name['task_id']._serialized_options = b'\342A\001\002'
  _globals['_GETOPERATIONSBYCURSORREQUEST'].fields_by_name['account_id']._loaded_options = None
  _globals['_GETOPERATIONSBYCURSORREQUEST'].fields_by_name['account_id']._serialized_options = b'\342A\001\002'
  _globals['_OPERATIONSTATE']._serialized_start=13334
  _globals['_OPERATIONSTATE']._serialized_end=13473
  _globals['_OPERATIONTYPE']._serialized_start=13476
  _globals['_OPERATIONTYPE']._serialized_end=15620
  _globals['_PORTFOLIOSUBSCRIPTIONSTATUS']._serialized_start=15623
  _globals['_PORTFOLIOSUBSCRIPTIONSTATUS']._serialized_end=15845
  _globals['_POSITIONSACCOUNTSUBSCRIPTIONSTATUS']._serialized_start=15848
  _globals['_POSITIONSACCOUNTSUBSCRIPTIONSTATUS']._serialized_end=16077
  _globals['_OPERATIONSREQUEST']._serialized_start=179
  _globals['_OPERATIONSREQUEST']._serialized_end=445
  _globals['_OPERATIONSRESPONSE']._serialized_start=447
  _globals['_OPERATIONSRESPONSE']._serialized_end=537
  _globals['_OPERATION']._serialized_start=540
  _globals['_OPERATION']._serialized_end=1249
  _globals['_OPERATIONTRADE']._serialized_start=1252
  _globals['_OPERATIONTRADE']._serialized_end=1417
  _globals['_PORTFOLIOREQUEST']._serialized_start=1420
  _globals['_PORTFOLIOREQUEST']._serialized_end=1619
  _globals['_PORTFOLIOREQUEST_CURRENCYREQUEST']._serialized_start=1562
  _globals['_PORTFOLIOREQUEST_CURRENCYREQUEST']._serialized_end=1606
  _globals['_PORTFOLIORESPONSE']._serialized_start=1622
  _globals['_PORTFOLIORESPONSE']._serialized_end=2545
  _globals['_POSITIONSREQUEST']._serialized_start=2547
  _globals['_POSITIONSREQUEST']._serialized_end=2591
  _globals['_POSITIONSRESPONSE']._serialized_start=2594
  _globals['_POSITIONSRESPONSE']._serialized_end=3011
  _globals['_WITHDRAWLIMITSREQUEST']._serialized_start=3013
  _globals['_WITHDRAWLIMITSREQUEST']._serialized_end=3062
  _globals['_WITHDRAWLIMITSRESPONSE']._serialized_start=3065
  _globals['_WITHDRAWLIMITSRESPONSE']._serialized_end=3301
  _globals['_PORTFOLIOPOSITION']._serialized_start=3304
  _globals['_PORTFOLIOPOSITION']._serialized_end=4272
  _globals['_VIRTUALPORTFOLIOPOSITION']._serialized_start=4275
  _globals['_VIRTUALPORTFOLIOPOSITION']._serialized_end=4901
  _globals['_POSITIONSSECURITIES']._serialized_start=4904
  _globals['_POSITIONSSECURITIES']._serialized_end=5070
  _globals['_POSITIONSFUTURES']._serialized_start=5072
  _globals['_POSITIONSFUTURES']._serialized_end=5184
  _globals['_POSITIONSOPTIONS']._serialized_start=5186
  _globals['_POSITIONSOPTIONS']._serialized_end=5284
  _globals['_BROKERREPORTREQUEST']._serialized_start=5287
  _globals['_BROKERREPORTREQUEST']._serialized_end=5529
  _globals['_BROKERREPORTRESPONSE']._serialized_start=5532
  _globals['_BROKERREPORTRESPONSE']._serialized_end=5779
  _globals['_GENERATEBROKERREPORTREQUEST']._serialized_start=5782
  _globals['_GENERATEBROKERREPORTREQUEST']._serialized_end=5931
  _globals['_GENERATEBROKERREPORTRESPONSE']._serialized_start=5933
  _globals['_GENERATEBROKERREPORTRESPONSE']._serialized_end=5980
  _globals['_GETBROKERREPORTREQUEST']._serialized_start=5982
  _globals['_GETBROKERREPORTREQUEST']._serialized_end=6057
  _globals['_GETBROKERREPORTRESPONSE']._serialized_start=6060
  _globals['_GETBROKERREPORTRESPONSE']._serialized_end=6215
  _globals['_BROKERREPORT']._serialized_start=6218
  _globals['_BROKERREPORT']._serialized_end=7332
  _globals['_GETDIVIDENDSFOREIGNISSUERREQUEST']._serialized_start=7335
  _globals['_GETDIVIDENDSFOREIGNISSUERREQUEST']._serialized_end=7631
  _globals['_GETDIVIDENDSFOREIGNISSUERRESPONSE']._serialized_start=7634
  _globals['_GETDIVIDENDSFOREIGNISSUERRESPONSE']._serialized_end=7938
  _globals['_GENERATEDIVIDENDSFOREIGNISSUERREPORTREQUEST']._serialized_start=7941
  _globals['_GENERATEDIVIDENDSFOREIGNISSUERREPORTREQUEST']._serialized_end=8106
  _globals['_GETDIVIDENDSFOREIGNISSUERREPORTREQUEST']._serialized_start=8108
  _globals['_GETDIVIDENDSFOREIGNISSUERREPORTREQUEST']._serialized_end=8199
  _globals['_GENERATEDIVIDENDSFOREIGNISSUERREPORTRESPONSE']._serialized_start=8201
  _globals['_GENERATEDIVIDENDSFOREIGNISSUERREPORTRESPONSE']._serialized_end=8264
  _globals['_GETDIVIDENDSFOREIGNISSUERREPORTRESPONSE']._serialized_start=8267
  _globals['_GETDIVIDENDSFOREIGNISSUERREPORTRESPONSE']._serialized_end=8472
  _globals['_DIVIDENDSFOREIGNISSUERREPORT']._serialized_start=8475
  _globals['_DIVIDENDSFOREIGNISSUERREPORT']._serialized_end=9060
  _globals['_PORTFOLIOSTREAMREQUEST']._serialized_start=9062
  _globals['_PORTFOLIOSTREAMREQUEST']._serialized_end=9104
  _globals['_PORTFOLIOSTREAMRESPONSE']._serialized_start=9107
  _globals['_PORTFOLIOSTREAMRESPONSE']._serialized_end=9376
  _globals['_PORTFOLIOSUBSCRIPTIONRESULT']._serialized_start=9379
  _globals['_PORTFOLIOSUBSCRIPTIONRESULT']._serialized_end=9532
  _globals['_ACCOUNTSUBSCRIPTIONSTATUS']._serialized_start=9535
  _globals['_ACCOUNTSUBSCRIPTIONSTATUS']._serialized_end=9679
  _globals['_GETOPERATIONSBYCURSORREQUEST']._serialized_start=9682
  _globals['_GETOPERATIONSBYCURSORREQUEST']._serialized_end=10280
  _globals['_GETOPERATIONSBYCURSORRESPONSE']._serialized_start=10283
  _globals['_GETOPERATIONSBYCURSORRESPONSE']._serialized_end=10422
  _globals['_OPERATIONITEM']._serialized_start=10425
  _globals['_OPERATIONITEM']._serialized_end=11647
  _globals['_OPERATIONITEMTRADES']._serialized_start=11649
  _globals['_OPERATIONITEMTRADES']._serialized_end=11745
  _globals['_OPERATIONITEMTRADE']._serialized_start=11748
  _globals['_OPERATIONITEMTRADE']._serialized_end=12047
  _globals['_POSITIONSSTREAMREQUEST']._serialized_start=12049
  _globals['_POSITIONSSTREAMREQUEST']._serialized_end=12091
  _globals['_POSITIONSSTREAMRESPONSE']._serialized_start=12094
  _globals['_POSITIONSSTREAMRESPONSE']._serialized_end=12357
  _globals['_POSITIONSSUBSCRIPTIONRESULT']._serialized_start=12360
  _globals['_POSITIONSSUBSCRIPTIONRESULT']._serialized_end=12515
  _globals['_POSITIONSSUBSCRIPTIONSTATUS']._serialized_start=12518
  _globals['_POSITIONSSUBSCRIPTIONSTATUS']._serialized_end=12671
  _globals['_POSITIONDATA']._serialized_start=12674
  _globals['_POSITIONDATA']._serialized_end=13048
  _globals['_POSITIONSMONEY']._serialized_start=13051
  _globals['_POSITIONSMONEY']._serialized_end=13217
  _globals['_CHILDOPERATIONITEM']._serialized_start=13219
  _globals['_CHILDOPERATIONITEM']._serialized_end=13331
  _globals['_OPERATIONSSERVICE']._serialized_start=16080
  _globals['_OPERATIONSSERVICE']._serialized_end=17128
  _globals['_OPERATIONSSTREAMSERVICE']._serialized_start=17131
  _globals['_OPERATIONSSTREAMSERVICE']._serialized_end=17454
# @@protoc_insertion_point(module_scope)
