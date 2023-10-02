from .abc import BaseModel, IterBaseModel
from .base_models import BaseClan
from .enums import ClanRole, WarPreference, Village
from .labels import LabelList
from .leagues import League, BuilderBaseLeague
from .player_house import PlayerHouse


__all__ = (
    'LegendLeagueTournamentSeasonResult',
    'Player',
    'PlayerAchievementProgress',
    'PlayerAchievementProgressList',
    'PlayerClan',
    'PlayerItemLevel',
    'PlayerItemLevelList',
    'PlayerLegendStatistics',
)


class PlayerClan(BaseClan):
    @property
    def clan_level(self):
        return self._get_data('clanLevel')


class LegendLeagueTournamentSeasonResult(BaseModel):
    def __init__(self, data):
        super().__init__(data)
        return

    @property
    def trophies(self):
        return self._get_data('trophies')

    @property
    def id(self):
        return self._get_data('id')

    @property
    def rank(self):
        return self._get_data('rank')


class PlayerLegendStatistics(BaseModel):
    @property
    def best_season(self):
        return LegendLeagueTournamentSeasonResult(self._get_data('bestSeason'))

    @property
    def current_season(self):
        return LegendLeagueTournamentSeasonResult(
            self._get_data('currentSeason')
        )

    @property
    def previous_season(self):
        return LegendLeagueTournamentSeasonResult(
            self._get_data('previousSeason')
        )

    @property
    def previous_builder_base_season(self):
        return LegendLeagueTournamentSeasonResult(
            self._get_data('previousBuilderBaseSeason')
        )

    @property
    def previous_versus_season(self):
        return LegendLeagueTournamentSeasonResult(
            self._get_data('previousVersusSeason')
        )

    @property
    def best_builder_base_season(self):
        return LegendLeagueTournamentSeasonResult(
            self._get_data('bestBuilderBaseSeason')
        )

    @property
    def best_versus_season(self):
        return LegendLeagueTournamentSeasonResult(
            self._get_data('bestVersusSeason')
        )

    @property
    def legend_trophies(self):
        return self._get_data('legendTrophies')


class PlayerItemLevel(BaseModel):
    @property
    def level(self):
        return self._get_data('level')

    @property
    def name(self):
        return self._get_data('name')

    @property
    def max_level(self):
        return self._get_data('maxLevel')

    @property
    def village(self):
        return Village(self._get_data('id'))


class PlayerItemLevelList(IterBaseModel):
    _iter_rtype = PlayerItemLevel


class PlayerAchievementProgress(BaseModel):
    @property
    def stars(self):
        return self._get_data('stars')

    @property
    def value(self):
        return self._get_data('value')

    @property
    def name(self):
        return self._get_data('name')

    @property
    def target(self):
        return self._get_data('target')

    @property
    def info(self):
        return self._get_data('info')

    @property
    def completion_info(self):
        return self._get_data('completionInfo')

    @property
    def village(self):
        return Village(self._get_data('village'))


class PlayerAchievementProgressList(IterBaseModel):
    _iter_rtype = PlayerAchievementProgress


class Player(BaseModel):
    def __init__(self, data):
        super().__init__(data)
        return

    @property
    def league(self):
        return League(self._get_data('league'))

    @property
    def builder_base_league(self):
        return BuilderBaseLeague(self._get_data('builderBaseLeague'))

    @property
    def clan(self):
        return PlayerClan(self._get_data('clan'))

    @property
    def role(self):
        return ClanRole(self._get_data('role'))

    @property
    def war_preference(self):
        return WarPreference(self._get_data('warPreference'))

    @property
    def attack_wins(self):
        return self._get_data('attackWins')

    @property
    def defense_wins(self):
        return self._get_data('defenseWins')

    @property
    def town_hall_level(self):
        return self._get_data('townHallLevel')

    @property
    def town_hall_weapon_level(self):
        return self._get_data('townHallWeaponLevel')

    @property
    def versus_battle_wins(self):
        return self._get_data('versusBattleWins')

    @property
    def legend_statistics(self):
        return PlayerLegendStatistics(self._get_data('legendStatistics'))

    @property
    def troops(self):
        return PlayerItemLevelList(self._get_data('troops'))

    @property
    def heroes(self):
        return PlayerItemLevelList(self._get_data('heroes'))

    @property
    def average_hero_level(self):
        return (sum((hero
                     for hero in self.heroes
                     if hero.village == Village.HOME_VILLAGE)) /
                sum((hero.village == Village.HOME_VILLAGE
                     for hero in self.heroes)))

    @property
    def spells(self):
        return PlayerItemLevelList(self._get_data('spells'))

    @property
    def labels(self):
        return LabelList(self._get_data('labels'))

    @property
    def tag(self):
        return self._get_data('tag')

    @property
    def name(self):
        return self._get_data('name')

    @property
    def exp_level(self):
        return self._get_data('expLevel')

    @property
    def trophies(self):
        return self._get_data('trophies')

    @property
    def best_trophies(self):
        return self._get_data('bestTrophies')

    @property
    def donations(self):
        return self._get_data('donations')

    @property
    def donations_received(self):
        return self._get_data('donationsReceived')

    @property
    def builder_hall_level(self):
        return self._get_data('builderHallLevel')

    @property
    def builder_base_trophies(self):
        return self._get_data('builderBaseTrophies')

    @property
    def best_builder_base_trophies(self):
        return self._get_data('bestBuilderBaseTrophies')

    @property
    def war_stars(self):
        return self._get_data('warStars')

    @property
    def achievements(self):
        return PlayerAchievementProgressList(self._get_data('achievements'))

    @property
    def clan_capital_contributions(self):
        return self._get_data('clanCapitalContributions')

    @property
    def player_house(self):
        return PlayerHouse(self._get_data('playerHouse'))
