"""
``Player`` class
"""

from .BuilderBaseLeague import BuilderBaseLeague
from .Label import Label
from .League import League
from .PlayerAchievementProgress import PlayerAchievementProgress
from .PlayerClan import PlayerClan
from .PlayerHouse import PlayerHouse
from .PlayerItemLevel import PlayerItemLevel
from .PlayerLegendStatistics import PlayerLegendStatistics
from ...model_abc import Model, ModelWrapper, ArrayIterator


@ModelWrapper(main_attributes=['tag'], exclude_annotations=None)
class Player(Model):
    achievements: ArrayIterator[PlayerAchievementProgress]
    attack_wins: int
    best_builder_base_trophies: int
    best_trophies: int
    builder_base_league: BuilderBaseLeague
    builder_base_trophies: int
    builder_hall_level: int
    clan: PlayerClan
    clan_capital_contributions: int
    defense_wins: int
    donations: int
    donations_received: int
    exp_level: int
    hero_equipment: ArrayIterator[PlayerItemLevel]
    heroes: ArrayIterator[PlayerItemLevel]
    labels: ArrayIterator[Label]
    league: League
    legend_statistics: PlayerLegendStatistics
    name: str
    player_house: PlayerHouse
    role: str
    spells: ArrayIterator[PlayerItemLevel]
    tag: str
    town_hall_level: int
    town_hall_weapon_level: int
    troops: ArrayIterator[PlayerItemLevel]
    trophies: int
    war_preference: str
    war_stars: int
