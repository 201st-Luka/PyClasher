"""
models concerning the location
"""

from .BaseModels import IterBaseModel, BaseModel
from ..Exceptions import Missing


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
    def country_code(self) -> int | Missing:
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

    def __getitem__(self, item: int | str) -> _iter_rtype:
        ...

    def __next__(self) -> _iter_rtype:
        ...
