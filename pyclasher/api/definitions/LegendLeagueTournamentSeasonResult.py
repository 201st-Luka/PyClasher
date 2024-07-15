"""
``LegendLeagueTournamentSeasonResult`` class
"""

from ...model_abc import Model, ModelWrapper


@ModelWrapper(main_attributes=None, exclude_annotations=None)
class LegendLeagueTournamentSeasonResult(Model):
    trophies: int
    id: str
    rank: int
