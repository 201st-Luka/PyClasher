"""
``Language`` class
"""

from ...model_abc import Model, ModelWrapper


@ModelWrapper(main_attributes=['id'], exclude_annotations=None)
class Language(Model):
    id: int
    language_code: str
    name: str
