"""
``PlayerLegendStatistics`` class
"""

from .LegendLeagueTournamentSeasonResult import LegendLeagueTournamentSeasonResult
from ...model_abc import Model, ModelWrapper


@ModelWrapper(main_attributes=None, exclude_annotations=None)
class PlayerLegendStatistics(Model):
    current_season: LegendLeagueTournamentSeasonResult
    previous_season: LegendLeagueTournamentSeasonResult
    previous_builder_base_season: LegendLeagueTournamentSeasonResult
    best_builder_base_season: LegendLeagueTournamentSeasonResult
    best_season: LegendLeagueTournamentSeasonResult
    legend_trophies: int
