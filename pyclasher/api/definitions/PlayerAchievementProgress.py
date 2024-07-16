"""
``PlayerAchievementProgress`` class
"""

from ...model_abc import Model, ModelWrapper


@ModelWrapper(main_attributes=None, exclude_annotations=None)
class PlayerAchievementProgress(Model):
    completion_info: str
    info: str
    name: str
    stars: int
    target: int
    value: int
    village: str
