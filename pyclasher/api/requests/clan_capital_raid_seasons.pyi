from typing import Iterator

from .abc import IterRequestModel
from ..models import ClanCapitalRaidSeasons, ClanCapitalRaidSeason


__all__ = (
    'ClanCapitalRaidSeasonsRequest',
)


class ClanCapitalRaidSeasonsRequest(IterRequestModel):
    _iter_rtype = ClanCapitalRaidSeason
    _list_rtype = ClanCapitalRaidSeasons

    def __init__(self, clan_tag: str, limit: int = None, after: str = None, before: str = None):
        self.clan_tag = clan_tag
        ...

    @property
    def items(self) -> _list_rtype:
        ...

    def __getitem__(self, item: int) -> _iter_rtype:
        ...

    def __iter__(self) -> Iterator[_iter_rtype]:
        ...

    def __next__(self) -> _iter_rtype:
        ...

    @property
    def average_capital_total_loot_per_season(self) -> float:
        ...

    @property
    def average_raids_completed_per_season(self) -> float:
        ...

    @property
    def average_total_attacks_per_season(self) -> float:
        ...

    @property
    def average_enemy_districts_destroyed_per_season(self) -> float:
        ...

    @property
    def average_defensive_reward_per_season(self) -> float:
        ...

    @property
    def average_offensive_reward_per_season(self) -> float:
        ...
