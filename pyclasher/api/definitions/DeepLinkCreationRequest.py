"""
``DeepLinkCreationRequest`` class
"""

from .String import String
from ...model_abc import Model, ModelWrapper, ArrayIterator


@ModelWrapper(main_attributes=None, exclude_annotations=None)
class DeepLinkCreationRequest(Model):
    clan_tag: str
    opponent_clan_tag: str
    player_tags: ArrayIterator[String]
