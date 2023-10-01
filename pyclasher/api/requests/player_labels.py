from .abc import IterRequestModel
from ..models import LabelList, Label


__all__ = (
    'PlayerLabelsRequest',
)


class PlayerLabelsRequest(IterRequestModel):
    _iter_rtype = Label
    _list_rtype = LabelList

    def __init__(self):
        super().__init__("labels/players")
        return
