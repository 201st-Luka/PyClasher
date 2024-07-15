"""
``WarClan`` class
"""

from .ClanWarMember import ClanWarMember
from ...model_abc import ArrayIterator, Model, ModelWrapper


@ModelWrapper(main_attributes=None, exclude_annotations=None)
class WarClan(Model):
    destruction_percentage: float
    tag: str
    name: str
    badge_urls: dict
    clan_level: int
    attacks: int
    stars: int
    exp_earned: int
    members: ArrayIterator[ClanWarMember]
