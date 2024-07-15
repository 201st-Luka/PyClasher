"""
``ClanWar`` class
"""

from .WarClan import WarClan
from ...model_abc import Model, ModelWrapper


@ModelWrapper(main_attributes=None, exclude_annotations=None)
class ClanWar(Model):
    clan: WarClan
    opponent: WarClan
    team_size: int
    attacks_per_member: int
    battle_modifier: str
    start_time: str
    state: str
    end_time: str
    preparation_start_time: str
