"""
``ClientError`` class
"""

from ...model_abc import Model, ModelWrapper


@ModelWrapper(main_attributes=['reason'], exclude_annotations=None)
class ClientError(Model):
    detail: dict
    message: str
    reason: str
    type: str
