"""
``ClanWarLeagueRound`` class
"""

from .String import String
from ...model_abc import Model, ModelWrapper, ArrayIterator


@ModelWrapper(main_attributes=None, exclude_annotations=None)
class ClanWarLeagueRound(Model):
    war_tags: ArrayIterator[String]
