"""
``ClanWarLogEntry`` class
"""

from .WarClan import WarClan
from ...model_abc import Model, ModelWrapper


@ModelWrapper(main_attributes=None, exclude_annotations=None)
class ClanWarLogEntry(Model):
    clan: WarClan
    opponent: WarClan
    team_size: int
    attacks_per_member: int
    battle_modifier: str
    end_time: str
    result: str
