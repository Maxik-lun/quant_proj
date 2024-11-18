from tinvest.grpc import common_pb2 as _common_pb2
from tinvest.grpc import orders_pb2 as _orders_pb2
from tinvest.grpc import operations_pb2 as _operations_pb2
from tinvest.grpc import users_pb2 as _users_pb2
from tinvest.grpc.google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class OpenSandboxAccountRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class OpenSandboxAccountResponse(_message.Message):
    __slots__ = ("account_id",)
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    account_id: str
    def __init__(self, account_id: _Optional[str] = ...) -> None: ...

class CloseSandboxAccountRequest(_message.Message):
    __slots__ = ("account_id",)
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    account_id: str
    def __init__(self, account_id: _Optional[str] = ...) -> None: ...

class CloseSandboxAccountResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SandboxPayInRequest(_message.Message):
    __slots__ = ("account_id", "amount")
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    account_id: str
    amount: _common_pb2.MoneyValue
    def __init__(self, account_id: _Optional[str] = ..., amount: _Optional[_Union[_common_pb2.MoneyValue, _Mapping]] = ...) -> None: ...

class SandboxPayInResponse(_message.Message):
    __slots__ = ("balance",)
    BALANCE_FIELD_NUMBER: _ClassVar[int]
    balance: _common_pb2.MoneyValue
    def __init__(self, balance: _Optional[_Union[_common_pb2.MoneyValue, _Mapping]] = ...) -> None: ...
