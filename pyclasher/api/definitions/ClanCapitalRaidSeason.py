"""
``ClanCapitalRaidSeason`` class
"""

from .ClanCapitalRaidSeasonAttackLog import ClanCapitalRaidSeasonAttackLog
from .ClanCapitalRaidSeasonDefenseLog import ClanCapitalRaidSeasonDefenseLog
from .ClanCapitalRaidSeasonMember import ClanCapitalRaidSeasonMember
from ...model_abc import Model, ModelWrapper, ArrayIterator


@ModelWrapper(main_attributes=None, exclude_annotations=None)
class ClanCapitalRaidSeason(Model):
    attack_log: ArrayIterator[ClanCapitalRaidSeasonAttackLog]
    capital_total_loot: int
    defense_log: ArrayIterator[ClanCapitalRaidSeasonDefenseLog]
    defensive_reward: int
    end_time: str
    enemy_districts_destroyed: int
    members: ArrayIterator[ClanCapitalRaidSeasonMember]
    offensive_reward: int
    raids_completed: int
    start_time: str
    state: str
    total_attacks: int
