from .abc import RequestModel
from ..models import ClanWarLeagueGroup


class ClanWarleaguesWarsRequest(RequestModel, ClanWarLeagueGroup):
    """
    Retrieve information about individual clan war league war
    """

    def __init__(self, war_tag) -> None:
        self.war_tag: str = ...
        self._main_attribute: str = ...
        ...
