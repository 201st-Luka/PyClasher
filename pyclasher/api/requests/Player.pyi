from typing import Coroutine, Any

from .RequestModels import RequestModel
from ..models import Player, VerifyTokenResponse


class PlayerRequest(RequestModel, Player):
    def __init__(self, player_tag: str) -> None:
        self.player_tag = player_tag
        ...

    async def _async_verify_token(self, player_token: str) -> VerifyTokenResponse:
        ...

    def verify_token(self, player_token: str) -> VerifyTokenResponse | Coroutine[Any, Any, VerifyTokenResponse]:
        ...
