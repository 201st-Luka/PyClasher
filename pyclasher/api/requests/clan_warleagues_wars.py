from .abc import RequestModel
from ..models import ClanWarLeagueGroup


class ClanWarleaguesWarsRequest(RequestModel, ClanWarLeagueGroup):
    """
    Retrieve information about individual clan war league war
    """

    def __init__(self, war_tag):
        self.war_tag = war_tag
        super().__init__("clanwarleagues/wars/{war_tag}",
                         war_tag=self.war_tag)
        return
