"""
``PlayerItemLevel`` class
"""

from ...model_abc import Model, ModelWrapper, ArrayIterator


@ModelWrapper(main_attributes=None, exclude_annotations=None)
class PlayerItemLevel(Model):
    equipment: ArrayIterator[PlayerItemLevel]
    level: int
    max_level: int
    name: str
    super_troop_is_active: bool
    village: str
