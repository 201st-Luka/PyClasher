"""
``ClanWarLeagueClanMember`` class
"""

from ...model_abc import Model, ModelWrapper


@ModelWrapper(main_attributes=None, exclude_annotations=None)
class ClanWarLeagueClanMember(Model):
    tag: str
    town_hall_level: int
    name: str
