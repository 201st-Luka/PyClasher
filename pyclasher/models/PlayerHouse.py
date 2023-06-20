from .BaseModels import BaseModel, IterBaseModel
from .Enums import PlayerHouseElementType


class PlayerHouseElement(BaseModel):
    def __init__(self, data: dict):
        super().__init__(data)
        self._main_attribute = self.id
        return

    @property
    def id(self) -> int:
        return self._get_data('id')

    @property
    def type(self) -> PlayerHouseElementType:
        return PlayerHouseElementType(self._get_data('type'))


class PlayerHouseElementList(IterBaseModel):
    _iter_rtype = PlayerHouseElement

    def __getitem__(self, item: int | str) -> _iter_rtype:
        return super().__getitem__(item)

    def __next__(self) -> _iter_rtype:
        return super().__next__()


class PlayerHouse(BaseModel):
    @property
    def elements(self) -> PlayerHouseElementList:
        return PlayerHouseElementList(self._get_data('elements'))


