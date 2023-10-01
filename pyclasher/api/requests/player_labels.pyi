from typing import Iterator

from .abc import IterRequestModel
from ..models import LabelList, Label


__all__ = (
    'PlayerLabelsRequest',
)


class PlayerLabelsRequest(IterRequestModel):
    _iter_rtype = Label
    _list_rtype = LabelList

    def __init__(self) -> None:
        ...

    async def _async_request(self) -> PlayerLabelsRequest:
        ...

    @property
    def items(self) -> _list_rtype:
        ...

    def __getitem__(self, item: int) -> _iter_rtype:
        ...

    def __iter__(self) -> Iterator[_iter_rtype]:
        ...

    def __next__(self) -> _iter_rtype:
        ...
