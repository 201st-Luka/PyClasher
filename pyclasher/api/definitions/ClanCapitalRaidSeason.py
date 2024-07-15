"""
``ClanCapitalRaidSeason`` class
"""

from .ClanCapitalRaidSeasonAttackLog import ClanCapitalRaidSeasonAttackLog
from .ClanCapitalRaidSeasonDefenseLog import ClanCapitalRaidSeasonDefenseLog
from .ClanCapitalRaidSeasonMember import ClanCapitalRaidSeasonMember
from ...model_abc import ArrayIterator, Model, ModelWrapper


@ModelWrapper(main_attributes=None, exclude_annotations=None)
class ClanCapitalRaidSeason(Model):
    attack_log: ArrayIterator[ClanCapitalRaidSeasonAttackLog]
    defense_log: ArrayIterator[ClanCapitalRaidSeasonDefenseLog]
    state: str
    start_time: str
    end_time: str
    capital_total_loot: int
    raids_completed: int
    total_attacks: int
    enemy_districts_destroyed: int
    offensive_reward: int
    defensive_reward: int
    members: ArrayIterator[ClanCapitalRaidSeasonMember]
