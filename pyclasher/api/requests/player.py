from asyncio import Future, get_running_loop, run
from urllib.parse import quote

from .request_models import RequestModel
from ..models import Player, VerifyTokenRequest, VerifyTokenResponse
from ...client import RequestMethods
from ...exceptions import ClientIsNotRunning, ApiCode


class PlayerRequest(RequestModel, Player):
    """
    Get information about a single player by player tag. Player tags can be found either in game or by
    from clan member lists.
    """

    def __init__(self, player_tag):
        self.player_tag = player_tag
        super().__init__("players/{player_tag}", player_tag=self.player_tag)
        self._main_attribute = self.player_tag
        return

    async def _async_verify_token(self, player_token):
        self.client.logger.debug(f"posting {self._request_id}")

        if not self.client.is_running:
            raise ClientIsNotRunning

        body = VerifyTokenRequest(player_token).to_dict()
        url = "/".join((self.client.endpoint, quote(f"players/{self.player_tag}/verifytoken")))

        future = Future()

        await self.client.queue.put((future, url, RequestMethods.POST.value, body))

        data = await future

        if isinstance(data, ApiCode):
            raise data

        self.client.logger.debug(f"post {self._request_id} done")
        return VerifyTokenResponse(data)

    def verify_token(self, player_token):
        try:
            get_running_loop()
        except RuntimeError:
            return run(self._async_verify_token(player_token))
        else:
            return self._async_verify_token(player_token)
