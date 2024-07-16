"""
``ClanCapitalRaidSeasonDefenseLogEntry`` class
"""

from .ClanCapitalRaidSeasonClanInfo import ClanCapitalRaidSeasonClanInfo
from .ClanCapitalRaidSeasonDistrict import ClanCapitalRaidSeasonDistrict
from ...model_abc import Model, ModelWrapper, ArrayIterator


@ModelWrapper(main_attributes=None, exclude_annotations=None)
class ClanCapitalRaidSeasonDefenseLogEntry(Model):
    attack_count: int
    attacker: ClanCapitalRaidSeasonClanInfo
    district_count: int
    districts: ArrayIterator[ClanCapitalRaidSeasonDistrict]
    districts_destroyed: int
