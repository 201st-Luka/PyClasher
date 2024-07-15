"""
``Location`` class
"""

from ...model_abc import Model, ModelWrapper


@ModelWrapper(main_attributes=None, exclude_annotations=None)
class Location(Model):
    localized_name: str
    id: int
    name: str
    is_country: bool
    country_code: str
