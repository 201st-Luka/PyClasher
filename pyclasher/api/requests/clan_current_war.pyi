from .abc import RequestModel
from ..models import ClanWar, BaseClan


__all__ = (
    'ClanCurrentWarRequest',
)


class ClanCurrentWarRequest(RequestModel, ClanWar):
    clan_tag: str = None

    def __init__(self, clan_tag: str) -> None:
        self.clan_tag = clan_tag
        ...

    @classmethod
    async def from_base_clan(cls, base_clan: BaseClan) -> ClanCurrentWarRequest:
        async def async_from_base_clan() -> ClanCurrentWarRequest:
            ...

        ...
