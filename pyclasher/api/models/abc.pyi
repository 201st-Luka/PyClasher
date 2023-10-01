"""
abstract base classes for the API models
"""


from typing import Any, Generator, Iterator

from ...exceptions import MISSING, Missing


__all__ = (
    'BaseModel',
    'IterBaseModel'
)


class BaseModel:
    """
    base model
    this model is a base for all other ClashOfClans API response models
    can be inherited from
    """

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
        protected method that returns a dict of the properties of a class (also works with inherited classes)
        or None or MISSING if the data is not defined

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

    :ivar   _len:              length of the iterative data
    :type   _len:              int
    :ivar   _data:             a list of dicts containing the data
    :type   _data:             list[dict] | None
    """

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

    def to_dict_list(self) -> list[dict] | None | MISSING:
        """
        method that returns the response as a list of dicts

        :return:    response as a list of dicts
        :rtype:     list[dict] | None | Missing
        """
        ...

    def __len__(self) -> int:
        ...

    def __getitem__(self, item: int | slice) -> MISSING | Generator | _iter_rtype:
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

