from .abc import RequestModel
from ..models import GoldPassSeason


__all__ = (
    'GoldPassRequest',
)


class GoldPassRequest(RequestModel, GoldPassSeason):
    def __init__(self) -> None:
        ...
