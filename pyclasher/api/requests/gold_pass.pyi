from .abc import RequestModel
from ..models import GoldPassSeason


class GoldPassRequest(RequestModel, GoldPassSeason):
    def __init__(self) -> None:
        ...
