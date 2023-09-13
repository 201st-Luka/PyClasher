import pytest

from pyclasher import (
    ClanRequest, ClanMembersRequest, Missing, ClanCurrentWarRequest,
    ClanWarLogRequest, ClanSearchRequest, ClanCapitalRaidSeasonsRequest,
    ClanCurrentwarLeaguegroupRequest,
    ClanWarleaguesWarsRequest,
    MISSING, NotFound
)
from pyclasher.api.models import (
    ClanType, WarFrequency, BadgeUrls, WarLeague, CapitalLeague, Language,
    ClanCapital, LabelList, Location, ClanMemberList, Paging,
    BuilderBaseLeague, League, PlayerHouse, ClanRole, ClanMember,
    ClanWarState, WarClan, Time, ClanWarLog, ClanWarResult, ClanList,
    ClanCapitalRaidSeasons, ClanCapitalRaidSeasonMemberList,
    ClanCapitalRaidSeasonAttackLogList, ClanCapitalRaidSeasonDefenseLogList,
    ClanWarLeagueGroupState, ClanWarLeagueClanList, ClanWarLeagueRoundList
)

from ..constants import TEST_CLAN_TAG, TEST_CLAN_NAME


@pytest.mark.asyncio
async def test_clan(event_loop, pyclasher_client):
    clan = ClanRequest(TEST_CLAN_TAG)

    await clan.request("test_client")

    assert isinstance(clan.to_dict(), dict)
    assert clan.tag == clan.clan_tag == TEST_CLAN_TAG
    assert isinstance(clan.clan_level, int)
    assert isinstance(clan.name, str)
    assert isinstance(clan.type, ClanType)
    assert isinstance(clan.war_ties, int)
    assert isinstance(clan.war_losses, int)
    assert isinstance(clan.war_wins, int)
    assert isinstance(clan.war_win_streak, int)
    assert isinstance(clan.total_wars, int)
    assert clan.total_wars == clan.war_wins + clan.war_ties + clan.war_losses
    assert isinstance(clan.war_frequency, WarFrequency)
    assert isinstance(clan.badge_urls, BadgeUrls)
    assert isinstance(clan.war_league, WarLeague)
    assert isinstance(clan.capital_league, CapitalLeague)
    assert isinstance(clan.chat_language, Language)
    assert isinstance(clan.clan_builder_base_points, int)
    assert isinstance(clan.clan_capital, ClanCapital)
    assert isinstance(clan.clan_capital_points, int)
    assert isinstance(clan.clan_points, int)
    assert isinstance(clan.description, str)
    assert isinstance(clan.is_family_friendly, bool)
    assert isinstance(clan.is_war_log_public, bool)
    assert isinstance(clan.labels, LabelList)
    assert isinstance(clan.location, Location)
    assert isinstance(clan.member_list, ClanMemberList)
    assert isinstance(clan.members, int)
    assert 0 <= clan.members <= 50
    assert isinstance(clan.required_builder_base_trophies, int)
    assert isinstance(clan.required_trophies, int)
    assert isinstance(clan.required_townhall_level, int)
    assert 1 <= clan.required_townhall_level <= 15


@pytest.mark.asyncio
async def test_clan_member(event_loop, pyclasher_client):
    clan_members = ClanMembersRequest(TEST_CLAN_TAG)

    await clan_members.request("test_client")

    assert isinstance(clan_members.to_dict(), dict)
    assert clan_members.clan_tag == TEST_CLAN_TAG
    assert isinstance(clan_members.items, ClanMemberList)
    assert isinstance(clan_members.paging, Paging)

    for member in clan_members:
        assert isinstance(member, ClanMember)
        assert isinstance(member.to_dict(), dict)
        assert isinstance(member.tag, str)
        assert isinstance(member.name, str)
        assert isinstance(member.clan_rank, int)
        assert 1 <= member.clan_rank <= 50
        assert isinstance(member.trophies, int)
        assert isinstance(member.builder_base_league, BuilderBaseLeague)
        assert isinstance(member.builder_base_trophies, int)
        assert isinstance(member.donations, int)
        assert isinstance(member.donations_received, int)
        assert isinstance(member.exp_level, int)
        assert isinstance(member.league, League)
        assert isinstance(member.player_house, (PlayerHouse, Missing))
        assert isinstance(member.previous_clan_rank, int)
        assert 0 <= member.previous_clan_rank <= 50
        assert isinstance(member.role, ClanRole)


@pytest.mark.asyncio
async def test_clan_current_war(event_loop, pyclasher_client):
    current_war = ClanCurrentWarRequest(TEST_CLAN_TAG)

    await current_war.request("test_client")

    assert isinstance(current_war.to_dict(), dict)
    assert current_war.clan_tag == TEST_CLAN_TAG
    assert isinstance(current_war.state, ClanWarState)
    assert isinstance(current_war.clan, WarClan)
    assert isinstance(current_war.opponent, WarClan)

    if (current_war.state == ClanWarState.IN_WAR
            or current_war.state == ClanWarState.PREPARATION):
        assert isinstance(current_war.attacks_per_member, int)
        assert isinstance(current_war.end_time, Time)
        assert isinstance(current_war.team_size, int)
        assert isinstance(current_war.preparation_start_time, Time)
        assert isinstance(current_war.start_time, Time)


