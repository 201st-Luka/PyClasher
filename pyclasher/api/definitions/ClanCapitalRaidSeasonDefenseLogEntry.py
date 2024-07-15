"""
``ClanCapitalRaidSeasonDefenseLogEntry`` class
"""

from .ClanCapitalRaidSeasonClanInfo import ClanCapitalRaidSeasonClanInfo
from .ClanCapitalRaidSeasonDistrict import ClanCapitalRaidSeasonDistrict
from ...model_abc import ArrayIterator, Model, ModelWrapper


@ModelWrapper(main_attributes=None, exclude_annotations=None)
class ClanCapitalRaidSeasonDefenseLogEntry(Model):
    attacker: ClanCapitalRaidSeasonClanInfo
    attack_count: int
    district_count: int
    districts_destroyed: int
    districts: ArrayIterator[ClanCapitalRaidSeasonDistrict]
