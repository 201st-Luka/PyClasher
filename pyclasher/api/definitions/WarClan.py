"""
``WarClan`` class
"""

from .ClanWarMember import ClanWarMember
from ...model_abc import Model, ModelWrapper, ArrayIterator


@ModelWrapper(main_attributes=['tag'], exclude_annotations=None)
class WarClan(Model):
    attacks: int
    badge_urls: dict
    clan_level: int
    destruction_percentage: float
    exp_earned: int
    members: ArrayIterator[ClanWarMember]
    name: str
    stars: int
    tag: str
