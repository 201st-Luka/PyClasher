from .abc import RequestModel
from ..models import ClanWar


__all__ = (
    'ClanWarleaguesWarsRequest',
)


class ClanWarleaguesWarsRequest(RequestModel, ClanWar):
    """
    Retrieve information about individual clan war league war
    """

    def __init__(self, war_tag):
        self.war_tag = war_tag
        RequestModel.__init__(self,
                              "clanwarleagues/wars/{war_tag}",
                              war_tag=self.war_tag)
        ClanWar.__init__(self, None)
        return
