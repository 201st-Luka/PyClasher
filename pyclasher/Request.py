"""
``Request`` class

This class is used in subclasses to make and execute requests to the ClashOfClans API.
"""

from asyncio import Future, get_running_loop

from .Client import Client
from .base import Model
from .base.IRequest import IRequest
from .exceptions import NoClient, MISSING
from .utils.RequestMode import RequestMode


class Request(IRequest, Model):
    """
    Class for creating requests to the ClashOfClans API

    Attributes:
        _request_id (int):
            the request id
        _url (str):
            the url of the request
        request_mode (RequestMode):
            request method
        _body (dict):
            additional data that is to be sent with the request
        _url_kwargs (dict):
            the url kwargs that are to replace in the url
        client (Client | int | str):
            the client or its client ID that is used to make the request
        _data (dict):
            the response data of the request
    """

    def __init__(
        self,
        raw_url: str,
        request_mode: RequestMode = RequestMode.GET,
        body: dict = None,
        kwargs: dict[str, str] = None,
        client: Client | int | str = None,
        **url_kwargs: str,
    ) -> None:
        """
        Args:
            raw_url (str):
                the url of the request
            request_mode (RequestMode):
                request method
            body (dict):
                additional data that is to be sent with the request
            kwargs (dict[str, str]):
                dict of kew word arguments that can be encoded in the API request
            client (Client | int | str):
                the client or its client ID that is used to make the request
            url_kwargs (str):
                the url kwargs that are to replace in raw_url
        """
        IRequest.__init__(self, raw_url, request_mode, body, kwargs, client, **url_kwargs)
        Model.__init__(self, MISSING)

    async def request(self, client: Client | int | str = None) -> "Request":
        """
        Executes a request and makes the call to the ClashOfClans API

        Args:
            client (Client | int | str):
                the client of its ID that is used to make the request

        Returns:
            Request:
                the request object itself

        Raises:
            NoClient:
                if the client is not found
            ClientIsNotRunning:
                if the client is not running
            InvalidClientId:
                if the client id is invalid
        """
        # check client
        if client is None:
            client = self.client
            if client is MISSING and client is None:
                raise NoClient

        client = Client.check_client(client)

        if get_running_loop() != client.event_loop:
            raise RuntimeError("Client and request must run on the same event loop")

        # create futures
        future, status, error = Future(), Future(), Future()

        client.logger.debug(f"Requesting {self._request_id}")

        # put request in queue
        await client.queue.put((future, self._make_request_url(), self.request_mode, self._body, status, error))

        # wait and get data, status and error
        self._data, req_status, req_error = await future, await status, await error

        # raise error if status is not 200
        if req_status != 200:
            raise req_error

        client.logger.debug(f"Request {self._request_id} done")

        return self
