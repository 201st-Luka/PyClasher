"""
base models for this API wrapper client
"""
from logging import Logger

from .abc import BaseModel
from ...exceptions import MISSING, Missing


__all__ = (
    'ImageUrl',
    'IconUrl',
    'IconUrls',
    'After',
    'Before',
    'Cursor',
    'Paging',
    'BadgeUrl',
    'BadgeUrls',
    'Time',
    'BaseLeague',
    'BaseClanMember',
    'BaseClan'
)


class ImageUrl:
    """
    image URL model

    :ivar   __url:  URL of the image
    :type   __url:  str
    """

    def __init__(self, url: str) -> None:
        """
        initialisation of the image url model
        """
        self.__url = url

    async def get_image(self, logger: Logger = MISSING) -> bytes:
        ...

    async def save_image(self, logger: Logger):
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
        self._data = before

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
    class to hold an url for one badge
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
    :ivar   _year:          year of the date and time
    :type   _year:          int
    :ivar   _month:         month of the date and time
    :type   _month:         int
    :ivar   _day:           day of the date and time
    :type   _day:           int
    :ivar   _hour:          hour of the date and time
    :type   _hour:          int
    :ivar   _minute:        minute of the date and time
    :type   _minute:        int
    :ivar   _second:        second of the date and time
    :type   _second:        int
    :ivar   _microsecond:   microsecond of the date and time
    :type   _microsecond:   int
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
