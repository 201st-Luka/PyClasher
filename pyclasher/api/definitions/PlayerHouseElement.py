"""
``PlayerHouseElement`` class
"""

from ...model_abc import Model, ModelWrapper


@ModelWrapper(main_attributes=['id'], exclude_annotations=None)
class PlayerHouseElement(Model):
    id: int
    type: str
