from typing import Iterator

from ..abc import BaseModel, IterBaseModel
from ..base_models import Time
from ..enums import ClanWarState


__all__ = (
    'WarStatus',
    'WarStatusList'
)


class WarStatus(BaseModel):
    """
    war status model
    """

    @property
    def status_code(self) -> int:
        """
        status code of the war

        :return:    the status code of the war
        :rtype:     int
        """
        ...

    @property
    def clan_tag(self) -> str:
        """
        clan_tag code of the war

        :return:    the clan_tag code of the war
        :rtype:     str
        """
        ...

    @property
    def enemy_clan_tag(self) -> str:
        """
        enemy_clan_tag code of the war

        :return:    the enemy_clan_tag code of the war
        :rtype:     str
        """
        ...

    @property
    def war_state(self) -> ClanWarState:
        """
        war_state code of the war

        :return:    the war_state code of the war
        :rtype:     ClanWarState
        """
        ...

    @property
    def timestamp(self) -> Time:
        """
        timestamp code of the war

        :return:    the timestamp code of the war
        :rtype:     Time
        """
        ...


class WarStatusList(IterBaseModel):
    """
    war status list model
    """

    _iter_rtype = WarStatus

    def __getitem__(self, item: int | str) -> WarStatus:
        ...

    def __iter__(self) -> Iterator[WarStatus]:
        ...

    def __next__(self) -> WarStatus:
        ...
