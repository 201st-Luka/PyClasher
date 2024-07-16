"""
``ClanDistrictData`` class
"""

from ...model_abc import Model, ModelWrapper


@ModelWrapper(main_attributes=None, exclude_annotations=None)
class ClanDistrictData(Model):
    district_hall_level: int
    id: int
    name: str
