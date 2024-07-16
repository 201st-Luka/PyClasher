"""
``ServiceVersion`` class
"""

from ...model_abc import Model, ModelWrapper


@ModelWrapper(main_attributes=None, exclude_annotations=None)
class ServiceVersion(Model):
    content: int
    major: int
    minor: int
