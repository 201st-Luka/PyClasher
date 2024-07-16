"""
``Label`` class
"""

from ...model_abc import Model, ModelWrapper


@ModelWrapper(main_attributes=['id'], exclude_annotations=None)
class Label(Model):
    icon_urls: dict
    id: int
    name: str
