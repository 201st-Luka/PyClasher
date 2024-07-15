"""
``PlayerItemLevel`` class
"""

from ...model_abc import ArrayIterator, Model, ModelWrapper


@ModelWrapper(main_attributes=None, exclude_annotations=None)
class PlayerItemLevel(Model):
    level: int
    name: str
    max_level: int
    village: str
    super_troop_is_active: bool
    equipment: ArrayIterator[PlayerItemLevel]
