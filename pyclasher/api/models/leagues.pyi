"""
models concerning the leagues
"""
from typing import Iterator

from .abc import BaseModel, IterBaseModel
from .base_models import IconUrls, BaseLeague


__all__ = (
    'League',
    'LeagueList',
    'BuilderBaseLeague',
    'BuilderBaseLeagueList',
    'CapitalLeague',
    'CapitalLeagueList',
    'LeagueSeason',
    'LeagueSeasonList',
    'WarLeague',
    'WarLeagueList',
)


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

    def __getitem__(self, item: int | str) -> League:
        ...

    def __iter__(self) -> Iterator[League]:
        ...

    def __next__(self) -> League:
        ...


class BuilderBaseLeagueList(IterBaseModel):
    """
    builder base league list model

    can be iterated over
    """

    _iter_rtype = BuilderBaseLeague

    def __getitem__(self, item: int | str) -> BuilderBaseLeague:
        ...

    def __iter__(self) -> Iterator[BuilderBaseLeague]:
        ...

    def __next__(self) -> BuilderBaseLeague:
        ...


class CapitalLeagueList(IterBaseModel):
    """
    capital league list model

    can be iterated over
    """

    _iter_rtype = CapitalLeague

    def __getitem__(self, item: int | str) -> CapitalLeague:
        ...

    def __iter__(self) -> Iterator[CapitalLeague]:
        ...

    def __next__(self) -> CapitalLeague:
        ...


class WarLeagueList(IterBaseModel):
    """
    war league list model

    can be iterated over
    """

    _iter_rtype = WarLeague

    def __getitem__(self, item: int) -> WarLeague:
        ...

    def __iter__(self) -> Iterator[WarLeague]:
        ...

    def __next__(self) -> WarLeague:
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

    def __getitem__(self, item: int | str) -> LeagueSeason:
        ...

    def __iter__(self) -> Iterator[LeagueSeason]:
        ...

    def __next__(self) -> LeagueSeason:
        ...
