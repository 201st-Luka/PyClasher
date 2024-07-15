"""
``PlayerAchievementProgress`` class
"""

from ...model_abc import Model, ModelWrapper


@ModelWrapper(main_attributes=None, exclude_annotations=None)
class PlayerAchievementProgress(Model):
    stars: int
    value: int
    name: str
    target: int
    info: str
    completion_info: str
    village: str
