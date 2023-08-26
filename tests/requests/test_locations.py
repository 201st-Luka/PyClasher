from random import randint

import pytest

from pyclasher import MISSING
from pyclasher.api.requests import (
    LocationsRequest, LocationRequest, ClanRankingsRequest,
    ClanBuilderBaseRankingsRequest, PlayerRankingsRequest,
    PlayerBuilderBaseRankingsRequest, CapitalRankingsRequest
)
from pyclasher.api.models import (
    LocationList, Paging, PlayerRankingList, ClanRankingList,
    ClanCapitalRankingList, PlayerBuilderBaseRankingList,
    ClanBuilderBaseRankingList, League, PlayerRankingClan, Location,
    BadgeUrls, BuilderBaseLeague
)


@pytest.mark.asyncio
async def test_locations(event_loop, pyclasher_client):
    locations = LocationsRequest()

    await locations.request("test_client")

    assert isinstance(locations.to_dict(), dict)
    assert isinstance(locations.items, LocationList)
    assert isinstance(locations.paging, Paging)

    for location in locations:
        assert isinstance(location.to_dict(), dict)
        assert isinstance(location.id, int)
        assert isinstance(location.name, str)


@pytest.mark.parametrize(
    "location_id",
    [randint(32000007, 32000260) for _ in range(5)]
)
@pytest.mark.asyncio
async def test_location(pyclasher_client, location_id):
    location = LocationRequest(location_id)

    await location.request("test_client")

    assert isinstance(location.to_dict(), dict)
    assert location.location_id == location_id
    assert location.id == location_id
    assert isinstance(location.name, str)
    assert isinstance(location.id, int)
    assert (isinstance(location.country_code, str)
            or location.country_code is MISSING)
    assert location.localized_name is MISSING


@pytest.mark.parametrize(
    "location_id",
    [randint(32000007, 32000260) for _ in range(5)]
)
@pytest.mark.asyncio
async def test_player_rankings(pyclasher_client, location_id):
    rankings = PlayerRankingsRequest(location_id, limit=20)

    await rankings.request("test_client")

    assert isinstance(rankings.to_dict(), dict)
    assert rankings.location_id == location_id

    assert isinstance(rankings.items, PlayerRankingList)
    assert isinstance(rankings.paging, Paging)

    for rank in rankings:
        assert isinstance(rank.rank, int)
        assert isinstance(rank.previous_rank, int)
        assert isinstance(rank.name, str)
        assert (isinstance(rank.clan, PlayerRankingClan)
                or rank.clan is MISSING)
        assert isinstance(rank.league, League)
        assert isinstance(rank.attack_wins, int)
        assert isinstance(rank.trophies, int)
        assert isinstance(rank.defense_wins, int)
        assert isinstance(rank.exp_level, int)
        assert isinstance(rank.tag, str)


@pytest.mark.parametrize(
    "location_id",
    [randint(32000007, 32000260) for _ in range(5)]
)
@pytest.mark.asyncio
async def test_clan_rankings(pyclasher_client, location_id):
    rankings = ClanRankingsRequest(location_id, limit=20)

    await rankings.request("test_client")

    assert isinstance(rankings.to_dict(), dict)
    assert rankings.location_id == location_id

    assert isinstance(rankings.items, ClanRankingList)
    assert isinstance(rankings.paging, Paging)

    for rank in rankings:
        assert isinstance(rank.rank, int)
        assert isinstance(rank.previous_rank, int)
        assert isinstance(rank.name, str)
        assert isinstance(rank.tag, str)
        assert isinstance(rank.location, Location)
        assert isinstance(rank.members, int)
        assert isinstance(rank.clan_points, int)
        assert isinstance(rank.clan_level, int)
        assert isinstance(rank.badge_urls, BadgeUrls)


@pytest.mark.parametrize(
    "location_id",
    [randint(32000007, 32000260) for _ in range(5)]
)
@pytest.mark.asyncio
async def test_player_builder_base_rankings(pyclasher_client, location_id):
    rankings = PlayerBuilderBaseRankingsRequest(location_id, limit=20)

    await rankings.request("test_client")

    assert isinstance(rankings.to_dict(), dict)
    assert rankings.location_id == location_id

    assert isinstance(rankings.items, PlayerBuilderBaseRankingList)
    assert isinstance(rankings.paging, Paging)

    for rank in rankings:
        assert isinstance(rank.rank, int)
        assert isinstance(rank.previous_rank, int)
        assert isinstance(rank.name, str)
        assert isinstance(rank.tag, str)
        assert (isinstance(rank.clan, PlayerRankingClan)
                or rank.clan is MISSING)
        assert isinstance(rank.exp_level, int)
        assert isinstance(rank.versus_battle_wins, int)
        assert isinstance(rank.builder_base_trophies, int)
        assert isinstance(rank.builder_base_league, BuilderBaseLeague)


@pytest.mark.parametrize(
    "location_id",
    [randint(32000000, 32000260) for _ in range(5)]
)
@pytest.mark.asyncio
async def test_clan_builder_base_rankings(pyclasher_client, location_id):
    rankings = ClanBuilderBaseRankingsRequest(location_id, limit=20)

    await rankings.request("test_client")

    assert isinstance(rankings.to_dict(), dict)
    assert rankings.location_id == location_id

    assert isinstance(rankings.items, ClanBuilderBaseRankingList)
    assert isinstance(rankings.paging, Paging)

    for rank in rankings:
        assert rank.clan_points is MISSING
        assert isinstance(rank.clan_builder_base_points, int)


@pytest.mark.parametrize(
    "location_id",
    [randint(32000000, 32000260) for _ in range(5)]
)
@pytest.mark.asyncio
async def test_capital_rankings(pyclasher_client, location_id):
    rankings = CapitalRankingsRequest(location_id)

    await rankings.request("test_client")

    assert isinstance(rankings.to_dict(), dict)
    assert rankings.location_id == location_id

    assert isinstance(rankings.items, ClanCapitalRankingList)
    assert isinstance(rankings.paging, Paging)

    for rank in rankings:
        assert rank.clan_points is MISSING
        assert isinstance(rank.clan_capital_points, int)
