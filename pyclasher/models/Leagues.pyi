"""
models concerning the leagues
"""

from .BaseModels import BaseModel, IconUrls, IterBaseModel, BaseLeague


class League(BaseLeague):
    """
    league model
    """

    @property
    def icon_urls(self) -> IconUrls:
        """
        icon URLs of the league

        :return:    the icon URLs of the league
        :rtype:     IconUrls
        """
        ...


class BuilderBaseLeague(BaseLeague):
    """
    builder base league model
    """
    pass


class CapitalLeague(BaseLeague):
    """
    capital league model
    """
    pass


class WarLeague(BaseLeague):
    """
    war league model
    """
    pass


class LeagueList(IterBaseModel):
    """
    league list model

    can be iterated over
    """

    _iter_rtype = League

    def __getitem__(self, item: int | str) -> _iter_rtype:
        ...

    def __next__(self) -> _iter_rtype:
        ...


class BuilderBaseLeagueList(IterBaseModel):
    """
    builder base league list model

    can be iterated over
    """

    _iter_rtype = BuilderBaseLeague

    def __getitem__(self, item: int | str) -> _iter_rtype:
        ...

    def __next__(self) -> _iter_rtype:
        ...


class CapitalLeagueList(IterBaseModel):
    """
    capital league list model

    can be iterated over
    """

    _iter_rtype = CapitalLeague

    def __getitem__(self, item: int | str) -> _iter_rtype:
        ...

    def __next__(self) -> _iter_rtype:
        ...


class WarLeagueList(IterBaseModel):
    """
    war league list model

    can be iterated over
    """

    _iter_rtype = WarLeague

    def __getitem__(self, item: int) -> _iter_rtype:
        ...

    def __next__(self) -> _iter_rtype:
        ...


class LeagueSeason(BaseModel):
    """
    league season model
    """

    @property
    def id(self) -> str:
        """
        season ID

        :return:    the ID of the season
        :rtype:     str
        """
        ...


class LeagueSeasonList(IterBaseModel):
    """
    league season list model

    can be iterated over
    """

    _iter_rtype = LeagueSeason

    def __getitem__(self, item: int | str) -> _iter_rtype:
        ...

    def __next__(self) -> _iter_rtype:
        ...
