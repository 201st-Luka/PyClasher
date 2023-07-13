from .RequestModels import RequestModel
from ..models import GoldPassSeason


class GoldPassRequest(RequestModel, GoldPassSeason):
    def __init__(self):
        super().__init__("goldpass/seasons/current")
        self._main_attribute = ""
        return
