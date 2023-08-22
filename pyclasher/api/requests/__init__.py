"""
requests that can be used
"""

from .builder_base_league import BuilderBaseLeagueRequest
from .builder_base_leagues import BuilderBaseLeaguesRequest
from .capital_league import CapitalLeagueRequest
from .capital_league_seasons import CapitalLeaguesRequest
# clan
from .clan import ClanRequest
from .clan_builder_base_rankings import ClanBuilderBaseRankingsRequest
from .clan_capital_raid_seasons import ClanCapitalRaidSeasonsRequest
from .clan_current_war import ClanCurrentWarRequest
from .clan_labels import ClanLabelsRequest
from .clan_members import ClanMembersRequest
from .clan_rankings import ClanRankingsRequest
from .clan_search import ClanSearchRequest
from .clan_war_log import ClanWarLogRequest
# goldpass
from .gold_pass import GoldPassRequest
from .league import LeagueRequest
# leagues
from .league_season import LeagueSeasonRequest
from .leagues import LeaguesRequest
from .location import LocationRequest
# locations
from .locations import LocationsRequest
# player
from .player import PlayerRequest
from .player_builder_base_rankings import PlayerBuilderBaseRankingsRequest
# labels
from .player_labels import PlayerLabelsRequest
from .player_rankings import PlayerRankingsRequest
from .abc import RequestModel, IterRequestModel, request_id
from .war_league import WarLeagueRequest
from .war_leagues import WarLeaguesRequest
