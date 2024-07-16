"""
``DeepLinkCreationResponse`` class
"""

from ...model_abc import Model, ModelWrapper


@ModelWrapper(main_attributes=['link'], exclude_annotations=None)
class DeepLinkCreationResponse(Model):
    link: str
