"""
``ClanWarLeagueClanMember`` class
"""

from ...model_abc import Model, ModelWrapper


@ModelWrapper(main_attributes=['tag'], exclude_annotations=None)
class ClanWarLeagueClanMember(Model):
    name: str
    tag: str
    town_hall_level: int
