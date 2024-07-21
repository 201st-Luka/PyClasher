"""
``IterativeRequest`` class
"""

from asyncio import Future

from .Client import Client
from .base import ArrayModel
from .base.IRequest import IRequest
from .exceptions import MISSING, NoClient
from .utils.RequestMode import RequestMode


class IterativeRequest[T](IRequest, ArrayModel[T]):
    def __init__(
        self,
        raw_url: str,
        type_: type[T],
        request_mode: RequestMode = RequestMode.GET,
        body: dict = None,
        kwargs: dict[str, str | int] = None,
        client: Client | int | str = None,
        **url_kwargs: str,
    ) -> None:
        """
        Args:
            raw_url (str):
                the url of the request
            type_ (type[T]):
                Type of the items in the array
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
        ArrayModel.__init__(self, MISSING, type_)

    async def request(self, client: Client | int | str = None) -> "IterativeRequest[T]":
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
        if client is None:
            client = self.client
            if client is MISSING and client is None:
                raise NoClient

        client = Client.check_client(client)

        # create futures
        future, status, error = Future(), Future(), Future()

        client.logger.debug(f"Requesting {self._request_id}")

        # put request in queue
        await client.queue.put((future, self._make_request_url(), self.request_mode, self._body, status, error))

        # wait and get data, status and error
        self._items, req_status, req_error = await future, await status, await error

        # raise error if status is not 200
        if req_status != 200:
            raise req_error

        client.logger.debug(f"Request {self._request_id} done")

        return self
