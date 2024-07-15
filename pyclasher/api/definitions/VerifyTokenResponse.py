"""
``VerifyTokenResponse`` class
"""

from ...model_abc import Model, ModelWrapper


@ModelWrapper(main_attributes=None, exclude_annotations=None)
class VerifyTokenResponse(Model):
    tag: str
    token: str
    status: str
