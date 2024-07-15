"""
``ClanCapitalRaidSeasonDistrict`` class
"""

from .ClanCapitalRaidSeasonAttack import ClanCapitalRaidSeasonAttack
from ...model_abc import ArrayIterator, Model, ModelWrapper


@ModelWrapper(main_attributes=None, exclude_annotations=None)
class ClanCapitalRaidSeasonDistrict(Model):
    stars: int
    name: str
    id: int
    destruction_percent: int
    attack_count: int
    total_looted: int
    attacks: ArrayIterator[ClanCapitalRaidSeasonAttack]
    district_hall_level: int
