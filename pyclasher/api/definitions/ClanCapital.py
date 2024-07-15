"""
``ClanCapital`` class
"""

from .ClanDistrictData import ClanDistrictData
from ...model_abc import ArrayIterator, Model, ModelWrapper


@ModelWrapper(main_attributes=None, exclude_annotations=None)
class ClanCapital(Model):
    capital_hall_level: int
    districts: ArrayIterator[ClanDistrictData]
