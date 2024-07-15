"""
``League`` class
"""

from ...model_abc import Model, ModelWrapper


@ModelWrapper(main_attributes=None, exclude_annotations=None)
class League(Model):
    name: str
    id: int
    icon_urls: dict
