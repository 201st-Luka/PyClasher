"""
``ClanWarAttack`` class
"""

from ...model_abc import Model, ModelWrapper


@ModelWrapper(main_attributes=None, exclude_annotations=None)
class ClanWarAttack(Model):
    attacker_tag: str
    defender_tag: str
    destruction_percentage: int
    duration: int
    order: int
    stars: int
