"""
``PlayerRanking`` class
"""

from .League import League
from .PlayerRankingClan import PlayerRankingClan
from ...model_abc import Model, ModelWrapper


@ModelWrapper(main_attributes=['tag'], exclude_annotations=None)
class PlayerRanking(Model):
    attack_wins: int
    clan: PlayerRankingClan
    defense_wins: int
    exp_level: int
    league: League
    name: str
    previous_rank: int
    rank: int
    tag: str
    trophies: int
