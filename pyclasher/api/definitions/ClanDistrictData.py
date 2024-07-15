"""
``ClanDistrictData`` class
"""

from ...model_abc import Model, ModelWrapper


@ModelWrapper(main_attributes=None, exclude_annotations=None)
class ClanDistrictData(Model):
    name: str
    id: int
    district_hall_level: int
