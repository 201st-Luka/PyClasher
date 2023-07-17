from pyclasher import RequestNotDone, ClanWarLogRequest, ClanSearchRequest, ClanCurrentWarRequest, ClanRequest, \
    ClanMembersRequest, ClanCapitalRaidSeasonsRequest
from pyclasher.models import ClanWarLog, Paging, ClanMemberList, Location, WarLeague, CapitalLeague, WarFrequency, \
    ClanType, BadgeUrls, Language, ClanCapital, LabelList, WarClan, ClanWarState, Time, ClanList, ClanCapitalRaidSeasons
from ...constants import my_test_clan_tag, client, my_test_clan_name


def test_clans_currentwar_leaguegroup():
    """
    request for this test is not implemented yet
    """
    client.reset_client(reset_tokens=False, reset_loop=False)

    ...


def test_clanwarleagues_wars():
    """
    request for this test is not implemented yet
    """
    ...


def test_clans_warlog() -> None:
    with client:
        clan_war_log = ClanWarLogRequest(my_test_clan_tag)

        try:
            clan_war_log_items = clan_war_log.items
        except Exception as exception:
            assert isinstance(exception, RequestNotDone)
        else:
            assert False

        clan_war_log.request()

        assert isinstance(clan_war_log.to_dict(), dict)
        assert 0 <= len(clan_war_log)
        assert isinstance(clan_war_log.items, ClanWarLog)
        assert isinstance(clan_war_log.paging, Paging)

        return


def test_clans_search() -> None:
    with client:
        clan_search = ClanSearchRequest(my_test_clan_name, limit=10)

        try:
            clan_search_items = clan_search.items
        except Exception as exception:
            assert isinstance(exception, RequestNotDone)
        else:
            assert False

        clan_search.request()

        assert isinstance(clan_search.to_dict(), dict)
        assert 0 <= len(clan_search) <= 10
        assert isinstance(clan_search.items, ClanList)
        assert isinstance(clan_search.paging, Paging)

        return


def test_clans_currentwar() -> None:
    with client:
        clan_current_war = ClanCurrentWarRequest(my_test_clan_tag)

        try:
            clan_current_war_state = clan_current_war.state
        except Exception as exception:
            assert isinstance(exception, RequestNotDone)
        else:
            assert False

        clan_current_war.request()

        assert isinstance(clan_current_war.to_dict(), dict)
        assert isinstance(clan_current_war.clan, WarClan)
        assert isinstance(clan_current_war.state, ClanWarState)
        assert isinstance(clan_current_war.team_size, int)
        assert isinstance(clan_current_war.attacks_per_member, int)
        assert isinstance(clan_current_war.opponent, WarClan)
        assert isinstance(clan_current_war.end_time, Time)
        assert isinstance(clan_current_war.start_time, Time)
        assert isinstance(clan_current_war.preparation_start_time, Time)

        return


def test_clans_clan() -> None:
    with client:
        clan = ClanRequest(my_test_clan_tag)

        try:
            clan_tag = clan.tag
        except Exception as exception:
            assert isinstance(exception, RequestNotDone)
        else:
            assert False

        clan.request()

        assert isinstance(clan.to_dict(), dict)
        assert isinstance(clan.tag, str)
        assert isinstance(clan.required_trophies, int)
        assert isinstance(clan.name, str)
        assert isinstance(clan.members, int)
        assert isinstance(clan.member_list, ClanMemberList)
        assert isinstance(clan.location, Location)
        assert isinstance(clan.war_league, WarLeague)
        assert isinstance(clan.capital_league, CapitalLeague)
        assert isinstance(clan.war_frequency, WarFrequency)
        assert isinstance(clan.type, ClanType)
        assert isinstance(clan.description, str)
        assert isinstance(clan.war_wins, int)
        assert isinstance(clan.clan_level, int)
        assert isinstance(clan.badge_urls, BadgeUrls)
        assert isinstance(clan.chat_language, Language)
        assert isinstance(clan.clan_builder_base_points, int)
        assert isinstance(clan.clan_capital, ClanCapital)
        assert isinstance(clan.clan_capital_points, int)
        assert isinstance(clan.clan_points, int)
        assert isinstance(clan.is_family_friendly, bool)
        assert isinstance(clan.is_war_log_public, bool)
        assert isinstance(clan.labels, LabelList)
        assert isinstance(clan.required_builder_base_trophies, int)
        assert isinstance(clan.required_townhall_level, int)
        assert isinstance(clan.war_losses, int)
        assert isinstance(clan.war_ties, int)
        assert isinstance(clan.war_win_streak, int)
        assert clan.clan_tag == clan.tag

        return


def test_clans_members() -> None:
    with client:
        clan_members = ClanMembersRequest(my_test_clan_tag)

        try:
            clan_members_items = clan_members.items
        except Exception as exception:
            assert isinstance(exception, RequestNotDone)
        else:
            assert False

        clan_members.request()

        assert isinstance(clan_members.to_dict(), dict)
        assert 0 <= len(clan_members) <= 50
        assert isinstance(clan_members.items, ClanMemberList)
        assert isinstance(clan_members.paging, Paging)

        return


def test_clans_capitalraidseasons():
    with client:
        clan_capital_raid_seasons = ClanCapitalRaidSeasonsRequest(my_test_clan_tag)

        try:
            clan_capital_raid_seasons_items = clan_capital_raid_seasons.items
        except Exception as exception:
            assert isinstance(exception, RequestNotDone)
        else:
            assert False

        clan_capital_raid_seasons.request()

        assert isinstance(clan_capital_raid_seasons.to_dict(), dict)
        assert 0 <= len(clan_capital_raid_seasons)
        assert isinstance(clan_capital_raid_seasons.items, ClanCapitalRaidSeasons)
        assert isinstance(clan_capital_raid_seasons.paging, Paging)

        return
