from abc import ABC
from typing import Any

from ...exceptions import RequestNotDone, MISSING


__all__ = (
    'BaseModel',
    'IterBaseModel'
)


class BaseModel(ABC):
    def __new__(cls, data=None):
        if data is MISSING:
            return MISSING
        return super().__new__(cls)

    def __init__(self, data=None):
        if data is not None:
            self._data = data
        return

    def to_dict(self):
        return self._data

    def _get_properties(self):
        if isinstance(self._data, dict):
            return {
                name: prop.__get__(self)
                for name, prop in vars(type(self)).items()
                if isinstance(prop, property)
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
        if self._data is MISSING:
            return f"{self.__class__.__name__}(RequestNotDone)"
        return f"{self.__class__.__name__}()"

    def __repr__(self):
        props = ', '.join(
            ('='.join((key, str(value)))
             for key, value in self._get_properties().items())
        )
        return f"{self.__class__.__name__}({props})"


class IterBaseModel(ABC):
    _iter_rtype: Any

    def __new__(cls, data):
        if data is MISSING:
            return MISSING
        return super().__new__(cls)

    def __init__(self, data):
        self._data = data
        self._len = len(self._data) if self._data is not None else None
        return

    def to_dict_list(self):
        return self._data

    def __len__(self):
        if self._len is None and self._data is not None:
            self._len = len(self._data)
        return self._len

    def __getitem__(self, item):
        if self._data is MISSING:
            raise RequestNotDone
        if self._data is None:
            return None
        if isinstance(item, int):
            return self._iter_rtype(self._data[item])
        if isinstance(item, slice):
            return (self._iter_rtype(self._data[i])
                    for i in range(*item.indices(len(self._data))))
        raise NotImplementedError(f"there is no implementation for type "
                                  f"{item.__class__.__name__} in "
                                  f"{self.__class__.__name__}.__getitem__()")

    def __iter__(self):
        self._iter = iter(self._data)
        return self

    def __next__(self):
        return self._iter_rtype(next(self._iter))

    def __contains__(self, item):
        if isinstance(item, (self._iter_rtype, str)):
            for item_ in self:
                if item_ == item:
                    return True
            return False
        return NotImplemented

    def __str__(self):
        return f"{self.__class__.__name__}()"

    def __repr__(self):
        return (f"{self.__class__.__name__}(len={self._len}, type="
                f"{self._iter_rtype.__name__}, {list(self)})")



