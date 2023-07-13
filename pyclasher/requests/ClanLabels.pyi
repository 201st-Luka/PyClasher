from .RequestModels import IterRequestModel
from ..models import LabelList, Label


class ClanLabelsRequest(IterRequestModel):
    _iter_rtype = Label
    _list_rtype = LabelList

    @property
    def items(self) -> _list_rtype:
        ...

    def __getitem__(self, item: int) -> _iter_rtype:
        ...

    def __next__(self) -> _iter_rtype:
        ...
