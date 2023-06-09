from .BaseModels import BaseModel, IterBaseModel, BaseClanMember, BaseClan
from .Enums import ClanWarLeagueGroupState


class ClanWarLeagueRound(BaseModel):
    """
    clan war league round model
    """

    @property
    def war_tags(self) -> list[str]:
        """
        war tags of the CWL round

        :return:    the list of war tags
        :rtype:     list[str]
        """
        ...


class ClanWarLeagueRoundList(IterBaseModel):
    """
    clan war league round list model

    can be iterated over
    """

    _iter_rtype = ClanWarLeagueRound

    def __getitem__(self, item: int) -> _iter_rtype:
        ...

    def __next__(self) -> _iter_rtype:
        ...


class ClanWarLeagueClanMember(BaseClanMember):
    """
    clan war league clan member model
    """

    @property
    def townhall_level(self) -> int:
        """
        town hall level of the player

        :return:    the player's town hall level
        :rtype:     int
        """
        ...


class ClanWarLeagueClanMemberList(IterBaseModel):
    """
    clan war league clan member list model

    can be iterated over
    """

    _iter_rtype = ClanWarLeagueClanMember

    def __getitem__(self, item: int) -> _iter_rtype:
        ...

    def __next__(self) -> _iter_rtype:
        ...


class ClanWarLeagueClan(BaseClan):
    """
    clan war league clan model
    """

    @property
    def clan_level(self) -> int:
        """
        clan level

        :return:    the clan level
        :rtype:     int
        """
        ...

    @property
    def members(self) -> ClanWarLeagueClanMemberList:
        """
        clan members

        :return:    the list of clan members
        :rtype:     ClanWarLeagueClanMemberList
        """
        ...


class ClanWarLeagueClanList(IterBaseModel):
    """
    clan war league clan list model

    can be iterated over
    """

    _iter_rtype = ClanWarLeagueClan

    def __getitem__(self, item: int) -> _iter_rtype:
        ...

    def __next__(self) -> _iter_rtype:
        ...


class ClanWarLeagueGroup(BaseModel):
    """
    clan war league group model
    """

    @property
    def tag(self) -> str:
        """
        group tag

        :return:    the group tag
        :rtype:     str
        """
        ...

    @property
    def state(self) -> ClanWarLeagueGroupState:
        """
        group state

        :return:    the group state
        :rtype:     ClanWarLeagueGroupState
        """
        ...

    @property
    def season(self) -> str:
        """
        clan war league season

        :return:    the clan war league season
        :rtype:     str
        """
        ...

    @property
    def clans(self) -> ClanWarLeagueClanList:
        """
        group clans

        :return:    the list of group clans
        :rtype:     ClanWarLeagueClanList
        """
        ...

    @property
    def rounds(self) -> ClanWarLeagueRoundList:
        """
        group rounds

        :return:    the list of group rounds
        :rtype:     ClanWarLeagueRoundList
        """
        ...
