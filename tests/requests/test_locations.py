import pytest


from pyclasher import (
    ClanBuilderBaseRanking,
    ClanCapitalRanking,
    ClanRanking,
    Location,
    Locations,
    PlayerBuilderBaseRanking,
    PlayerRanking,
)
from pyclasher.api.definitions import Location as LocationModel


@pytest.mark.asyncio(scope="session")
class TestLocations:
    async def test_locations__valid(self):
        locations = Locations()

        await locations.request()

        assert len(locations) >= 0

        for location in locations:
            assert isinstance(location, LocationModel)


@pytest.mark.asyncio(scope="session")
class TestLocation:
    @pytest.mark.parametrize(
        "location_id,location_name",
        [
            (
                32000000,
                "Europe",
            )
        ],
    )
    async def test_location__valid(self, location_id, location_name):
        location = Location(location_id)

        await location.request()

        assert location.id == location_id
        assert location.name == location_name
