from datetime import datetime
from typing import Any, Self

from ..Exceptions import RequestNotDone, InvalidTimeString


class BaseModel:
    _main_attribute: Any | list[Any, ...] | tuple[Any, ...] = None
    _data: dict

    def __init__(self, data: dict | None):
        self._data = data
        return

    def to_dict(self) -> dict | None:
        return self._data

    def _get_properties(self) -> dict:
        return {name: prop.__get__(self) for name, prop in vars(type(self)).items() if isinstance(prop, property)}

    def _get_data(self, item: str) -> dict | list | int | str | float | bool | None:
        if self._data is None:
            raise RequestNotDone
        if item in self._data:
            return self._data[item]
        return None

    def __str__(self) -> str:
        try:
            main_attr = ",".join((str(attr) for attr in self._main_attribute)) if isinstance(self._main_attribute, (list, tuple)) else \
                str(self._main_attribute) if self._main_attribute is not None else ""
        except RequestNotDone:
            main_attr = "RequestNotDone"
        return f"{self.__class__.__name__}({main_attr})"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({', '.join(('='.join((key, str(value))) for key, value in self._get_properties().items()))})"


class IterBaseModel:
    _len: int = None
    _main_attribute: Any = None
    _iter_rtype: Any = Any

    def __init__(self, data: list[dict] | None):
        self._data = data
        if self._data is not None:
            self._len = len(self._data)
        self._main_attribute = self._len
        return

    def to_dict(self) -> dict | None:
        return self._data

    def __len__(self) -> int:
        return self._len

    def __getitem__(self, item: int) -> _iter_rtype:
        return self._iter_rtype(self._data[item])

    def __iter__(self):
        self._iter = iter(self._data)
        return self

    def __next__(self):
        return self._iter_rtype(next(self._iter))

    def __contains__(self, item) -> bool:
        if isinstance(item, (self._iter_rtype, str)):
            for s_item in self:
                if s_item == item:
                    return True
            return False
        return NotImplemented

    def __str__(self) -> str:
        return f"{self.__class__.__name__}({self._main_attribute})"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(len={self._len}, type={self._iter_rtype.__name__})"


class RequestEntryPointBaseModel(BaseModel):
    def _get_data(self, item: str) -> dict | list | int | str | float | bool | None | RequestNotDone:
        if self._data is None:
            return RequestNotDone
        if item in self._data:
            return self._data[item]
        return None


class ImageUrl:
    """
    Holds an image url and can return the content
    """

    __url: str = None

    def __init__(self, url: str):
        self.__url = url
        return

    async def get_image(self):
        ...

    @property
    def url(self) -> str:
        return self.__url

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(url={self.__url})"

    def __str__(self) -> str:
        return f"{self.__class__.__name__}({self.__url})"


class IconUrl(ImageUrl):
    """
    Holds an icon url
    """


class IconUrls(BaseModel):
    """
    Holds icon urls
    """

    def __init__(self, data: dict) -> None:
        super().__init__(data)
        self._main_attribute = self.small
        return

    @property
    def tiny(self) -> IconUrl | None:
        if 'tiny' in self._data:
            return IconUrl(self._data['tiny'])
        return None

    @property
    def small(self) -> IconUrl:
        return IconUrl(self._get_data('small'))

    @property
    def medium(self) -> IconUrl | None:
        if 'medium' in self._data:
            return IconUrl(self._get_data('medium'))
        return None


class After:
    """
    Holds the after string
    """

    def __init__(self, after: str):
        self.__response = after
        return

    @property
    def value(self) -> str:
        return self.__response

    def __repr__(self) -> str:
        return "After()"

    def __str__(self) -> str:
        return f"After(value={self.value})"


class Before:
    """
    Holds the before string
    """

    def __init__(self, before: str):
        self.__response = before
        return

    @property
    def value(self) -> str:
        return self.__response

    def __repr__(self) -> str:
        return "Before()"

    def __str__(self) -> str:
        return f"Before(value={self.value})"


class Cursor:
    """
    Holds information about the cursor on the war log pages
    """

    def __init__(self, cursor: dict) -> None:
        self.__response = cursor
        return

    @property
    def after(self) -> After | None:
        return After(self.__response['after']) if 'after' in self.__response else None

    @property
    def before(self) -> Before | None:
        return Before(self.__response['before']) if 'before' in self.__response else None

    def __repr__(self) -> str:
        return "Cursor"

    def __str__(self) -> str:
        return f"Cursor({self.after}, {self.before})"


class Paging:
    """
    Holds information about the paging of the clan war log
    """

    def __init__(self, paging: dict) -> None:
        self.__response = paging
        return

    @property
    def cursor(self) -> Cursor:
        return Cursor(self.__response['cursors'])

    def __repr__(self) -> str:
        return "Paging()"

    def __str__(self) -> str:
        return f"Paging({self.cursor})"


class BadgeUrl(ImageUrl):
    """
    class to hold a url for one badge
    """

    def __init__(self, badge_url: str):
        super().__init__(badge_url)
        return


