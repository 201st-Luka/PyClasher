import pytest
from random import randint, choices

from pyclasher import MISSING
from pyclasher.api.models import (
    LeagueList, CapitalLeagueList, BuilderBaseLeagueList, WarLeagueList,
    Paging, IconUrls, LeagueSeasonList, LeagueSeason, PlayerRankingList,
    PlayerRankingClan, Season
)
from pyclasher.api.requests import (
    LeaguesRequest, CapitalLeaguesRequest, BuilderBaseLeaguesRequest,
    WarLeaguesRequest, LeagueRequest, CapitalLeagueRequest,
    BuilderBaseLeagueRequest, WarLeagueRequest, LeagueSeasonRequest,
    LeagueSeasonsRequest
)


Seasons = (
    "2015-07", "2015-08", "2015-09", "2015-10", "2015-11", "2015-12",
    "2016-01", "2016-02", "2016-03", "2016-04", "2016-05", "2016-06",
    "2016-07", "2016-08", "2016-09", "2016-10", "2016-11", "2016-12",
    "2017-01", "2017-02", "2017-03", "2017-04", "2017-05", "2017-06",
    "2017-07", "2017-08", "2017-09", "2017-10", "2017-11", "2017-12",
    "2018-01", "2018-02", "2018-03", "2018-04", "2018-05", "2018-06",
    "2018-07", "2018-08", "2018-09", "2018-10", "2018-11", "2018-12",
    "2019-01", "2019-02", "2019-03", "2019-04", "2019-05", "2019-06",
    "2019-07", "2019-08", "2019-09", "2019-10", "2019-11", "2019-12",
    "2020-01", "2020-02", "2020-03", "2020-04", "2020-05", "2020-06",
    "2020-07", "2020-08", "2020-09", "2020-10", "2020-11", "2020-12",
    "2021-01", "2021-02", "2021-03", "2021-04", "2021-05", "2021-06",
    "2021-07", "2021-08", "2021-09", "2021-10", "2021-11", "2021-12",
    "2022-01", "2022-02", "2022-03", "2022-04", "2022-05", "2022-06",
    "2022-07", "2022-08", "2022-09", "2022-10", "2022-11", "2022-12",
    "2023-01", "2023-02", "2023-03", "2023-04", "2023-05", "2023-06",
    "2023-07",
)


@pytest.mark.asyncio
async def test_leagues(pyclasher_client):
    leagues = LeaguesRequest()

    await leagues.request("test_client")

    assert isinstance(leagues.to_dict(), dict)
    assert isinstance(leagues.items, LeagueList)
    assert isinstance(leagues.paging, Paging)

    for league in leagues:
        assert isinstance(league.name, str)
        assert isinstance(league.id, int)
        assert isinstance(league.icon_urls, IconUrls)


@pytest.mark.asyncio
async def test_capital_leagues(pyclasher_client):
    capital_leagues = CapitalLeaguesRequest()

    await capital_leagues.request("test_client")

    assert isinstance(capital_leagues.to_dict(), dict)
    assert isinstance(capital_leagues.items, CapitalLeagueList)
    assert isinstance(capital_leagues.paging, Paging)

    for capital_league in capital_leagues:
        assert isinstance(capital_league.name, str)
        assert isinstance(capital_league.id, int)


@pytest.mark.asyncio
async def test_builder_base_leagues(pyclasher_client):
    builder_base_leagues = BuilderBaseLeaguesRequest()

    await builder_base_leagues.request("test_client")

    assert isinstance(builder_base_leagues.to_dict(), dict)
    assert isinstance(builder_base_leagues.items, BuilderBaseLeagueList)
    assert isinstance(builder_base_leagues.paging, Paging)

    for builder_base_league in builder_base_leagues:
        assert isinstance(builder_base_league.name, str)
        assert isinstance(builder_base_league.id, int)


