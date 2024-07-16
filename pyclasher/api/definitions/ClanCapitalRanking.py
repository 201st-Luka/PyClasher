"""
``ClanCapitalRanking`` class
"""

from ...model_abc import Model, ModelWrapper


@ModelWrapper(main_attributes=None, exclude_annotations=None)
class ClanCapitalRanking(Model):
    clan_capital_points: int
    clan_points: int
