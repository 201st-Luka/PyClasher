from .BaseModels import BaseModel, IterBaseModel, BaseClan
from .Enums import ClanRole, WarPreference, Village
from .Labels import LabelList
from .Leagues import League, BuilderBaseLeague
from .PlayerHouse import PlayerHouse


class PlayerClan(BaseClan):
    """
    player clan model

    clan model found in the player response
    """

    @property
    def clan_level(self) -> int:
        """
        clan level

        :return:    the level of the clan
        :rtype:     int
        """
        ...


class LegendLeagueTournamentSeasonResult(BaseModel):
    """
    legend league tournament season result model
    """

    @property
    def trophies(self) -> int:
        """
        trophy score of the season

        :return:    the trophy score of the season of the player
        :rtype:     int
        """
        ...

    @property
    def id(self) -> str:
        """
        season ID

        :return:    the ID of the season
        :rtype:     str
        """
        ...

    @property
    def rank(self) -> int:
        """
        rank of the season

        :return:    the rank of the season
        :rtype:     int
        """
        ...


class PlayerLegendStatistics(BaseModel):
    """
    player legend statistics model
    """

    @property
    def best_season(self) -> LegendLeagueTournamentSeasonResult:
        ...

    @property
    def current_season(self) -> LegendLeagueTournamentSeasonResult:
        ...

    @property
    def previous_season(self) -> LegendLeagueTournamentSeasonResult:
        ...

    @property
    def previous_builder_base_season(self) -> LegendLeagueTournamentSeasonResult:
        ...

    @property
    def previous_versus_season(self) -> LegendLeagueTournamentSeasonResult:
        ...

    @property
    def best_builder_base_season(self) -> LegendLeagueTournamentSeasonResult:
        ...

    @property
    def best_versus_season(self) -> LegendLeagueTournamentSeasonResult:
        ...

    @property
    def legend_trophies(self) -> int:
        ...


class PlayerItemLevel(BaseModel):
    @property
    def level(self) -> int:
        ...

    @property
    def name(self) -> str:
        ...

    @property
    def max_level(self) -> int:
        ...

    @property
    def village(self) -> Village:
        ...


class PlayerItemLevelList(IterBaseModel):
    _iter_rtype = PlayerItemLevel

    def __getitem__(self, item: int | str) -> _iter_rtype:
        ...

    def __next__(self) -> _iter_rtype:
        ...


class PlayerAchievementProgress(BaseModel):
    @property
    def stars(self) -> int:
        ...

    @property
    def value(self) -> int:
        ...

    @property
    def name(self) -> str:
        ...

    @property
    def target(self) -> int:
        ...

    @property
    def info(self) -> str:
        ...

    @property
    def completion_info(self) -> str:
        ...

    @property
    def village(self) -> Village:
        ...


class PlayerAchievementProgressList(IterBaseModel):
    _iter_rtype = PlayerAchievementProgress

    def __getitem__(self, item: int | str) -> _iter_rtype:
        ...

    def __next__(self) -> _iter_rtype:
        ...


class Player(BaseModel):
    @property
    def league(self) -> League:
        ...

    @property
    def builder_base_league(self) -> BuilderBaseLeague:
        ...

    @property
    def clan(self) -> PlayerClan:
        ...

    @property
    def role(self) -> ClanRole:
        ...

    @property
    def war_preference(self) -> WarPreference:
        ...

    @property
    def attack_wins(self) -> int:
        ...

    @property
    def defense_wins(self) -> int:
        ...

    @property
    def versus_trophies(self) -> int:
        ...

    @property
    def best_versus_trophies(self) -> int:
        ...

    @property
    def town_hall_level(self) -> int:
        ...

    @property
    def town_hall_weapon_level(self) -> int:
        ...

    @property
    def versus_battle_wins(self) -> int:
        ...

    @property
    def legend_statistics(self) -> PlayerLegendStatistics:
        ...

    @property
    def troops(self) -> PlayerItemLevelList:
        ...

    @property
    def heroes(self) -> PlayerItemLevelList:
        ...

    @property
    def spells(self) -> PlayerItemLevelList:
        ...

    @property
    def labels(self) -> LabelList:
        ...

    @property
    def tag(self) -> str:
        ...

    @property
    def name(self) -> str:
        ...

    @property
    def exp_level(self) -> int:
        ...

    @property
    def trophies(self) -> int:
        ...

    @property
    def best_trophies(self) -> int:
        ...

    @property
    def donations(self) -> int:
        ...

    @property
    def donations_received(self) -> int:
        ...

    @property
    def builder_hall_level(self) -> int:
        ...

    @property
    def builder_base_trophies(self) -> int:
        ...

    @property
    def best_builder_base_trophies(self) -> int:
        ...

    @property
    def war_stars(self) -> int:
        ...

    @property
    def achievements(self) -> PlayerAchievementProgressList:
        ...

    @property
    def clan_capital_contributions(self) -> str:
        ...

    @property
    def player_house(self) -> PlayerHouse:
        ...
