"""
``ArrayIterator`` class
"""

from typing import Iterator

from ..exceptions import Missing, RequestNotDone


class ArrayModel[T]:
    """
    Class to iterate over an array of items

    Attributes:
        _items (list[dict | str | int | float | bool]):
            Array of items
        _type (type[T]):
            Type of the items in the array
    """

    def __init__(self, items: list[dict | str | int | float | bool] | Missing | None, type_: type[T]) -> None:
        """
        Args:
            items (list[dict]):
                Data dictionary of the API response
            type_ (type[T]):
                Type of the items in the array
        """
        self._items = items
        self._type = type_

    def _get_items(self) -> list[T]:
        """
        Check if the items are present
        """
        if self._items is Missing:
            raise RequestNotDone
        if self._items is None:
            return []
        return self._items

    def __iter__(self) -> Iterator[T]:
        return (self._type(item) for item in self._get_items())

    def __getitem__(self, index: int) -> T:
        """
        Args:
            index (int):
                Index of the item in the array
        Returns:
            T:
                Item at the index
        """
        return self._type(self._get_items()[index])

    def __len__(self) -> int:
        return len(self._get_items())

    def __str__(self) -> str:
        if self._items is Missing:
            return f"{self.__class__.__name__}(Request not done)"
        if self._items is None:
            return f"{self.__class__.__name__}(No items of type {self._type})"
        return f"{self.__class__.__name__}({len(self)} items of type {self._type})"

    def __repr__(self) -> str:
        if self._items is Missing:
            return f"<{self.__class__.__name__}(Request not done)>"
        if self._items is None:
            return f"<{self.__class__.__name__}(No items of type {self._type})>"
        return f"<{self.__class__.__name__}([{', '.join((repr(item)) for item in self)}])>"
