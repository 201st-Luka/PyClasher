from typing import Self

from ..models import LabelList, Label
from .RequestModels import IterRequestModel


class ClanLabelsRequest(IterRequestModel):
    _iter_rtype = Label
    _list_rtype = LabelList

    def __init__(self):
        super().__init__("labels/clans")
        self._main_attribute = ""
        return

    async def _async_request(self) -> Self:
        await super()._async_request()
        self._main_attribute = self._len
        return self

    @property
    def items(self) -> _list_rtype:
        return super().items

    def __getitem__(self, item: int) -> _iter_rtype:
        return super().__getitem__(item)

    def __next__(self) -> _iter_rtype:
        return super().__next__()
