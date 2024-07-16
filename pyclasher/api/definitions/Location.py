"""
``Location`` class
"""

from ...model_abc import Model, ModelWrapper


@ModelWrapper(main_attributes=['id'], exclude_annotations=None)
class Location(Model):
    country_code: str
    id: int
    is_country: bool
    localized_name: str
    name: str
