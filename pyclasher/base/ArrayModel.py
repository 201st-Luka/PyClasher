"""
``ArrayIterator`` class
"""

from typing import Iterator

from ..exceptions import Missing


class ArrayModel[T]:
    """
    Class to iterate over an array of items

    Attributes:
        _items (list[dict]):
            Array of items
        _type (type[T]):
            Type of the items in the array
    """

    def __init__(self, data: dict[str, list[dict]] | Missing | None, type_: type[T]) -> None:
        """
        Args:
            data (dict[str, list[dict]]):
                Data dictionary of the API response
            type_ (type[T]):
                Type of the items in the array
        """
        self._items = data["items"]
        self._type = type_

    def __iter__(self) -> Iterator[T]:
        return (self._type(item) for item in self._items)

    def __getitem__(self, index: int) -> T:
        """
        Args:
            index (int):
                Index of the item in the array
        Returns:
            T:
                Item at the index
        """
        return self._type(self._items[index])

    def __len__(self) -> int:
        return len(self._items)

    def __str__(self) -> str:
        return f"{self.__class__.__name__}({len(self)} items of type {self._type})"

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__}([{', '.join((repr(item)) for item in self)}])>"
