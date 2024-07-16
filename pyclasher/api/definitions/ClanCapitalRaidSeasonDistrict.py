"""
``ClanCapitalRaidSeasonDistrict`` class
"""

from .ClanCapitalRaidSeasonAttack import ClanCapitalRaidSeasonAttack
from ...model_abc import Model, ModelWrapper, ArrayIterator


@ModelWrapper(main_attributes=None, exclude_annotations=None)
class ClanCapitalRaidSeasonDistrict(Model):
    attack_count: int
    attacks: ArrayIterator[ClanCapitalRaidSeasonAttack]
    destruction_percent: int
    district_hall_level: int
    id: int
    name: str
    stars: int
    total_looted: int
