"""
``CapitalLeague`` class
"""

from ...model_abc import Model, ModelWrapper


@ModelWrapper(main_attributes=['id'], exclude_annotations=None)
class CapitalLeague(Model):
    id: int
    name: str
