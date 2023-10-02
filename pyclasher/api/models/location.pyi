"""
models concerning the location
"""
from typing import Iterator

from .abc import IterBaseModel, BaseModel
from ...exceptions import Missing


__all__ = (
    'Location',
    'LocationList',
)


class Location(BaseModel):
    """
    location model
    """

    @property
    def localized_name(self) -> str:
        """
        localized name of the location

        :return:    the location's localized name
        :rtype:     str
        """
        ...

    @property
    def id(self) -> int:
        """
        location ID

        :return:    the ID of the location
        :rtype:     int
        """
        ...

    @property
    def name(self) -> str:
        """
        location name

        :return:    the name of the location
        :rtype:     str
        """
        ...

    @property
    def country_code(self) -> Missing | str:
        """
        location country code

        :return:    the country code of the location if available
        :rtype:     int | MISSING
        """
        ...


class LocationList(IterBaseModel):
    """
    location list model

    can be iterated over
    """

    _iter_rtype = Location

    def __getitem__(self, item: int | str) -> Location:
        ...

    def __iter__(self) -> Iterator[Location]:
        ...

    def __next__(self) -> Location:
        ...
