"""
``ClanWarLogEntry`` class
"""

from .WarClan import WarClan
from ...model_abc import Model, ModelWrapper


@ModelWrapper(main_attributes=['clan', 'opponent', 'end_time'], exclude_annotations=None)
class ClanWarLogEntry(Model):
    attacks_per_member: int
    battle_modifier: str
    clan: WarClan
    end_time: str
    opponent: WarClan
    result: str
    team_size: int
