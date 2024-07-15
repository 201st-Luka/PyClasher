"""
``ClanWarLeagueClan`` class
"""

from .ClanWarLeagueClanMember import ClanWarLeagueClanMember
from ...model_abc import ArrayIterator, Model, ModelWrapper


@ModelWrapper(main_attributes=None, exclude_annotations=None)
class ClanWarLeagueClan(Model):
    tag: str
    clan_level: int
    name: str
    members: ArrayIterator[ClanWarLeagueClanMember]
    badge_urls: dict
