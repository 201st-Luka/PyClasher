from .abc import RequestModel
from ..models import Player, VerifyTokenResponse


__all__ = (
    'PlayerRequest',
)


class PlayerRequest(RequestModel, Player):
    def __init__(self, player_tag: str) -> None:
        self.player_tag = player_tag
        ...

    async def verify_token(self, player_token: str) -> VerifyTokenResponse:
        ...
