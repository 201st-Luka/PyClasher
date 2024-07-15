"""
``ServiceVersion`` class
"""

from ...model_abc import Model, ModelWrapper


@ModelWrapper(main_attributes=None, exclude_annotations=None)
class ServiceVersion(Model):
    major: int
    minor: int
    content: int
