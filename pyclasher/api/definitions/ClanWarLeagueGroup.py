"""
``ClanWarLeagueGroup`` class
"""

from .ClanWarLeagueClan import ClanWarLeagueClan
from .ClanWarLeagueRound import ClanWarLeagueRound
from ...model_abc import Model, ModelWrapper, ArrayIterator


@ModelWrapper(main_attributes=['tag'], exclude_annotations=None)
class ClanWarLeagueGroup(Model):
    clans: ArrayIterator[ClanWarLeagueClan]
    rounds: ArrayIterator[ClanWarLeagueRound]
    season: str
    state: str
    tag: str
