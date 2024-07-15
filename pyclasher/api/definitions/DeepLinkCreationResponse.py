"""
``DeepLinkCreationResponse`` class
"""

from ...model_abc import Model, ModelWrapper


@ModelWrapper(main_attributes=None, exclude_annotations=None)
class DeepLinkCreationResponse(Model):
    link: str
