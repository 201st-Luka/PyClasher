from .abc import RequestModel
from ..models import ClanWar


class ClanWarleaguesWarsRequest(RequestModel, ClanWar):
    """
    Retrieve information about individual clan war league war
    """

    def __init__(self, war_tag) -> None:
        self.war_tag: str = ...
        ...
