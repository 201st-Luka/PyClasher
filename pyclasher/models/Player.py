from .Labels import LabelList
from .PlayerHouse import PlayerHouse
from .BaseModels import BaseModel, IterBaseModel, BaseClan
from .Leagues import League, BuilderBaseLeague
from .Enums import ClanRole, WarPreference, Village


class PlayerClan(BaseClan):
    @property
    def clan_level(self) -> int:
        return self._get_data('clanLevel')


class LegendLeagueTournamentSeasonResult(BaseModel):
    def __init__(self, data: dict):
        super().__init__(data)
        self._main_attribute = self.id
        return

    @property
    def trophies(self) -> int:
        return self._get_data('trophies')

    @property
    def id(self) -> str:
        return self._get_data('id')

    @property
    def rank(self) -> int:
        return self._get_data('rank')


class PlayerLegendStatistics(BaseModel):
    @property
    def best_season(self) -> LegendLeagueTournamentSeasonResult:
        return LegendLeagueTournamentSeasonResult(self._get_data('bestSeason'))

    @property
    def current_season(self) -> LegendLeagueTournamentSeasonResult:
        return LegendLeagueTournamentSeasonResult(self._get_data('currentSeason'))

    @property
    def previous_season(self) -> LegendLeagueTournamentSeasonResult:
        return LegendLeagueTournamentSeasonResult(self._get_data('previousSeason'))

    @property
    def previous_builder_base_season(self) -> LegendLeagueTournamentSeasonResult:
        return LegendLeagueTournamentSeasonResult(self._get_data('previousBuilderBaseSeason'))

    @property
    def previous_versus_season(self) -> LegendLeagueTournamentSeasonResult:
        return LegendLeagueTournamentSeasonResult(self._get_data('previousVersusSeason'))

    @property
    def best_builder_base_season(self) -> LegendLeagueTournamentSeasonResult:
        return LegendLeagueTournamentSeasonResult(self._get_data('bestBuilderBaseSeason'))

    @property
    def best_versus_season(self) -> LegendLeagueTournamentSeasonResult:
        return LegendLeagueTournamentSeasonResult(self._get_data('bestVersusSeason'))

    @property
    def legend_trophies(self) -> int:
        return self._get_data('legendTrophies')


class PlayerItemLevel(BaseModel):
    @property
    def level(self) -> int:
        return self._get_data('level')

    @property
    def name(self) -> str:
        return self._get_data('name')

    @property
    def max_level(self) -> int:
        return self._get_data('maxLevel')

    @property
    def village(self) -> Village:
        return Village(self._get_data('id'))


class PlayerItemLevelList(IterBaseModel):
    _iter_rtype = PlayerItemLevel

    def __getitem__(self, item: int | str) -> _iter_rtype:
        return super().__getitem__(item)

    def __next__(self) -> _iter_rtype:
        return super().__next__()


class PlayerAchievementProgress(BaseModel):
    @property
    def stars(self) -> int:
        return self._get_data('stars')

    @property
    def value(self) -> int:
        return self._get_data('value')

    @property
    def name(self) -> str:
        return self._get_data('name')

    @property
    def target(self) -> int:
        return self._get_data('target')

    @property
    def info(self) -> str:
        return self._get_data('info')

    @property
    def completion_info(self) -> str:
        return self._get_data('completionInfo')

    @property
    def village(self) -> Village:
        return Village(self._get_data('village'))


class PlayerAchievementProgressList(IterBaseModel):
    _iter_rtype = PlayerAchievementProgress

    def __getitem__(self, item: int | str) -> _iter_rtype:
        return super().__getitem__(item)

    def __next__(self) -> _iter_rtype:
        return super().__next__()


class Player(BaseModel):
    def __init__(self, data: dict):
        super().__init__(data)
        self._main_attribute = self.tag
        return

    @property
    def league(self) -> League:
        return League(self._get_data('league'))

    @property
    def builder_base_league(self) -> BuilderBaseLeague:
        return BuilderBaseLeague(self._get_data('builderBaseLeague'))

    @property
    def clan(self) -> PlayerClan:
        return PlayerClan(self._get_data('clan'))

    @property
    def role(self) -> ClanRole:
        return ClanRole(self._get_data('role'))

    @property
    def war_preference(self) -> WarPreference:
        return WarPreference(self._get_data('warPreference'))

    @property
    def attack_wins(self) -> int:
        return self._get_data('attackWins')

    @property
    def defense_wins(self) -> int:
        return self._get_data('defenseWins')

    @property
    def versus_trophies(self) -> int:
        return self._get_data('versusTrophies')

    @property
    def best_versus_trophies(self) -> int:
        return self._get_data('bestVersusTrophies')

    @property
    def town_hall_level(self) -> int:
        return self._get_data('townHallLevel')

    @property
    def town_hall_weapon_level(self) -> int:
        return self._get_data('townHallWeaponLevel')

    @property
    def versus_battle_wins(self) -> int:
        return self._get_data('versusBattleWins')

    @property
    def legend_statistics(self) -> PlayerLegendStatistics:
        return PlayerLegendStatistics(self._get_data('legendStatistics'))

    @property
    def troops(self) -> PlayerItemLevelList:
        return PlayerItemLevelList(self._get_data('troops'))

    @property
    def heroes(self) -> PlayerItemLevelList:
        return PlayerItemLevelList(self._get_data('heroes'))

    @property
    def spells(self) -> PlayerItemLevelList:
        return PlayerItemLevelList(self._get_data('spells'))

    @property
    def labels(self) -> LabelList:
        return LabelList(self._get_data('labels'))

    @property
    def tag(self) -> str:
        return self._get_data('tag')

    @property
    def name(self) -> str:
        return self._get_data('name')

    @property
    def exp_level(self) -> int:
        return self._get_data('expLevel')

    @property
    def trophies(self) -> int:
        return self._get_data('trophies')

    @property
    def best_trophies(self) -> int:
        return self._get_data('bestTrophies')

    @property
    def donations(self) -> int:
        return self._get_data('donations')

    @property
    def donations_received(self) -> int:
        return self._get_data('donationsReceived')

    @property
    def builder_hall_level(self) -> int:
        return self._get_data('builderHallLevel')

    @property
    def builder_base_trophies(self) -> int:
        return self._get_data('builderBaseTrophies')

    @property
    def best_builder_base_trophies(self) -> int:
        return self._get_data('bestBuilderBaseTrophies')

    @property
    def war_stars(self) -> int:
        return self._get_data('warStars')

    @property
    def achievements(self) -> PlayerAchievementProgressList:
        return PlayerAchievementProgressList(self._get_data('achievements'))

    @property
    def clan_capital_contributions(self) -> str:
        return self._get_data('clanCapitalContributions')

    @property
    def player_house(self) -> PlayerHouse:
        return PlayerHouse(self._get_data('playerHouse'))
