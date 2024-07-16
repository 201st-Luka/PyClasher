"""
``LegendLeagueTournamentSeasonResult`` class
"""

from ...model_abc import Model, ModelWrapper


@ModelWrapper(main_attributes=None, exclude_annotations=None)
class LegendLeagueTournamentSeasonResult(Model):
    id: str
    rank: int
    trophies: int
