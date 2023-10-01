from typing import Iterator

from .abc import BaseModel, IterBaseModel
from .enums import PlayerHouseElementType


__all__ = (
    'PlayerHouse',
    'PlayerHouseElement',
    'PlayerHouseElementList',
)


class PlayerHouseElement(BaseModel):
    @property
    def id(self) -> int:
        ...

    @property
    def type(self) -> PlayerHouseElementType:
        ...


class PlayerHouseElementList(IterBaseModel):
    _iter_rtype = PlayerHouseElement

    def __getitem__(self, item: int | str) -> PlayerHouseElement:
        ...

    def __iter__(self) -> Iterator[PlayerHouseElement]:
        ...

    def __next__(self) -> PlayerHouseElement:
        ...


class PlayerHouse(BaseModel):
    @property
    def elements(self) -> PlayerHouseElementList:
        ...
