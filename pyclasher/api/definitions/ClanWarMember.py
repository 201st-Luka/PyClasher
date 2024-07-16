"""
``ClanWarMember`` class
"""

from .ClanWarAttack import ClanWarAttack
from ...model_abc import Model, ModelWrapper, ArrayIterator


@ModelWrapper(main_attributes=['tag'], exclude_annotations=None)
class ClanWarMember(Model):
    attacks: ArrayIterator[ClanWarAttack]
    best_opponent_attack: ClanWarAttack
    map_position: int
    name: str
    opponent_attacks: int
    tag: str
    townhall_level: int
