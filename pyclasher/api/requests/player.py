from asyncio import Future
from urllib.parse import quote

from .abc import RequestModel
from ..models import Player, VerifyTokenRequest, VerifyTokenResponse
from ...client import Client
from ...exceptions import ClientIsNotRunning
from ...utils.request_methods import RequestMethods


__all__ = (
    'PlayerRequest',
)


class PlayerRequest(RequestModel, Player):
    """
    Get information about a single player by player tag. Player tags can be
    found either in game or from clan member lists.
    """

    def __init__(self, player_tag):
        self.player_tag = player_tag
        super().__init__("players/{player_tag}", player_tag=self.player_tag)
        return

    async def verify_token(self, player_token):
        self.client = Client.get_instance()

        if not self.client.is_running:
            raise ClientIsNotRunning

        body = VerifyTokenRequest(player_token).to_dict()
        url = "/".join((self.client.endpoint,
                        quote(f"players/{self.player_tag}/verifytoken")))

        future, status, error = Future(), Future(), Future()

        self.client.logger.debug(f"posting {self._request_id}")

        await self.client.queue.put(future,
                                    url,
                                    RequestMethods.POST.value,
                                    body,
                                    status,
                                    error)

        data, req_status, req_error = (await future,
                                       await status,
                                       await error)

        if req_status != 200:
            raise req_error.value

        self.client.logger.debug(f"post {self._request_id} done")
        return VerifyTokenResponse(data)
