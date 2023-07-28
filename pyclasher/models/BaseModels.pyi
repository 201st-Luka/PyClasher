"""
base models for this API wrapper client
"""

from typing import Any, Iterator

from ..Exceptions import MISSING, Missing


class BaseModel:
    """
    base model
    this model is a base for all other ClashOfClans API response models
    can be inherited from

    :cvar   _main_attribute:    the main attribute for generating the string representation of the class
    :type   _main_attribute:    Any | list[Any, ...] | tuple[Any, ...]
    :cvar   _data:             the model's data
    :type   _data:             dict
    """

    _main_attribute: Any | list[Any, ...] | tuple[Any, ...] = None
    _data: Missing | dict | None = MISSING

    def __new__(cls, data: Missing | dict = None) -> BaseModel:
        ...

    def __init__(self, data: Missing | dict = None) -> None:
        """
        initialisation of the base model

        :param  data:   the data dictionary, None or MISSING
        :return:        None
        :rtype:         None
        """
        self._data = data

    def to_dict(self) -> None | Missing | dict:
        """
        method that returns the response as a dict

        :return:    response as a dict
        :rtype:     dict | None | Missing
        """
        ...

    def _get_properties(self) -> None | Missing | dict:
        """
        protected method that returns a dict of the properties of a class (also works with inherited classes) or None or MISSING if the data is not defined

        key:    name of the property

        value:  value of the property

        :return:    dict of properties
        :rtype:     dict
        """
        ...

    def _get_data(self, item: str) -> None | Missing | dict | list | int | str | float | bool:
        """
        getter for the data class attribute that handles errors if the data is not defined

        :param item:            the key of the dict item
        :type item:             str
        :return:                the value of the key or MISSING
        :rtype:                 dict | list | int | str | float | bool | None | MISSING
        :raises RequestNotDone: if the data is not defined (MISSING)
        """
        ...

    def __str__(self) -> str:
        ...

    def __repr__(self) -> str:
        ...


class IterBaseModel:
    """
    iterative base model
    this model is an iterative base model for the ClashOfClans API response models
    can be inherited from

    :cvar   _len:               length of the iterative data
    :type   _len:               int
    :cvar   _main_attribute:    the main attribute for generating the string representation of the class
    :type   _main_attribute:    Any | list[Any, ...] | tuple[Any, ...]
    :cvar   _iter_rtype:        the type that is returned it iterated over the model
    :type   _iter_rtype:        Any
    :ivar   _data:             a list of dicts containing the data
    :type   _data:             list[dict] | None
    """

    _len: int = None
    _main_attribute: Any = None
    _iter_rtype: Any = Any

    def __init__(self, data: list[dict] | None) -> None:
        """
        initialisation of the iterative base model

        :param data:    a list of dicts containing the data
        :type data:     list[dict] | None
        :return:        None
        :rtype:         None
        """

        self._data = data
        if self._data is not None:
            self._len = len(self._data)
        self._main_attribute = self._len

    def to_dict_list(self) -> list[dict] | None | MISSING:
        """
        method that returns the response as a list of dicts

        :return:    response as a list of dicts
        :rtype:     list[dict] | None | Missing
        """
        ...

    def __len__(self) -> int:
        ...

    def __getitem__(self, item: int) -> _iter_rtype:
        ...

    def __iter__(self) -> Iterator[_iter_rtype]:
        self._iter = iter(self._data)
        ...

    def __next__(self):
        ...

    def __contains__(self, item) -> bool:
        ...

    def __str__(self) -> str:
        ...

    def __repr__(self) -> str:
        ...


class ImageUrl:
    """
    image URL model

    :cvar   __url:  URL of the image
    :tpye   __url:  str
    """

    __url: str = None

    def __init__(self, url: str) -> None:
        """
        initialisation of the image url model
        """
        self.__url = url

    async def get_image(self):
        """
        NOT IMPLEMENTED YET

        coroutine that retrieves the image of the URL
        """
        ...

    @property
    def url(self) -> str:
        """
        URL of the image

        :return:    the URL of the image
        :rtype:     str
        """
        ...

    def __repr__(self) -> str:
        ...

    def __str__(self) -> str:
        ...


class IconUrl(ImageUrl):
    """
    Holds an icon url
    """


class IconUrls(BaseModel):
    """
    icon URLs model that contains 3 icon URLs
    """

    @property
    def tiny(self) -> Missing | IconUrl:
        """
        tiny icon URL

        :return:    the tiny icon URL or MISSING if the tiny icon URL is not supported for a model
        :rtype:     Missing | IconUrl
        """
        ...

    @property
    def small(self) -> IconUrl:
        """
        small icon URL

        :return:    the small icon URL
        :rtype:     str
        """
        ...

    @property
    def medium(self) -> IconUrl | MISSING:
        """
        medium icon URL

        :return:    the medium icon URL or MISSING if the medium icon URL is not supported for a model
        :rtype:     str | Missing
        """
        ...


class After:
    """
    after model
    """

    def __init__(self, after: str) -> None:
        """
        initialisation of the after model

        :return:    None
        :rtype:     None
        """
        self._data = after

    @property
    def value(self) -> str:
        """
        value of the after model

        :return:    the value of the after model
        :rtype:     str
        """
        ...

    def __repr__(self) -> str:
        ...

    def __str__(self) -> str:
        ...


class Before:
    """
    before model
    """

    def __init__(self, before: str) -> None:
        """
        initialisation of the before model

        :return:    None
        :rtype:     None
        """
        self.__response = before

    @property
    def value(self) -> str:
        """
        value of the before model

        :return:    the value of the before model
        :rtype:     str
        """
        ...

    def __repr__(self) -> str:
        ...

    def __str__(self) -> str:
        ...


