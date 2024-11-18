# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: tinvest/grpc/sandbox.proto
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
    'tinvest/grpc/sandbox.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from tinvest.grpc import common_pb2 as tinvest_dot_grpc_dot_common__pb2
from tinvest.grpc import orders_pb2 as tinvest_dot_grpc_dot_orders__pb2
from tinvest.grpc import operations_pb2 as tinvest_dot_grpc_dot_operations__pb2
from tinvest.grpc import users_pb2 as tinvest_dot_grpc_dot_users__pb2
from tinvest.grpc.google.api import field_behavior_pb2 as tinvest_dot_grpc_dot_google_dot_api_dot_field__behavior__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1atinvest/grpc/sandbox.proto\x12%tinkoff.public.invest.api.contract.v1\x1a\x19tinvest/grpc/common.proto\x1a\x19tinvest/grpc/orders.proto\x1a\x1dtinvest/grpc/operations.proto\x1a\x18tinvest/grpc/users.proto\x1a,tinvest/grpc/google/api/field_behavior.proto\"7\n\x19OpenSandboxAccountRequest\x12\x11\n\x04name\x18\x01 \x01(\tH\x00\x88\x01\x01\x42\x07\n\x05_name\"0\n\x1aOpenSandboxAccountResponse\x12\x12\n\naccount_id\x18\x01 \x01(\t\"6\n\x1a\x43loseSandboxAccountRequest\x12\x18\n\naccount_id\x18\x01 \x01(\tB\x04\xe2\x41\x01\x02\"\x1d\n\x1b\x43loseSandboxAccountResponse\"x\n\x13SandboxPayInRequest\x12\x18\n\naccount_id\x18\x01 \x01(\tB\x04\xe2\x41\x01\x02\x12G\n\x06\x61mount\x18\x02 \x01(\x0b\x32\x31.tinkoff.public.invest.api.contract.v1.MoneyValueB\x04\xe2\x41\x01\x02\"Z\n\x14SandboxPayInResponse\x12\x42\n\x07\x62\x61lance\x18\x01 \x01(\x0b\x32\x31.tinkoff.public.invest.api.contract.v1.MoneyValue2\x8d\x11\n\x0eSandboxService\x12\x99\x01\n\x12OpenSandboxAccount\x12@.tinkoff.public.invest.api.contract.v1.OpenSandboxAccountRequest\x1a\x41.tinkoff.public.invest.api.contract.v1.OpenSandboxAccountResponse\x12\x8b\x01\n\x12GetSandboxAccounts\x12\x39.tinkoff.public.invest.api.contract.v1.GetAccountsRequest\x1a:.tinkoff.public.invest.api.contract.v1.GetAccountsResponse\x12\x9c\x01\n\x13\x43loseSandboxAccount\x12\x41.tinkoff.public.invest.api.contract.v1.CloseSandboxAccountRequest\x1a\x42.tinkoff.public.invest.api.contract.v1.CloseSandboxAccountResponse\x12\x85\x01\n\x10PostSandboxOrder\x12\x37.tinkoff.public.invest.api.contract.v1.PostOrderRequest\x1a\x38.tinkoff.public.invest.api.contract.v1.PostOrderResponse\x12\x8b\x01\n\x13ReplaceSandboxOrder\x12:.tinkoff.public.invest.api.contract.v1.ReplaceOrderRequest\x1a\x38.tinkoff.public.invest.api.contract.v1.PostOrderResponse\x12\x85\x01\n\x10GetSandboxOrders\x12\x37.tinkoff.public.invest.api.contract.v1.GetOrdersRequest\x1a\x38.tinkoff.public.invest.api.contract.v1.GetOrdersResponse\x12\x8b\x01\n\x12\x43\x61ncelSandboxOrder\x12\x39.tinkoff.public.invest.api.contract.v1.CancelOrderRequest\x1a:.tinkoff.public.invest.api.contract.v1.CancelOrderResponse\x12\x86\x01\n\x14GetSandboxOrderState\x12;.tinkoff.public.invest.api.contract.v1.GetOrderStateRequest\x1a\x31.tinkoff.public.invest.api.contract.v1.OrderState\x12\x88\x01\n\x13GetSandboxPositions\x12\x37.tinkoff.public.invest.api.contract.v1.PositionsRequest\x1a\x38.tinkoff.public.invest.api.contract.v1.PositionsResponse\x12\x8b\x01\n\x14GetSandboxOperations\x12\x38.tinkoff.public.invest.api.contract.v1.OperationsRequest\x1a\x39.tinkoff.public.invest.api.contract.v1.OperationsResponse\x12\xa9\x01\n\x1cGetSandboxOperationsByCursor\x12\x43.tinkoff.public.invest.api.contract.v1.GetOperationsByCursorRequest\x1a\x44.tinkoff.public.invest.api.contract.v1.GetOperationsByCursorResponse\x12\x88\x01\n\x13GetSandboxPortfolio\x12\x37.tinkoff.public.invest.api.contract.v1.PortfolioRequest\x1a\x38.tinkoff.public.invest.api.contract.v1.PortfolioResponse\x12\x87\x01\n\x0cSandboxPayIn\x12:.tinkoff.public.invest.api.contract.v1.SandboxPayInRequest\x1a;.tinkoff.public.invest.api.contract.v1.SandboxPayInResponse\x12\x97\x01\n\x18GetSandboxWithdrawLimits\x12<.tinkoff.public.invest.api.contract.v1.WithdrawLimitsRequest\x1a=.tinkoff.public.invest.api.contract.v1.WithdrawLimitsResponse\x12\x88\x01\n\x11GetSandboxMaxLots\x12\x38.tinkoff.public.invest.api.contract.v1.GetMaxLotsRequest\x1a\x39.tinkoff.public.invest.api.contract.v1.GetMaxLotsResponseBa\n\x1cru.tinkoff.piapi.contract.v1P\x01Z\x0c./;investapi\xa2\x02\x05TIAPI\xaa\x02\x14Tinkoff.InvestApi.V1\xca\x02\x11Tinkoff\\Invest\\V1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'tinvest.grpc.sandbox_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\034ru.tinkoff.piapi.contract.v1P\001Z\014./;investapi\242\002\005TIAPI\252\002\024Tinkoff.InvestApi.V1\312\002\021Tinkoff\\Invest\\V1'
  _globals['_CLOSESANDBOXACCOUNTREQUEST'].fields_by_name['account_id']._loaded_options = None
  _globals['_CLOSESANDBOXACCOUNTREQUEST'].fields_by_name['account_id']._serialized_options = b'\342A\001\002'
  _globals['_SANDBOXPAYINREQUEST'].fields_by_name['account_id']._loaded_options = None
  _globals['_SANDBOXPAYINREQUEST'].fields_by_name['account_id']._serialized_options = b'\342A\001\002'
  _globals['_SANDBOXPAYINREQUEST'].fields_by_name['amount']._loaded_options = None
  _globals['_SANDBOXPAYINREQUEST'].fields_by_name['amount']._serialized_options = b'\342A\001\002'
  _globals['_OPENSANDBOXACCOUNTREQUEST']._serialized_start=226
  _globals['_OPENSANDBOXACCOUNTREQUEST']._serialized_end=281
  _globals['_OPENSANDBOXACCOUNTRESPONSE']._serialized_start=283
  _globals['_OPENSANDBOXACCOUNTRESPONSE']._serialized_end=331
  _globals['_CLOSESANDBOXACCOUNTREQUEST']._serialized_start=333
  _globals['_CLOSESANDBOXACCOUNTREQUEST']._serialized_end=387
  _globals['_CLOSESANDBOXACCOUNTRESPONSE']._serialized_start=389
  _globals['_CLOSESANDBOXACCOUNTRESPONSE']._serialized_end=418
  _globals['_SANDBOXPAYINREQUEST']._serialized_start=420
  _globals['_SANDBOXPAYINREQUEST']._serialized_end=540
  _globals['_SANDBOXPAYINRESPONSE']._serialized_start=542
  _globals['_SANDBOXPAYINRESPONSE']._serialized_end=632
  _globals['_SANDBOXSERVICE']._serialized_start=635
  _globals['_SANDBOXSERVICE']._serialized_end=2824
# @@protoc_insertion_point(module_scope)