class BadgeUrls(BaseModel):
    """
    class to hold data of a clan badge
    """

    def __init__(self, data: dict):
        super().__init__(data)
        self._main_attribute = self.medium
        return

    @property
    def small(self) -> BadgeUrl:
        return BadgeUrl(self._get_data('small'))

    @property
    def medium(self) -> BadgeUrl:
        return BadgeUrl(self._get_data('medium'))

    @property
    def large(self) -> BadgeUrl:
        return BadgeUrl(self._get_data('large'))


class Time:
    def __init__(self, year: int, month: int, day: int, hour: int, minute: int, second: int, microsecond: int):
        self._year = year
        self._month = month
        self._day = day
        self._hour = hour
        self._minute = minute
        self._second = second
        self._microsecond = microsecond
        return

    @property
    def year(self) -> int:
        return self._year

    @property
    def month(self) -> int:
        return self._month

    @property
    def day(self) -> int:
        return self._day

    @property
    def hour(self) -> int:
        return self._hour

    @property
    def minute(self) -> int:
        return self._minute

    @property
    def second(self) -> int:
        return self._second

    @property
    def microsecond(self) -> int:
        return self._microsecond

    @classmethod
    def from_str(cls, time: str) -> Self:
        """
        converts a string with the format yyyymmddThhmmss.000Z
        """

        if len(time) != 20:
            raise InvalidTimeString

        dt = datetime.strptime(time, "%Y%m%dT%H%M%S.%fZ")

        return cls(dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second, dt.microsecond)

    def __eq__(self, other) -> bool:
        if isinstance(other, Time):
            return self._year == other._year and self._month == other._month and self._day == other._day and \
                self._hour == other._hour and self._minute == other._minute and self._second == other._second
        if isinstance(other, (Time, datetime)):
            return self._year == other.year and self._month == other.month and self._day == other.day and \
                self._hour == other.hour and self._minute == other.minute and self._second == other.second
        return NotImplemented

    def __ne__(self, other):
        return not self == other

    def __lt__(self, other) -> bool:
        if isinstance(other, (Time, datetime)):
            if self._year < other.year:
                return True
            if self._year == other.year and self._month < other.month:
                return True
            if self._year == other.year and self._month == other.month and self._day < other.day:
                return True
            if self._year == other.year and self._month == other.month and self._day == other.day and self._hour < other.hour:
                return True
            if self._year == other.year and self._month == other.month and self._day == other.day and self._hour == other.hour \
                    and self._minute < other.minute:
                return True
            if self._year == other.year and self._month == other.month and self._day == other.day and self._hour == other.hour \
                    and self._minute == other.minute and self._second < other.second:
                return True
            if self._year == other.year and self._month == other.month and self._day == other.day and self._hour == other.hour \
                    and self._minute == other.minute and self._second == other.second and self._microsecond < other.microsecond:
                return True
            return False
        return NotImplemented

    def __le__(self, other):
        return self == other or self < other

    def __gt__(self, other):
        return not self <= other

    def __ge__(self, other):
        return not self < other

    def __str__(self) -> str:
        return f"Time({self._year}.{self._month}.{self._day}:{self._hour}.{self._minute}.{self._second}. {self._microsecond})"

    def __repr__(self) -> str:
        return f"Time(year={self._year}, month={self._month}, day={self._day}, hour={self._hour}, minute={self._minute}, " \
               f"second={self._second}, microsecond={self._microsecond})"

    def __add__(self, other) -> Self:
        if isinstance(other, (Time, datetime)):
            return Time(self._year + other.year, self._month + other.month, self._day + other.day,
                        self._hour + other.hour, self._minute + other.minute, self._second + other.second,
                        self._microsecond + other.microsecond)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, (Time, datetime)):
            return Time(self._year - other.year, self._month - other.month, self._day - other.day,
                        self._hour - other.hour, self._minute - other.minute, self._second - other.second,
                        self._microsecond - other.microsecond)
        return NotImplemented


class BaseClanMember(BaseModel):
    def __init__(self, data: dict):
        super().__init__(data)
        self._main_attribute = self.tag
        return

    @property
    def tag(self) -> str:
        return self._get_data('tag')

    @property
    def name(self) -> str:
        return self._get_data('name')


class BaseLeague(BaseModel):
    def __init__(self, data: dict):
        super().__init__(data)
        self._main_attribute = self.id
        return

    @property
    def id(self) -> int:
        return self._get_data('id')

    @property
    def name(self) -> int:
        return self._get_data('name')


class BaseClan(BaseModel):
    def __init__(self, data: dict | None):
        super().__init__(data)
        self._main_attribute = self.tag
        return

    @property
    def tag(self) -> str:
        return self._get_data('tag')

    @property
    def name(self) -> str:
        return self._get_data('name')

    @property
    def badge_urls(self) -> BadgeUrls:
        return BadgeUrls(self._get_data('badgeUrls'))