class Cursor(BaseModel):
    """
    cursor model
    """

    @property
    def after(self) -> Missing | After:
        ...

    @property
    def before(self) -> Missing | Before:
        ...


class Paging(BaseModel):
    """
    Holds information about the paging of the clan war log
    """

    @property
    def cursor(self) -> Cursor:
        ...


class BadgeUrl(ImageUrl):
    """
    class to hold a url for one badge
    """


class BadgeUrls(BaseModel):
    """
    class to hold data of a clan badge
    """

    @property
    def small(self) -> BadgeUrl:
        """
        small badge URL

        :return:    the small badge URL
        :rtype:     BadgeUrl
        """
        ...

    @property
    def medium(self) -> BadgeUrl:
        """
        medium badge URL

        :return:    the medium badge URL
        :rtype:     BadgeUrl
        """
        ...

    @property
    def large(self) -> BadgeUrl:
        """
        large badge URL

        :return:    the large badge URL
        :rtype:     BadgeUrl
        """
        ...


class Time:
    """
    time model

    :cvar   time_format:    time format of the string class method
    :type   time_format:    str
    :ivar   year:           year of the date and time
    :type   year:           int
    :ivar   month:          month of the date and time
    :type   month:          int
    :ivar   day:            day of the date and time
    :type   day:            int
    :ivar   hour:           hour of the date and time
    :type   hour:           int
    :ivar   minute:         minute of the date and time
    :type   minute:         int
    :ivar   second:         second of the date and time
    :type   second:         int
    :ivar   microsecond:    microsecond of the date and time
    :type   microsecond:    int
    """

    time_format: str = "%Y%m%dT%H%M%S.%fZ"

    def __init__(self,
                 year: int,
                 month: int,
                 day: int,
                 hour: int,
                 minute: int,
                 second: int,
                 microsecond: int) -> None:
        """
        initialisation of the time model

        :param  year:           year of the date and time
        :type   year:           int
        :param  month:          month of the date and time
        :type   month:          int
        :param  day:            day of the date and time
        :type   day:            int
        :param  hour:           hour of the date and time
        :type   hour:           int
        :param  minute:         minute of the date and time
        :type   minute:         int
        :param  second:         second of the date and time
        :type   second:         int
        :param  microsecond:    microsecond of the date and time
        :type   microsecond:    int
        """

        self._year = year
        self._month = month
        self._day = day
        self._hour = hour
        self._minute = minute
        self._second = second
        self._microsecond = microsecond

    @property
    def year(self) -> int:
        """
        year of the date and time

        :return:    the year of the date and time
        :rtype:     int
        """
        ...

    @property
    def month(self) -> int:
        """
        month of the date and time

        :return:    the month of the date and time
        :rtype:     int
        """
        ...

    @property
    def day(self) -> int:
        """
        day of the date and time

        :return:    the day of the date and time
        :rtype:     int
        """
        ...

    @property
    def hour(self) -> int:
        """
        hour of the date and time

        :return:    the hour of the date and time
        :rtype:     int
        """
        ...

    @property
    def minute(self) -> int:
        """
        minute of the date and time

        :return:    the minute of the date and time
        :rtype:     int
        """
        ...

    @property
    def second(self) -> int:
        """
        second of the date and time

        :return:    the second of the date and time
        :rtype:     int
        """
        ...

    @property
    def microsecond(self) -> int:
        """
        microsecond of the date and time

        :return:    the microsecond of the date and time
        :rtype:     int
        """
        ...

    @classmethod
    def from_str(cls, time: str) -> Time:
        """
        class method that converts a string with the format yyyymmddThhmmss.000Z

        :param time:                the time string following the format '%Y%m%dT%H%M%S.%fZ'
        :type time:                 str
        :return:                    a Time instance
        :rtype:                     Time
        :raise InvalidTimeFormat:   raises InvalidTimeFormat if the time does not match the format '%Y%m%dT%H%M%S.%fZ'
        """
        ...

    def __eq__(self, other) -> bool:
        ...

    def __ne__(self, other) -> bool:
        ...

    def __lt__(self, other) -> bool:
        ...

    def __le__(self, other) -> bool:
        ...

    def __gt__(self, other) -> bool:
        ...

    def __ge__(self, other) -> bool:
        ...

    def __str__(self) -> str:
        ...

    def __repr__(self) -> str:
        ...

    def __add__(self, other) -> Time:
        ...

    def __sub__(self, other) -> Time:
        ...


class BaseClanMember(BaseModel):
    """
    base clan member model
    """

    @property
    def tag(self) -> str:
        """
        clan member's tag

        :return:    the clan member's tag
        :rtype:     str
        """
        ...

    @property
    def name(self) -> str:
        """
        clan member's name

        :return:    the clan member's name
        :rtype:     str
        """
        ...


class BaseLeague(BaseModel):
    """
    base league model
    """

    @property
    def id(self) -> int:
        """
        league id

        :return:    the league id
        :rtype:     int
        """
        ...

    @property
    def name(self) -> str:
        """
        league name

        :return:    the league name
        :rtype:     str
        """
        ...


class BaseClan(BaseModel):
    """
    base clan model
    """

    @property
    def tag(self) -> str:
        """
        clan tag

        :return:    the clan's tag
        :rtype:     str
        """
        ...

    @property
    def name(self) -> str:
        """
        clan name

        :return:    the clan's name
        :rtype:     str
        """
        ...

    @property
    def badge_urls(self) -> BadgeUrls:
        """
        clan badge URLs

        :return:    the clan's badge URLs
        :rtype:     BadgeUrls
        """
        ...
