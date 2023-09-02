from .abc import RequestModel
from ..models import GoldPassSeason


class GoldPassRequest(RequestModel, GoldPassSeason):
    def __init__(self):
        RequestModel.__init__(self, "goldpass/seasons/current")
        GoldPassSeason.__init__(self)
        return