@pytest.mark.asyncio
async def test_clan_war_log(event_loop, pyclasher_client):
    war_log = ClanWarLogRequest(TEST_CLAN_TAG)

    await war_log.request("test_client")

    assert isinstance(war_log.to_dict(), dict)
    assert war_log.clan_tag == TEST_CLAN_TAG
    assert isinstance(war_log.items, ClanWarLog)
    assert isinstance(war_log.paging, Paging)

    for war in war_log:
        assert isinstance(war.attacks_per_member, int)
        assert war.attacks_per_member == 1 or war.attacks_per_member == 2
        assert isinstance(war.clan, WarClan)
        assert isinstance(war.opponent, WarClan)
        assert isinstance(war.end_time, Time)
        assert isinstance(war.team_size, int)
        assert 5 <= war.team_size <= 50
        assert isinstance(war.result, ClanWarResult)

    war_log.sort("team_size", descending=False)
    previous = 0

    for war in war_log:
        assert war.team_size >= previous
        previous = war.team_size

    war_log.filter("attacks_per_member", 1)
    for war in war_log:
        assert war.attacks_per_member == 1


@pytest.mark.asyncio
async def test_clan_search(event_loop, pyclasher_client):
    clans = ClanSearchRequest(TEST_CLAN_NAME)

    await clans.request("test_client")

    assert isinstance(clans.to_dict(), dict)
    assert clans.clan_name == TEST_CLAN_NAME
    assert isinstance(clans.items, ClanList)
    assert isinstance(clans.paging, Paging)

    for clan in clans:
        assert isinstance(clan.to_dict(), dict)
        assert isinstance(clan.clan_level, int)
        assert isinstance(clan.name, str)
        assert isinstance(clan.type, ClanType)
        assert isinstance(clan.war_ties, (int, Missing))
        assert isinstance(clan.war_losses, (int, Missing))
        assert isinstance(clan.war_wins, (int, Missing))
        assert isinstance(clan.war_win_streak, int)
        assert isinstance(clan.war_frequency, WarFrequency)
        assert isinstance(clan.badge_urls, BadgeUrls)
        assert isinstance(clan.war_league, WarLeague)
        assert isinstance(clan.capital_league, CapitalLeague)
        assert isinstance(clan.chat_language, (Language, Missing))
        assert isinstance(clan.clan_builder_base_points, int)
        assert isinstance(clan.clan_capital, (ClanCapital, Missing))
        assert isinstance(clan.clan_capital_points, int)
        assert isinstance(clan.clan_points, int)
        assert isinstance(clan.description, (str, Missing))
        assert isinstance(clan.is_family_friendly, bool)
        assert isinstance(clan.is_war_log_public, bool)
        assert isinstance(clan.labels, LabelList)
        assert isinstance(clan.location, (Location, Missing))
        assert isinstance(clan.member_list, Missing)
        assert isinstance(clan.members, int)
        assert 0 <= clan.members <= 50
        assert isinstance(clan.required_builder_base_trophies, int)
        assert isinstance(clan.required_trophies, int)
        assert isinstance(clan.required_townhall_level, int)
        assert 1 <= clan.required_townhall_level <= 15


@pytest.mark.asyncio
async def test_clan_capital_raid_season(event_loop, pyclasher_client):
    raid_seasons = ClanCapitalRaidSeasonsRequest(TEST_CLAN_TAG)

    await raid_seasons.request("test_client")

    assert isinstance(raid_seasons.to_dict(), dict)
    assert raid_seasons.clan_tag == TEST_CLAN_TAG
    assert isinstance(raid_seasons.items, ClanCapitalRaidSeasons)
    assert isinstance(raid_seasons.paging, Paging)

    for rs in raid_seasons:
        assert isinstance(rs.to_dict(), dict)
        assert isinstance(rs.state, str)
        assert isinstance(rs.members,
                          (ClanCapitalRaidSeasonMemberList, Missing))
        assert isinstance(rs.end_time, Time)
        assert isinstance(rs.start_time, Time)
        assert isinstance(rs.attack_log, ClanCapitalRaidSeasonAttackLogList)
        assert isinstance(rs.capital_total_loot, int)
        assert isinstance(rs.defense_log, ClanCapitalRaidSeasonDefenseLogList)
        assert isinstance(rs.defensive_reward, int)
        assert isinstance(rs.enemy_districts_destroyed, int)
        assert isinstance(rs.raids_completed, int)
        assert isinstance(rs.total_attacks, int)


@pytest.mark.asyncio
async def test_clan_currentwar_leaguegroup(event_loop, pyclasher_client):
    try:
        league_group = ClanCurrentwarLeaguegroupRequest(TEST_CLAN_TAG)

        await league_group.request("test_client")
    except NotFound:
        pass
    else:
        assert isinstance(league_group.to_dict(), dict)
        assert league_group.clan_tag == TEST_CLAN_TAG

        assert isinstance(league_group.state, ClanWarLeagueGroupState)
        assert isinstance(league_group.clans, ClanWarLeagueClanList)
        assert isinstance(league_group.rounds, ClanWarLeagueRoundList)
        assert isinstance(league_group.season, str)


@pytest.mark.asyncio
async def test_clan_warleagues_wars(event_loop, pyclasher_client):
    try:
        league_group = ClanCurrentwarLeaguegroupRequest(TEST_CLAN_TAG)

        await league_group.request("test_client")
    except NotFound:
        pass
    else:
        for league_round in league_group.rounds:
            for war in league_round.war_tags:
                if war == "#0":
                    continue

                group = ClanWarleaguesWarsRequest(war)

                await group.request("test_client")

                assert isinstance(group.to_dict(), dict)
                assert group.war_tag == war

                assert isinstance(group.state, ClanWarState)
                assert isinstance(group.clan, WarClan)
                assert isinstance(group.opponent, WarClan)

                assert group.attacks_per_member == MISSING
                assert isinstance(group.end_time, Time)
                assert isinstance(group.team_size, int)
                assert isinstance(group.preparation_start_time, Time)
                assert isinstance(group.start_time, Time)