@pytest.mark.asyncio
async def test_war_leagues(pyclasher_client):
    war_leagues = WarLeaguesRequest()

    await war_leagues.request("test_client")

    assert isinstance(war_leagues.to_dict(), dict)
    assert isinstance(war_leagues.items, WarLeagueList)
    assert isinstance(war_leagues.paging, Paging)

    for war_league in war_leagues:
        assert isinstance(war_league.name, str)
        assert isinstance(war_league.id, int)


@pytest.mark.parametrize(
    "league_id",
    [randint(29000000, 29000022) for _ in range(10)]
)
@pytest.mark.asyncio
async def test_league(pyclasher_client, league_id):
    league = LeagueRequest(league_id)

    await league.request("test_client")

    assert isinstance(league.to_dict(), dict)
    assert league.league_id == league_id
    assert league.id == league_id
    assert isinstance(league.id, int)
    assert isinstance(league.name, str)
    assert isinstance(league.icon_urls, IconUrls)


@pytest.mark.parametrize(
    "league_id",
    [randint(85000000, 85000022) for _ in range(5)]
)
@pytest.mark.asyncio
async def test_capital_league(pyclasher_client, league_id):
    capital_league = CapitalLeagueRequest(league_id)

    await capital_league.request("test_client")

    assert isinstance(capital_league.to_dict(), dict)
    assert capital_league.league_id == league_id
    assert capital_league.id == league_id
    assert isinstance(capital_league.id, int)
    assert isinstance(capital_league.name, str)


@pytest.mark.parametrize(
    "league_id",
    [randint(44000000, 44000041) for _ in range(5)]
)
@pytest.mark.asyncio
async def test_builder_base_league(pyclasher_client, league_id):
    builder_base_league = BuilderBaseLeagueRequest(league_id)

    await builder_base_league.request("test_client")

    assert isinstance(builder_base_league.to_dict(), dict)
    assert builder_base_league.league_id == league_id
    assert builder_base_league.id == league_id
    assert isinstance(builder_base_league.id, int)
    assert isinstance(builder_base_league.name, str)


@pytest.mark.parametrize(
    "league_id",
    [randint(48000000, 48000018) for _ in range(5)]
)
@pytest.mark.asyncio
async def test_war_league(pyclasher_client, league_id):
    war_league = WarLeagueRequest(league_id)

    await war_league.request("test_client")

    assert isinstance(war_league.to_dict(), dict)
    assert war_league.league_id == league_id
    assert war_league.id == league_id
    assert isinstance(war_league.id, int)
    assert isinstance(war_league.name, str)


@pytest.mark.asyncio
async def test_league_seasons(pyclasher_client):
    seasons = LeagueSeasonsRequest(29000022)

    await seasons.request("test_client")

    assert isinstance(seasons.to_dict(), dict)
    assert isinstance(seasons.items, LeagueSeasonList)
    assert isinstance(seasons.paging, Paging)

    for season in seasons:
        assert isinstance(season, LeagueSeason)
        assert isinstance(season.to_dict(), dict)
        assert isinstance(season.id, str)


@pytest.mark.parametrize(
    "season",
    choices(Seasons, k=5)
)
@pytest.mark.asyncio
async def test_league_season(pyclasher_client, season):
    league_season = LeagueSeasonRequest(29000022, season, limit=20)

    await league_season.request("test_client")

    assert isinstance(league_season.to_dict(), dict)
    assert league_season.league_id == 29000022
    assert league_season.season_id == Season.from_str(season)
    assert isinstance(league_season.items, PlayerRankingList)
    assert isinstance(league_season.paging, Paging)

    for ranking in league_season:
        assert isinstance(ranking.to_dict(), dict)
        assert isinstance(ranking.name, str)
        assert ranking.league == MISSING
        assert isinstance(ranking.rank, int)
        assert isinstance(ranking.tag, str)
        assert isinstance(ranking.exp_level, int)
        assert isinstance(ranking.defense_wins, int)
        assert isinstance(ranking.trophies, int)
        assert isinstance(ranking.attack_wins, int)
        assert (isinstance(ranking.clan, PlayerRankingClan)
                or ranking.clan == MISSING)
        assert ranking.previous_rank == MISSING
