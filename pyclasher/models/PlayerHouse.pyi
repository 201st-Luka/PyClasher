from .BaseModels import BaseModel, IterBaseModel
from .Enums import PlayerHouseElementType


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

    def __next__(self) -> PlayerHouseElement:
        ...


class PlayerHouse(BaseModel):
    @property
    def elements(self) -> PlayerHouseElementList:
        ...
