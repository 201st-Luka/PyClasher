from .RequestModels import IterRequestModel
from api.models import LabelList, Label


class ClanLabelsRequest(IterRequestModel):
    _iter_rtype = Label
    _list_rtype = LabelList

    def __init__(self):
        super().__init__("labels/clans")
        self._main_attribute = ""
        return
