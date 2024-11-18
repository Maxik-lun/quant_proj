import logging
from datetime import datetime
from abc import ABC
from typing import Any, Generator, Iterable, Iterator, List, Optional, Tuple
from schemas import (
    InstrumentIdType, InstrumentRequest, 
    BondResponse, BondsResponse,
    ShareResponse, SharesResponse
)

import grpc
from .grpc import (
    instruments_pb2,
    instruments_pb2_grpc,
    marketdata_pb2,
    marketdata_pb2_grpc,
    operations_pb2,
    operations_pb2_grpc,
    orders_pb2,
    orders_pb2_grpc,
    sandbox_pb2,
    sandbox_pb2_grpc,
    stoporders_pb2,
    stoporders_pb2_grpc,
    users_pb2,
    users_pb2_grpc,
)
# from .logging import get_tracking_id_from_call, log_request
# from .metadata import get_metadata

def get_metadata(token: str, app_name: str = 'test-app') -> List[Tuple[str, str]]:
    return [("authorization", f"Bearer {token}"), ("x-app-name", app_name)]

class Service(ABC):
    _stub_factory: Any

    def __init__(self, channel, metadata):
        self.stub = self._stub_factory(channel)
        self.metadata = metadata

class Services:
    def __init__(
        self,
        channel: grpc.Channel,
        token: str,
        sandbox_token: Optional[str] = None,
        app_name: str = 'test-app',
    ) -> None:
        metadata = get_metadata(token, app_name)
        sandbox_metadata = get_metadata(sandbox_token or token, app_name)
        self.instruments = InstrumentsService(channel, metadata)
        # self.market_data = MarketDataService(channel, metadata)
        # self.market_data_stream = MarketDataStreamService(channel, metadata)
        # self.operations = OperationsService(channel, metadata)
        # self.operations_stream = OperationsStreamService(channel, metadata)
        # self.orders_stream = OrdersStreamService(channel, metadata)
        # self.orders = OrdersService(channel, metadata)
        # self.users = UsersService(channel, metadata)
        # self.sandbox = SandboxService(channel, sandbox_metadata)
        # self.stop_orders = StopOrdersService(channel, metadata)

class InstrumentsService(Service):
    _stub_factory = instruments_pb2_grpc.InstrumentsServiceStub