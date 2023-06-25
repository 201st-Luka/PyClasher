from ..models import GoldPassSeason
from .RequestModels import RequestModel


class GoldPassRequest(RequestModel, GoldPassSeason):
    def __init__(self):
        super().__init__("goldpass/seasons/current")
        self._main_attribute = ""
        return
