from .abc import IterRequestModel
from ..models import LabelList, Label


__all__ = (
    'ClanLabelsRequest',
)


class ClanLabelsRequest(IterRequestModel):
    _iter_rtype = Label
    _list_rtype = LabelList

    def __init__(self):
        super().__init__("labels/clans")
        return
