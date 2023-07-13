from .RequestModels import IterRequestModel
from ..models import LabelList, Label


class PlayerLabelsRequest(IterRequestModel):
    _iter_rtype = Label
    _list_rtype = LabelList

    async def _async_request(self) -> PlayerLabelsRequest:
        ...

    @property
    def items(self) -> _list_rtype:
        ...

    def __getitem__(self, item: int) -> _iter_rtype:
        ...

    def __next__(self) -> _iter_rtype:
        ...
