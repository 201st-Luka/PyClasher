from .abc import RequestModel
from ..models import ClanWarLeagueGroup, BaseClan


__all__ = (
    'ClanCurrentwarLeaguegroupRequest',
)


class ClanCurrentwarLeaguegroupRequest(RequestModel, ClanWarLeagueGroup):
    clan_tag: str = None

    def __init__(self, clan_tag: str) -> None:
        self.clan_tag = clan_tag
        ...

    @classmethod
    async def from_base_clan(cls, base_clan: BaseClan) -> ClanCurrentwarLeaguegroupRequest:
        ...
