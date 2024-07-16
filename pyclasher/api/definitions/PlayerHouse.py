"""
``PlayerHouse`` class
"""

from .PlayerHouseElement import PlayerHouseElement
from ...model_abc import Model, ModelWrapper, ArrayIterator


@ModelWrapper(main_attributes=None, exclude_annotations=None)
class PlayerHouse(Model):
    elements: ArrayIterator[PlayerHouseElement]
