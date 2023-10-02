from .abc import BaseModel
from .base_models import Time
from .enums import ClanWarState
from .war_clan import WarClan


__all__ = (
    'ClanWar',
)


class ClanWar(BaseModel):
    @property
    def clan(self) -> WarClan:
        """
        clan in the war

        :return:    the clan in the war
        :rtype:     WarClan
        """
        ...

    @property
    def opponent(self) -> WarClan:
        """
        opponent

        :return:    the clan's opponent
        :rtype:     WarClan
        """
        ...

    @property
    def team_size(self) -> int:
        """
        team size of the war

        :return:    the war's team size
        :rtype:     int
        """
        ...

    @property
    def attacks_per_member(self) -> int:
        """
        attacks per member (usually 2 for regular war and 1 for clan war league)

        :return:    the attacks per member
        :rtype:     int
        """
        ...

    @property
    def start_time(self) -> Time:
        """
        start time of the clan war

        :return:    the start time of the clan war
        :rtype:     Time
        """
        ...

    @property
    def state(self) -> ClanWarState:
        """
        state of the clan war

        :return:    the state of the clan war
        :rtype:     ClanWarState
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
    def preparation_start_time(self) -> Time:
        """
        preparation start time of the clan war

        :return:    the preparation start time of the clan war
        :rtype:     Time
        """
        ...
