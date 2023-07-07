"""
ClashOfClans API models
"""

# base models, miscellaneous models and enums
from .BaseModels import BaseModel, IterBaseModel, ImageUrl, IconUrl, IconUrls, After, Before, \
    Cursor, Paging, BadgeUrl, BadgeUrls, Time, BaseClanMember, BaseClan, BaseLeague

from .misc import *

from .Enums import ApiCodes, ClanType, WarFrequency, Locations, Leagues, CapitalLeagues, \
    BuilderBaseLeagues, WarLeagues, Labels, Languages, ClanWarState, ClanWarLeagueGroupState, \
    ClanWarResult, WarPreference, PlayerHouseElementType, Village, TokenStatus

from .Season import Season


# clan models
from .Clan import ClanDistrictData, ClanDistrictDataList, ClanCapital, Clan
from .ClanCapitalRaidSeasons import ClanCapitalRaidSeasonClanInfo, ClanCapitalRaidSeasonAttacker, \
    ClanCapitalRaidSeasonAttack, ClanCapitalRaidSeasonAttackList, ClanCapitalRaidSeasonDistrict, \
    ClanCapitalRaidSeasonDistrictList, ClanCapitalRaidSeasonDefenseLogEntry, ClanCapitalRaidSeasonAttackLogEntry, \
    ClanCapitalRaidSeasonDefenseLogList, ClanCapitalRaidSeasonAttackLogList, ClanCapitalRaidSeasonMember, \
    ClanCapitalRaidSeasonMemberList, ClanCapitalRaidSeason, ClanCapitalRaidSeasons
from .ClanList import SearchClan, ClanList
from .ClanMember import ClanMember
from .ClanMemberList import ClanMemberList
from .ClanWar import ClanWar
from .ClanWarLeagueGroup import ClanWarLeagueRound, ClanWarLeagueRoundList, ClanWarLeagueClanMember, \
    ClanWarLeagueClanMemberList, ClanWarLeagueClan, ClanWarLeagueClanList, ClanWarLeagueGroup
from .ClanWarLog import ClanWarLogEntry, ClanWarLog
from .WarClan import ClanWarAttack, ClanWarAttackList, ClanWarMember, ClanWarMemberList, WarClan


# player models
from .Player import PlayerClan, LegendLeagueTournamentSeasonResult, PlayerLegendStatistics, \
    PlayerItemLevel, PlayerItemLevelList, PlayerAchievementProgress, PlayerAchievementProgressList, Player
from .PlayerHouse import PlayerHouseElement, PlayerHouseElementList, PlayerHouse


# league models
from .Leagues import League, BuilderBaseLeague, CapitalLeague, WarLeague, LeagueList, \
    BuilderBaseLeagueList, CapitalLeagueList, WarLeagueList, LeagueSeason, LeagueSeasonList


# locations
from .Location import Location, LocationList
from .ClanRankingList import ClanRanking, ClanRankingList
from .PlayerRankingClan import PlayerRankingClan
from .PlayerRankingList import PlayerRanking, PlayerRankingList
from .PlayerBuilderBaseRankingList import PlayerBuilderBaseRanking, PlayerBuilderBaseRankingList
from .ClanBuilderBaseRankingList import ClanBuilderBaseRanking, ClanBuilderBaseRankingList
from .ClanCapitalRankingList import ClanCapitalRanking, ClanCapitalRankingList


# gold pass season
from .GoldPassSeason import GoldPassSeason


# labels
from .Labels import Label, LabelList
