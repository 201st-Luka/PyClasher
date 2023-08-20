import pytest

from pyclasher import GoldPassRequest
from api.models import Time


@pytest.mark.asyncio
async def test_goldpass(event_loop, pyclasher_client):
    goldpass = GoldPassRequest()

    await goldpass.request()

    assert isinstance(goldpass.to_dict(), dict)
    assert isinstance(goldpass.start_time, Time)
    assert isinstance(goldpass.end_time, Time)
