"""
``ClanWarLeagueClan`` class
"""

from .ClanWarLeagueClanMember import ClanWarLeagueClanMember
from ...model_abc import Model, ModelWrapper, ArrayIterator


@ModelWrapper(main_attributes=['tag'], exclude_annotations=None)
class ClanWarLeagueClan(Model):
    badge_urls: dict
    clan_level: int
    members: ArrayIterator[ClanWarLeagueClanMember]
    name: str
    tag: str
