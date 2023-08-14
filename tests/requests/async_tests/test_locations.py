import pytest

from pyclasher import LocationsRequest
from pyclasher.models import LocationList, Paging


@pytest.mark.asyncio
async def test_locations(event_loop, pyclasher_client):
    locations = LocationsRequest()

    await locations.request()

    assert isinstance(locations.to_dict(), dict)
    assert isinstance(locations.items, LocationList)
    assert isinstance(locations.paging, Paging)

    for location in locations:
        assert isinstance(location.to_dict(), dict)
        assert isinstance(location.id, int)
        assert isinstance(location.name, str)
