"""
``PlayerRanking`` class
"""

from .League import League
from .PlayerRankingClan import PlayerRankingClan
from ...model_abc import Model, ModelWrapper


@ModelWrapper(main_attributes=None, exclude_annotations=None)
class PlayerRanking(Model):
    league: League
    clan: PlayerRankingClan
    attack_wins: int
    defense_wins: int
    tag: str
    name: str
    exp_level: int
    rank: int
    previous_rank: int
    trophies: int
