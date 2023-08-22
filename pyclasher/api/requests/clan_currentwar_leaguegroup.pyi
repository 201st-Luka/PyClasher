from .abc import RequestModel
from ..models import ClanWarLeagueGroup, BaseClan


class ClanCurrentwarLeaguegroupRequest(RequestModel, ClanWarLeagueGroup):
    clan_tag: str = None

    def __init__(self, clan_tag: str) -> None:
        self.clan_tag = clan_tag
        ...

    @classmethod
    def from_base_clan(cls, base_clan: BaseClan) -> ClanCurrentwarLeaguegroupRequest:
        async def async_from_base_clan() -> ClanCurrentwarLeaguegroupRequest:
            ...

        ...
