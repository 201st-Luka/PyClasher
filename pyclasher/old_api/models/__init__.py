"""
ClashOfClans API models
"""
# abc
from .abc import BaseModel, IterBaseModel
# base models, miscellaneous models and enums
from .base_models import (
    ImageUrl, IconUrl, IconUrls, After, Before,
    Cursor, Paging, BadgeUrl, BadgeUrls, Time,
    BaseClanMember, BaseClan,
    BaseLeague
)

# clan models
from .clan import ClanDistrictData, ClanDistrictDataList, ClanCapital, Clan
from .clan_builder_base_ranking_list import (
    ClanBuilderBaseRanking, ClanBuilderBaseRankingList
)
from .clan_capital_raid_seasons import (
    ClanCapitalRaidSeasonClanInfo, ClanCapitalRaidSeasonAttacker,
    ClanCapitalRaidSeasonAttack, ClanCapitalRaidSeasonAttackList,
    ClanCapitalRaidSeasonDistrict, ClanCapitalRaidSeasonDistrictList,
    ClanCapitalRaidSeasonDefenseLogEntry,
    ClanCapitalRaidSeasonAttackLogEntry, ClanCapitalRaidSeasonDefenseLogList,
    ClanCapitalRaidSeasonAttackLogList, ClanCapitalRaidSeasonMember,
    ClanCapitalRaidSeasonMemberList, ClanCapitalRaidSeason,
    ClanCapitalRaidSeasons
)
from .clan_capital_ranking_list import (
    ClanCapitalRanking, ClanCapitalRankingList
)
from .clan_list import ClanList
from .clan_member import ClanMember
from .clan_member_list import ClanMemberList
from .clan_ranking_list import ClanRanking, ClanRankingList
from .clan_war import ClanWar
from .clan_war_league_group import (
    ClanWarLeagueRound, ClanWarLeagueRoundList, ClanWarLeagueClanMember,
    ClanWarLeagueClanMemberList, ClanWarLeagueClan, ClanWarLeagueClanList,
    ClanWarLeagueGroup
)
from .clan_war_log import ClanWarLogEntry, ClanWarLog
from .enums import (
    ClanType, WarFrequency, Locations, Leagues, CapitalLeagues,
    BuilderBaseLeagues, WarLeagues, Labels, Languages, ClanWarState,
    ClanWarLeagueGroupState, ClanWarResult, WarPreference,
    PlayerHouseElementType, Village, TokenStatus, ClanRole
)
# gold pass season
from .gold_pass_season import GoldPassSeason
# labels
from .labels import Label, LabelList
from .language import Language
# league models
from .leagues import (
    League, BuilderBaseLeague, CapitalLeague, WarLeague, LeagueList,
    BuilderBaseLeagueList, CapitalLeagueList, WarLeagueList, LeagueSeason,
    LeagueSeasonList
)
# locations
from .location import Location, LocationList
# login
from .login import *
# misc
from .misc import *
# player models
from .player import (
    PlayerClan, LegendLeagueTournamentSeasonResult, PlayerLegendStatistics,
    PlayerItemLevel, PlayerItemLevelList, PlayerAchievementProgress,
    PlayerAchievementProgressList, Player
)
from .player_builder_base_ranking_list import (
    PlayerBuilderBaseRanking, PlayerBuilderBaseRankingList
)
from .player_house import (
    PlayerHouseElement, PlayerHouseElementList, PlayerHouse
)
from .player_ranking_clan import PlayerRankingClan
from .player_ranking_list import PlayerRanking, PlayerRankingList
# miscellaneous
from .season import Season
from .war_clan import (
    ClanWarAttack, ClanWarAttackList, ClanWarMember, ClanWarMemberList, WarClan
)

__all__ = (
    "ClanCapital",
    "Clan",
    "ClanBuilderBaseRanking",
    "ClanCapitalRaidSeason",
    "ClanCapitalRaidSeasons",
    "ClanCapitalRanking",
    "ClanMember",
    "ClanRanking",
    "ClanWar",
    "ClanWarLeagueGroup",
    "ClanWarLog",
    "Label",
    "Language",
    "League",
    "BuilderBaseLeague",
    "CapitalLeague",
    "WarLeague",
    "Location",
    "LoginModel",
    "Player",
    "PlayerBuilderBaseRanking",
    "WarClan"
)
