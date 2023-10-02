from .abc import RequestModel
from ..models import Clan, BaseClan


__all__ = (
    'ClanRequest',
)


class ClanRequest(RequestModel, Clan):
    clan_tag: str = None

    def __init__(self, clan_tag: str) -> None:
        self.clan_tag = clan_tag
        ...

    @classmethod
    def from_base_clan(cls, base_clan: BaseClan) -> ClanRequest:
        async def async_from_base_clan() -> ClanRequest:
            ...

        ...
