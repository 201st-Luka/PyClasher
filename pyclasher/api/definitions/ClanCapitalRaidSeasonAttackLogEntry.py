"""
``ClanCapitalRaidSeasonAttackLogEntry`` class
"""

from .ClanCapitalRaidSeasonClanInfo import ClanCapitalRaidSeasonClanInfo
from .ClanCapitalRaidSeasonDistrict import ClanCapitalRaidSeasonDistrict
from ...model_abc import ArrayIterator, Model, ModelWrapper


@ModelWrapper(main_attributes=None, exclude_annotations=None)
class ClanCapitalRaidSeasonAttackLogEntry(Model):
    defender: ClanCapitalRaidSeasonClanInfo
    attack_count: int
    district_count: int
    districts_destroyed: int
    districts: ArrayIterator[ClanCapitalRaidSeasonDistrict]
