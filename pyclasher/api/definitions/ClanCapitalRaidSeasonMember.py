"""
``ClanCapitalRaidSeasonMember`` class
"""

from ...model_abc import Model, ModelWrapper


@ModelWrapper(main_attributes=None, exclude_annotations=None)
class ClanCapitalRaidSeasonMember(Model):
    tag: str
    name: str
    attacks: int
    attack_limit: int
    bonus_attack_limit: int
    capital_resources_looted: int
