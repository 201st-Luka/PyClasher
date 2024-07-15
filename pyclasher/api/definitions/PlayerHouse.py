"""
``PlayerHouse`` class
"""

from .PlayerHouseElement import PlayerHouseElement
from ...model_abc import ArrayIterator, Model, ModelWrapper


@ModelWrapper(main_attributes=None, exclude_annotations=None)
class PlayerHouse(Model):
    elements: ArrayIterator[PlayerHouseElement]
