"""
``Label`` class
"""

from ...model_abc import Model, ModelWrapper


@ModelWrapper(main_attributes=None, exclude_annotations=None)
class Label(Model):
    name: str
    id: int
    icon_urls: dict
