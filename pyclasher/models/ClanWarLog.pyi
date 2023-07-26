from .BaseModels import IterBaseModel, BaseModel, Time
from .Enums import ClanWarResult
from .WarClan import WarClan


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

    def __getitem__(self, item: int) -> ClanWarLogEntry:
        ...

    def __next__(self) -> ClanWarLogEntry:
        ...
