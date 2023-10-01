from .abc import BaseModel, IterBaseModel
from .enums import PlayerHouseElementType


__all__ = (
    'PlayerHouse',
    'PlayerHouseElement',
    'PlayerHouseElementList',
)


class PlayerHouseElement(BaseModel):
    def __init__(self, data):
        super().__init__(data)
        return

    @property
    def id(self):
        return self._get_data('id')

    @property
    def type(self):
        return PlayerHouseElementType(self._get_data('type'))


class PlayerHouseElementList(IterBaseModel):
    _iter_rtype = PlayerHouseElement

    def __getitem__(self, item):
        return super().__getitem__(item)

    def __next__(self):
        return super().__next__()


class PlayerHouse(BaseModel):
    @property
    def elements(self):
        return PlayerHouseElementList(self._get_data('elements'))
