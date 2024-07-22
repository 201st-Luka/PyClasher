import pytest

from pyclasher import (
    CapitalRaidSeasons,
    Clan,
    ClanMembers,
    ClanWarLeagueGroup,
    ClanWarLeagueWar,
    ClanWarLog,
    CurrentWar,
    SearchClans,
    NotFound,
    BadRequest,
    Forbidden,
)
from pyclasher.api.definitions import (
    ClanCapitalRaidSeason,
    ClanMember,
    ClanWarLogEntry,
    Clan as ClanModel,
)
from pyclasher.api.definitions.BaseClan import BaseClan
from pyclasher.api.enums import LeagueWarState

from ..constants import TEST_CLAN_TAG, TEST_CWL_WAR_TAG, TEST_CLAN_TAG2, TEST_CLAN_NAME


@pytest.mark.asyncio(scope="session")
class TestCapitalRaisSeasons:
    async def test_capital_raid_seasons__valid(self, pyclasher_client):
        capital_raid_seasons = CapitalRaidSeasons(TEST_CLAN_TAG)

        await capital_raid_seasons.request()

        assert len(capital_raid_seasons) >= 0

        for season in capital_raid_seasons:
            assert isinstance(season, ClanCapitalRaidSeason)
            assert season.start_time is not None

    async def test_capital_raid_seasons__not_found(self, pyclasher_client):
        capital_raid_seasons = CapitalRaidSeasons("INVALID_TAG")

        with pytest.raises(NotFound):
            await capital_raid_seasons.request()


@pytest.mark.asyncio(scope="session")
class TestClan:
    async def test_clan__valid(self, pyclasher_client):
        clan = Clan(TEST_CLAN_TAG)

        await clan.request()

        assert isinstance(clan, BaseClan)
        assert clan.tag == TEST_CLAN_TAG

    async def test_clan__not_found(self, pyclasher_client):
        clan = Clan("INVALID_TAG")

        with pytest.raises(NotFound):
            await clan.request()

    async def test_clan__bad_request(self, pyclasher_client):
        clan = Clan("")

        with pytest.raises(BadRequest):
            await clan.request()


@pytest.mark.asyncio(scope="session")
class TestClanMembers:
    async def test_clan_members__valid(self, pyclasher_client):
        clan_members = ClanMembers(TEST_CLAN_TAG)

        await clan_members.request()

        assert len(clan_members) >= 0

        for member in clan_members:
            assert isinstance(member, ClanMember)
            assert member.tag is not None

    async def test_clan_members__not_found(self, pyclasher_client):
        clan_members = ClanMembers("INVALID_TAG")

        with pytest.raises(NotFound):
            await clan_members.request()


@pytest.mark.asyncio(scope="session")
class TestClanWarLeagueGroup:
    # it is not always possible to test this endpoint because the test requires the clan to be in a clan war league
    # which is not always the case
    # async def test_clan_war_league_group__valid(self, pyclasher_client):
    #     clan_war_league_group = ClanWarLeagueGroup(TEST_CLAN_TAG)
    #
    #     await clan_war_league_group.request()
    #
    #     assert clan_war_league_group.tag == TEST_CLAN_TAG

    async def test_clan_war_league_group__not_found(self, pyclasher_client):
        clan_war_league_group = ClanWarLeagueGroup("INVALID_TAG")

        with pytest.raises(NotFound):
            await clan_war_league_group.request()


@pytest.mark.asyncio(scope="session")
class TestClanWarLeagueWar:
    async def test_clan_war_league_war__valid(self, pyclasher_client):
        clan_war_league_war = ClanWarLeagueWar(TEST_CWL_WAR_TAG)

        await clan_war_league_war.request()

        print(clan_war_league_war.state)

        assert clan_war_league_war.state == LeagueWarState.NOT_IN_WAR  # old war tag -> notInWar

    async def test_clan_war_league_war__not_found(self, pyclasher_client):
        clan_war_league_war = ClanWarLeagueWar("INVALID_TAG")

        with pytest.raises(NotFound):
            await clan_war_league_war.request()


@pytest.mark.asyncio(scope="session")
class TestClanWarLog:
    async def test_clan_war_log__valid(self, pyclasher_client):
        clan_war_log = ClanWarLog(TEST_CLAN_TAG2)

        await clan_war_log.request()

        assert len(clan_war_log) >= 0

        for war in clan_war_log:
            assert isinstance(war, ClanWarLogEntry)
            assert war.clan.tag == TEST_CLAN_TAG2

    async def test_clan_war_log__not_found(self, pyclasher_client):
        clan_war_log = ClanWarLog("INVALID_TAG")

        with pytest.raises(NotFound):
            await clan_war_log.request()

    async def test_clan_war_log__forbidden(self, pyclasher_client):
        clan_war_log = ClanWarLog(TEST_CLAN_TAG)

        with pytest.raises(Forbidden):
            await clan_war_log.request()


@pytest.mark.asyncio(scope="session")
class TestCurrentWar:
    async def test_current_war__valid(self, pyclasher_client):
        current_war = CurrentWar(TEST_CLAN_TAG2)

        await current_war.request()

        assert current_war.clan.tag == TEST_CLAN_TAG2

    async def test_current_war__not_found(self, pyclasher_client):
        current_war = CurrentWar("INVALID_TAG")

        with pytest.raises(NotFound):
            await current_war.request()

    async def test_current_war__forbidden(self, pyclasher_client):
        current_war = CurrentWar(TEST_CLAN_TAG)

        with pytest.raises(Forbidden):
            await current_war.request()


@pytest.mark.asyncio(scope="session")
class TestSearchClans:
    async def test_search_clans__valid(self, pyclasher_client):
        search_clans = SearchClans(name=TEST_CLAN_NAME)

        await search_clans.request()

        assert len(search_clans) >= 0

        for clan in search_clans:
            assert isinstance(clan, ClanModel)

    async def test_search_clans__bad_request(self, pyclasher_client):
        search_clans = SearchClans()

        with pytest.raises(BadRequest):
            await search_clans.request()
