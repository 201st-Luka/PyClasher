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
from ...model_abc import ArrayIterator, Model, ModelWrapper


@ModelWrapper(main_attributes=None, exclude_annotations=None)
class Player(Model):
    league: League
    builder_base_league: BuilderBaseLeague
    clan: PlayerClan
    role: str
    war_preference: str
    attack_wins: int
    defense_wins: int
    town_hall_level: int
    town_hall_weapon_level: int
    legend_statistics: PlayerLegendStatistics
    troops: ArrayIterator[PlayerItemLevel]
    heroes: ArrayIterator[PlayerItemLevel]
    hero_equipment: ArrayIterator[PlayerItemLevel]
    spells: ArrayIterator[PlayerItemLevel]
    labels: ArrayIterator[Label]
    tag: str
    name: str
    exp_level: int
    trophies: int
    best_trophies: int
    donations: int
    donations_received: int
    builder_hall_level: int
    builder_base_trophies: int
    best_builder_base_trophies: int
    war_stars: int
    achievements: ArrayIterator[PlayerAchievementProgress]
    clan_capital_contributions: int
    player_house: PlayerHouse
