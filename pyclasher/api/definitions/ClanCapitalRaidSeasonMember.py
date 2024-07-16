"""
``ClanCapitalRaidSeasonMember`` class
"""

from ...model_abc import Model, ModelWrapper


@ModelWrapper(main_attributes=None, exclude_annotations=None)
class ClanCapitalRaidSeasonMember(Model):
    attack_limit: int
    attacks: int
    bonus_attack_limit: int
    capital_resources_looted: int
    name: str
    tag: str
