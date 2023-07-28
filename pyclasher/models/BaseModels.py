from datetime import datetime
from typing import Any

from ..Exceptions import RequestNotDone, InvalidTimeFormat, MISSING


class BaseModel:
    _main_attribute = None
    _data = MISSING

    def __new__(cls, data):
        if data is MISSING:
            return MISSING
        return super().__new__(cls)

    def __init__(self, data):
        if data is not None:
            self._data = data
        return

    def to_dict(self):
        return self._data

    def _get_properties(self):
        if isinstance(self._data, dict):
            return {
                name: prop.__get__(self) for name, prop in vars(type(self)).items() if isinstance(prop, property)
            }
        return self._data

    def _get_data(self, item):
        if self._data is None:
            return None
        if self._data is MISSING:
            raise RequestNotDone
        if item in self._data:
            return self._data[item]
        else:
            return MISSING

    def __str__(self):
        try:
            main_attr = ",".join((str(attr) for attr in self._main_attribute)) if isinstance(self._main_attribute, (list, tuple)) else \
                str(self._main_attribute) if self._main_attribute is not None else ""
        except RequestNotDone:
            main_attr = "RequestNotDone"
        return f"{self.__class__.__name__}({main_attr})"

    def __repr__(self):
        return f"{self.__class__.__name__}({', '.join(('='.join((key, str(value))) for key, value in self._get_properties().items()))})"


class IterBaseModel:
    _len = None
    _main_attribute = None
    _iter_rtype = Any

    def __init__(self, data):
        self._data = data
        if self._data is not None and self._data is not MISSING:
            self._len = len(self._data)
        self._main_attribute = self._len
        return

    def to_dict_list(self):
        return self._data

    def __len__(self):
        return self._len

    def __getitem__(self, item):
        if self._data is MISSING:
            raise RequestNotDone
        if self._data is None:
            return None
        if isinstance(item, int):
            return self._iter_rtype(self._data[item])
        if isinstance(item, slice):
            return (self._iter_rtype(self._data[i]) for i in range(*item.indices(len(self._data))))
        raise NotImplementedError

    def __iter__(self):
        self._iter = iter(self._data)
        return self

    def __next__(self):
        return self._iter_rtype(next(self._iter))

    def __contains__(self, item):
        if isinstance(item, (self._iter_rtype, str)):
            for s_item in self:
                if s_item == item:
                    return True
            return False
        return NotImplemented

    def __str__(self):
        return f"{self.__class__.__name__}({self._main_attribute})"

    def __repr__(self):
        return f"{self.__class__.__name__}(len={self._len}, type={self._iter_rtype.__name__})"


class ImageUrl:
    __url = None

    def __init__(self, url):
        self.__url = url
        return

    async def get_image(self):
        raise NotImplementedError

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
        self._main_attribute = self.small
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
        self.__response = before
        return

    @property
    def value(self):
        return self.__response

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
    def __init__(self, data):
        super().__init__(data)
        self._main_attribute = self.medium
        return

    @property
    def small(self):
        return BadgeUrl(self._get_data('small'))

    @property
    def medium(self):
        return BadgeUrl(self._get_data('medium'))

    @property
    def large(self):
        return BadgeUrl(self._get_data('large'))


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

        return cls(dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second, dt.microsecond)

    def __eq__(self, other):
        if isinstance(other, Time):
            return self._year == other._year and self._month == other._month and self._day == other._day and \
                self._hour == other._hour and self._minute == other._minute and self._second == other._second
        if isinstance(other, (Time, datetime)):
            return self._year == other.year and self._month == other.month and self._day == other.day and \
                self._hour == other.hour and self._minute == other.minute and self._second == other.second
        return NotImplemented

    def __ne__(self, other):
        return not self == other

    def __lt__(self, other):
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

    def __str__(self):
        return f"Time({self._year}.{self._month}.{self._day}:{self._hour}.{self._minute}.{self._second}.{self._microsecond})"

    def __repr__(self):
        return f"Time(year={self._year}, month={self._month}, day={self._day}, hour={self._hour}, minute={self._minute}, " \
               f"second={self._second}, microsecond={self._microsecond})"

    def __add__(self, other):
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
    def tag(self):
        return self._get_data('tag')

    @property
    def name(self):
        return self._get_data('name')


class BaseLeague(BaseModel):
    def __init__(self, data):
        super().__init__(data)
        self._main_attribute = self.id if data is not None else None
        return

    @property
    def id(self):
        return self._get_data('id')

    @property
    def name(self):
        return self._get_data('name')


class BaseClan(BaseModel):
    def __init__(self, data: dict | None):
        super().__init__(data)
        if data is not None:
            self._main_attribute = self.tag
        return

    @property
    def tag(self):
        return self._get_data('tag')

    @property
    def name(self):
        return self._get_data('name')

    @property
    def badge_urls(self):
        return BadgeUrls(self._get_data('badgeUrls'))
