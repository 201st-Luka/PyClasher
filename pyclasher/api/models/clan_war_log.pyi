from typing import Iterator, Literal

from .abc import IterBaseModel, BaseModel
from .base_models import Time
from .enums import ClanWarResult
from .war_clan import WarClan


__all__ = (
    'ClanWarLog',
    'ClanWarLogEntry',
)


class ClanWarLogEntry(BaseModel):
    """
    clan war log entry model
    """

    @property
    def clan(self) -> WarClan:
        """
        clan of the clan war

        :return:    the clan of the clan war
        :rtype:     WarClan
        """
        ...

    @property
    def opponent(self) -> WarClan:
        """
        opponent of the clan war

        :return:    the opponent of the clan war
        :rtype:     WarClan
        """
        ...

    @property
    def team_size(self) -> int:
        """
        clan war team size

        :return:    the clan war team size
        :rtype:     int
        """
        ...

    @property
    def attacks_per_member(self) -> int:
        """
        attack count per member

        :return:    the attack count per member (usually 2 for regular war and 1 for clan war league)
        :rtype:     int
        """
        ...

    @property
    def end_time(self) -> Time:
        """
        end time of the clan war

        :return:    the end time of the clan war
        :rtype:     Time
        """
        ...

    @property
    def result(self) -> ClanWarResult:
        """
        result of the clan war

        :return:    the result of the clan war
        :rtype:     ClanWarResult
        """
        ...


class ClanWarLog(IterBaseModel):
    """
    clan war log model

    can be iterated over
    """

    _iter_rtype = ClanWarLogEntry
    __Criteria = Literal["team_size", "attacks_per_member", "result"]

    @property
    def average_team_size(self) -> None | float:
        ...

    @property
    def average_destruction_percentage(self) -> None | float:
        ...

    @property
    def average_attacks(self) -> None | float:
        ...

    @property
    def average_stars(self) -> None | float:
        ...

    @property
    def average_exp_earned(self) -> None | float:
        ...

    @staticmethod
    def __sort_key(item: dict, key: str) -> int:
        ...

    def sort(self, criteria: __Criteria, descending=True) -> None:
        ...

    def filter(self, criteria: __Criteria, value: int | ClanWarResult) -> None:
        ...

    def __getitem__(self, item: int) -> ClanWarLogEntry:
        ...

    def __iter__(self) -> Iterator[ClanWarLogEntry]:
        ...

    def __next__(self) -> ClanWarLogEntry:
        ...
