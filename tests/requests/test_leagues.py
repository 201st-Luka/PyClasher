import pytest


from pyclasher import (
    BuilderBaseLeague,
    BuilderBaseLeagues,
    CapitalLeague,
    CapitalLeagues,
    League,
    Leagues,
    WarLeague,
    WarLeagues,
    BadRequest,
)
from pyclasher.api.definitions import (
    League as LeagueModel,
    WarLeague as WarLeagueModel,
    BuilderBaseLeague as BuilderBaseLeagueModel,
    CapitalLeague as CapitalLeagueModel,
)
from pyclasher.api.definitions.BaseLeague import BaseLeague


@pytest.mark.asyncio(scope="session")
class TestBuilderBaseLeagues:
    async def test_builder_base_leagues__valid(self):
        builder_base_leagues = BuilderBaseLeagues()

        await builder_base_leagues.request()

        assert len(builder_base_leagues) >= 0

        for builder_base_league in builder_base_leagues:
            assert isinstance(builder_base_league, BaseLeague)
            assert isinstance(builder_base_league, BuilderBaseLeagueModel)


@pytest.mark.asyncio(scope="session")
class TestCapitalLeagues:
    async def test_capital_leagues__valid(self):
        capital_leagues = CapitalLeagues()

        await capital_leagues.request()

        assert len(capital_leagues) >= 0

        for capital_league in capital_leagues:
            assert isinstance(capital_league, BaseLeague)
            assert isinstance(capital_league, CapitalLeagueModel)


@pytest.mark.asyncio(scope="session")
class TestLeagues:
    async def test_leagues__valid(self):
        leagues = Leagues()

        await leagues.request()

        assert len(leagues) >= 0

        for league in leagues:
            assert isinstance(league, BaseLeague)
            assert isinstance(league, LeagueModel)


@pytest.mark.asyncio(scope="session")
class TestWarLeagues:
    async def test_war_leagues__valid(self):
        war_leagues = WarLeagues()

        await war_leagues.request()

        assert len(war_leagues) >= 0

        for war_league in war_leagues:
            assert isinstance(war_league, BaseLeague)
            assert isinstance(war_league, WarLeagueModel)


@pytest.mark.asyncio(scope="session")
class TestBuilderBaseLeague:
    @pytest.mark.parametrize(
        "league_id, league_name",
        [
            (
                44000000,
                "Wood League V",
            )
        ],
    )
    async def test_builder_base_league__valid(self, league_id, league_name):
        builder_base_league = BuilderBaseLeague(league_id)

        await builder_base_league.request()

        assert isinstance(builder_base_league, BaseLeague)
        assert isinstance(builder_base_league, BuilderBaseLeagueModel)
        assert builder_base_league.id == league_id
        assert builder_base_league.name == league_name

    @pytest.mark.parametrize("league_id", ["invalid", 0])
    async def test_builder_base_league__bad_request(self, league_id):
        builder_base_league = BuilderBaseLeague(league_id)

        with pytest.raises(BadRequest):
            await builder_base_league.request()


@pytest.mark.asyncio(scope="session")
class TestCapitalLeague:
    @pytest.mark.parametrize(
        "league_id, league_name",
        [
            (
                85000000,
                "Unranked",
            )
        ],
    )
    async def test_capital_league__valid(self, league_id, league_name):
        capital_league = CapitalLeague(league_id)

        await capital_league.request()

        assert isinstance(capital_league, BaseLeague)
        assert isinstance(capital_league, CapitalLeagueModel)
        assert capital_league.id == league_id
        assert capital_league.name == league_name

    @pytest.mark.parametrize("league_id", ["invalid", 0])
    async def test_capital_league__bad_request(self, league_id):
        capital_league = CapitalLeague(league_id)

        with pytest.raises(BadRequest):
            await capital_league.request()


@pytest.mark.asyncio(scope="session")
class TestLeague:
    @pytest.mark.parametrize(
        "league_id, league_name",
        [
            (
                29000000,
                "Unranked",
            )
        ],
    )
    async def test_league__valid(self, league_id, league_name):
        league = League(league_id)

        await league.request()

        assert isinstance(league, BaseLeague)
        assert isinstance(league, LeagueModel)
        assert league.id == league_id
        assert league.name == league_name

    @pytest.mark.parametrize("league_id", ["invalid", 0])
    async def test_league__bad_request(self, league_id):
        league = League(league_id)

        with pytest.raises(BadRequest):
            await league.request()


@pytest.mark.asyncio(scope="session")
class TestWarLeague:
    @pytest.mark.parametrize(
        "league_id, league_name",
        [
            (
                48000000,
                "Unranked",
            )
        ],
    )
    async def test_war_league__valid(self, league_id, league_name):
        war_league = WarLeague(league_id)

        await war_league.request()

        assert isinstance(war_league, BaseLeague)
        assert isinstance(war_league, WarLeagueModel)
        assert war_league.id == league_id
        assert war_league.name == league_name

    @pytest.mark.parametrize("league_id", ["invalid", 0])
    async def test_war_league__bad_request(self, league_id):
        war_league = WarLeague(league_id)

        with pytest.raises(BadRequest):
            await war_league.request()
