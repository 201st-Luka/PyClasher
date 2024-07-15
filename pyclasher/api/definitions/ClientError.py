"""
``ClientError`` class
"""

from ...model_abc import Model, ModelWrapper


@ModelWrapper(main_attributes=None, exclude_annotations=None)
class ClientError(Model):
    reason: str
    message: str
    type: str
    detail: dict
