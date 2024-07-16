"""
``WarStatus`` class
"""

from ...model_abc import Model, ModelWrapper


@ModelWrapper(main_attributes=None, exclude_annotations=None)
class WarStatus(Model):
    clan_tag: str
    enemy_clan_tag: str
    status_code: int
    timestamp: str
    war_state: str
