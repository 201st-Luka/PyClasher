"""
``ClanCapitalRaidSeasonAttack`` class
"""

from .ClanCapitalRaidSeasonAttacker import ClanCapitalRaidSeasonAttacker
from ...model_abc import Model, ModelWrapper


@ModelWrapper(main_attributes=None, exclude_annotations=None)
class ClanCapitalRaidSeasonAttack(Model):
    attacker: ClanCapitalRaidSeasonAttacker
    destruction_percent: int
    stars: int
