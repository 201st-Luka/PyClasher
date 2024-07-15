"""
``ClanWarMember`` class
"""

from .ClanWarAttack import ClanWarAttack
from ...model_abc import ArrayIterator, Model, ModelWrapper


@ModelWrapper(main_attributes=None, exclude_annotations=None)
class ClanWarMember(Model):
    tag: str
    name: str
    map_position: int
    townhall_level: int
    opponent_attacks: int
    best_opponent_attack: ClanWarAttack
    attacks: ArrayIterator[ClanWarAttack]
