"""
``WarLeague`` class
"""

from ...model_abc import Model, ModelWrapper


@ModelWrapper(main_attributes=None, exclude_annotations=None)
class WarLeague(Model):
    name: str
    id: int
