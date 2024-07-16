"""
``GoldPassSeason`` class
"""

from ...model_abc import Model, ModelWrapper


@ModelWrapper(main_attributes=['start_time'], exclude_annotations=None)
class GoldPassSeason(Model):
    end_time: str
    start_time: str
