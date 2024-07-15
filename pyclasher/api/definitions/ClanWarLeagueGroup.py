"""
``ClanWarLeagueGroup`` class
"""

from .ClanWarLeagueClan import ClanWarLeagueClan
from .ClanWarLeagueRound import ClanWarLeagueRound
from ...model_abc import ArrayIterator, Model, ModelWrapper


@ModelWrapper(main_attributes=None, exclude_annotations=None)
class ClanWarLeagueGroup(Model):
    tag: str
    state: str
    season: str
    clans: ArrayIterator[ClanWarLeagueClan]
    rounds: ArrayIterator[ClanWarLeagueRound]
