import pytest

from pyclasher.api.models import LeagueList, Paging, IconUrls
from pyclasher import LeaguesRequest


@pytest.mark.asyncio
async def test_leagues(event_loop, pyclasher_client):
    leagues = LeaguesRequest()

    await leagues.request("test_client")

    assert isinstance(leagues.to_dict(), dict)
    assert isinstance(leagues.items, LeagueList)
    assert isinstance(leagues.paging, Paging)

    for league in leagues:
        assert isinstance(league.name, str)
        assert isinstance(league.id, int)
        assert isinstance(league.icon_urls, IconUrls)
