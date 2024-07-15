"""
``GoldPassSeason`` class
"""

from ...model_abc import Model, ModelWrapper


@ModelWrapper(main_attributes=None, exclude_annotations=None)
class GoldPassSeason(Model):
    start_time: str
    end_time: str
