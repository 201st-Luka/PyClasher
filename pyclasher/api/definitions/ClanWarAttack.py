"""
``ClanWarAttack`` class
"""

from ...model_abc import Model, ModelWrapper


@ModelWrapper(main_attributes=None, exclude_annotations=None)
class ClanWarAttack(Model):
    order: int
    attacker_tag: str
    defender_tag: str
    stars: int
    destruction_percentage: int
    duration: int
