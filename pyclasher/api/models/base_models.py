from datetime import datetime

from aiohttp import ClientSession

from .abc import BaseModel
from ...exceptions import InvalidTimeFormat, MISSING


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
    def __init__(self, url):
        self.__url = url
        return

    async def get_image(self, logger=MISSING) -> bytes:
        async with ClientSession() as session:
            async with session.get(self.url) as request:
                if request.status == 200:
                    logger.info(f"Successfully downloaded {self.url}")
                    return await request.read()

    async def save_image(self, filename, logger=MISSING):
        image = await self.get_image(logger)
        with open(filename, "wb") as file:
            file.write(image)

    @property
    def url(self):
        return self.__url

    def __repr__(self):
        return f"{self.__class__.__name__}(url={self.__url})"

    def __str__(self):
        return f"{self.__class__.__name__}({self.__url})"


class IconUrl(ImageUrl):
    pass


class IconUrls(BaseModel):
    def __init__(self, data: dict):
        super().__init__(data)
        return

    @property
    def tiny(self):
        return IconUrl(self._get_data('tiny'))

    @property
    def small(self):
        return IconUrl(self._get_data('small'))

    @property
    def medium(self):
        return IconUrl(self._get_data('medium'))


class After:
    """
    Holds the after string
    """

    def __init__(self, after):
        self._data = after
        return

    @property
    def value(self):
        return self._data

    def __repr__(self):
        return f"After(value={self.value})"

    def __str__(self):
        return f"After({self.value})"


class Before:
    def __init__(self, before):
        self._data = before
        return

    @property
    def value(self):
        return self._data

    def __repr__(self):
        return "Before()"

    def __str__(self):
        return f"Before(value={self.value})"


class Cursor(BaseModel):
    @property
    def after(self):
        return After(self._get_data('after'))

    @property
    def before(self):
        return Before(self._get_data('before'))


class Paging(BaseModel):
    @property
    def cursor(self) -> Cursor:
        return Cursor(self._get_data('cursors'))


class BadgeUrl(ImageUrl):
    pass


class BadgeUrls(BaseModel):
    @property
    def small(self):
        return BadgeUrl(self._get_data('small'))

    @property
    def medium(self):
        return BadgeUrl(self._get_data('medium'))

    @property
    def large(self):
        return BadgeUrl(self._get_data('large'))

    def __str__(self):
        return f"{self.__class__.__name__}({self.medium})"


class Time:
    time_format = "%Y%m%dT%H%M%S.%fZ"

    def __init__(self, year, month, day, hour, minute, second, microsecond):
        self._year = year
        self._month = month
        self._day = day
        self._hour = hour
        self._minute = minute
        self._second = second
        self._microsecond = microsecond
        return

    @property
    def year(self):
        return self._year

    @property
    def month(self):
        return self._month

    @property
    def day(self):
        return self._day

    @property
    def hour(self):
        return self._hour

    @property
    def minute(self):
        return self._minute

    @property
    def second(self):
        return self._second

    @property
    def microsecond(self):
        return self._microsecond

    @classmethod
    def from_str(cls, time):
        try:
            dt = datetime.strptime(time, cls.time_format)
        except ValueError:
            raise InvalidTimeFormat(time, cls.time_format)

        return cls(
            dt.year, dt.month, dt.day,
            dt.hour, dt.minute, dt.second, dt.microsecond
        )

    def __eq__(self, other):
        if isinstance(other, Time):
            return (self._year == other._year and self._month == other._month
                    and self._day == other._day and
                    self._hour == other._hour and self._minute == other._minute
                    and self._second == other._second)
        if isinstance(other, (Time, datetime)):
            return (self._year == other.year and self._month == other.month
                    and self._day == other.day and
                    self._hour == other.hour and self._minute == other.minute
                    and self._second == other.second)
        return NotImplemented

    def __ne__(self, other):
        return not self == other

    def __lt__(self, other):
        if isinstance(other, (Time, datetime)):
            if self._year < other.year:
                return True
            if self._year == other.year and self._month < other.month:
                return True
            if (self._year == other.year and self._month == other.month
                    and self._day < other.day):
                return True
            if (self._year == other.year and self._month == other.month
                    and self._day == other.day
                    and self._hour < other.hour):
                return True
            if (self._year == other.year and self._month == other.month
                    and self._day == other.day and self._hour == other.hour
                    and self._minute < other.minute):
                return True
            if (self._year == other.year and self._month == other.month
                    and self._day == other.day and self._hour == other.hour
                    and self._minute == other.minute
                    and self._second < other.second):
                return True
            if (self._year == other.year and self._month == other.month
                    and self._day == other.day and self._hour == other.hour
                    and self._minute == other.minute
                    and self._second == other.second
                    and self._microsecond < other.microsecond):
                return True
            return False
        return NotImplemented

    def __le__(self, other):
        return self == other or self < other

    def __gt__(self, other):
        return not self <= other

    def __ge__(self, other):
        return not self < other

    def __str__(self):
        return (f"Time({self._year}.{self._month}.{self._day}:"
                f"{self._hour}.{self._minute}.{self._second}"
                f".{self._microsecond})")

    def __repr__(self):
        return (f"Time(year={self._year}, month={self._month}, day={self._day},"
                f" hour={self._hour}, minute={self._minute}, "
                f"second={self._second}, microsecond={self._microsecond})")

    def __add__(self, other):
        if isinstance(other, (Time, datetime)):
            return Time(self._year + other.year, self._month + other.month,
                        self._day + other.day, self._hour + other.hour,
                        self._minute + other.minute,
                        self._second + other.second,
                        self._microsecond + other.microsecond)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, (Time, datetime)):
            return Time(self._year - other.year, self._month - other.month,
                        self._day - other.day, self._hour - other.hour,
                        self._minute - other.minute,
                        self._second - other.second,
                        self._microsecond - other.microsecond)
        return NotImplemented


class BaseClanMember(BaseModel):
    @property
    def tag(self):
        return self._get_data('tag')

    @property
    def name(self):
        return self._get_data('name')

    def __str__(self):
        return f"{self.__class__.__name__}({self.tag})"


class BaseLeague(BaseModel):
    @property
    def id(self):
        return self._get_data('id')

    @property
    def name(self):
        return self._get_data('name')

    def __str__(self):
        return f"{self.__class__.__name__}({self.id})"


class BaseClan(BaseModel):
    @property
    def tag(self):
        return self._get_data('tag')

    @property
    def name(self):
        return self._get_data('name')

    @property
    def badge_urls(self):
        return BadgeUrls(self._get_data('badgeUrls'))

    def __str__(self):
        return f"{self.__class__. __name__}({self.tag})"
