"""
requests that can be used
"""

from .builder_base_league import BuilderBaseLeagueRequest
from .builder_base_leagues import BuilderBaseLeaguesRequest
from .capital_league import CapitalLeagueRequest
from .capital_league_seasons import CapitalLeaguesRequest
from .capital_rankings import CapitalRankingsRequest
from .clan import ClanRequest
from .clan_builder_base_rankings import ClanBuilderBaseRankingsRequest
from .clan_capital_raid_seasons import ClanCapitalRaidSeasonsRequest
from .clan_current_war import ClanCurrentWarRequest
from .clan_currentwar_leaguegroup import ClanCurrentwarLeaguegroupRequest
from .clan_labels import ClanLabelsRequest
from .clan_members import ClanMembersRequest
from .clan_rankings import ClanRankingsRequest
from .clan_search import ClanSearchRequest
from .clan_war_log import ClanWarLogRequest
from .clan_warleagues_wars import ClanWarleaguesWarsRequest
from .gold_pass import GoldPassRequest
from .league import LeagueRequest
from .league_season import LeagueSeasonRequest
from .league_seasons import LeagueSeasonsRequest
from .leagues import LeaguesRequest
from .location import LocationRequest
from .locations import LocationsRequest
from .player import PlayerRequest
from .player_builder_base_rankings import PlayerBuilderBaseRankingsRequest
from .player_labels import PlayerLabelsRequest
from .player_rankings import PlayerRankingsRequest
from .war_league import WarLeagueRequest
from .war_leagues import WarLeaguesRequest


__all__ = (
    'WarLeagueRequest',
    'WarLeaguesRequest',
    'CapitalLeagueRequest',
    'CapitalLeaguesRequest',
    'CapitalRankingsRequest',
    'BuilderBaseLeagueRequest',
    'BuilderBaseLeaguesRequest',
    'PlayerLabelsRequest',
    'PlayerRankingsRequest',
    'LeaguesRequest',
    'LocationRequest',
    'PlayerRequest',
    'LocationsRequest',
    'LeagueSeasonsRequest',
    'PlayerBuilderBaseRankingsRequest',
    'LeagueRequest',
    'ClanRequest',
    'GoldPassRequest',
    'LeagueSeasonRequest',
    'ClanSearchRequest',
    'ClanRankingsRequest',
    'ClanLabelsRequest',
    'ClanMembersRequest',
    'ClanWarLogRequest',
    'ClanWarleaguesWarsRequest',
    'ClanCurrentwarLeaguegroupRequest',
    'ClanCurrentWarRequest',
    'ClanCapitalRaidSeasonsRequest',
    'ClanBuilderBaseRankingsRequest',
)
