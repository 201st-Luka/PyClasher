"""
``ClanWar`` class
"""

from .WarClan import WarClan
from ...model_abc import Model, ModelWrapper


@ModelWrapper(main_attributes=['clan', 'opponent'], exclude_annotations=None)
class ClanWar(Model):
    attacks_per_member: int
    battle_modifier: str
    clan: WarClan
    end_time: str
    opponent: WarClan
    preparation_start_time: str
    start_time: str
    state: str
    team_size: int
