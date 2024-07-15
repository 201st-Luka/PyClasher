"""
``DeepLinkCreationRequest`` class
"""

from .String import String
from ...model_abc import ArrayIterator, Model, ModelWrapper


@ModelWrapper(main_attributes=None, exclude_annotations=None)
class DeepLinkCreationRequest(Model):
    player_tags: ArrayIterator[String]
    clan_tag: str
    opponent_clan_tag: str
