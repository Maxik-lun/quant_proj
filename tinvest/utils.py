from datetime import datetime, timezone, timedelta
from google.protobuf.timestamp_pb2 import Timestamp

def ts_to_datetime(value: Timestamp) -> datetime:
    ts = value.seconds + (value.nanos / 1e9)
    return datetime(1970, 1, 1, tzinfo=timezone.utc) + timedelta(seconds=ts)