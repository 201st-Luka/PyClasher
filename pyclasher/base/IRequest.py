"""
``IRequest`` class

This class is used to create the request subclasses.
"""

from abc import ABC, abstractmethod
from urllib.parse import quote, urlencode

from ..Client import Client
from ..utils.RequestMode import RequestMode


class IRequest(ABC):
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
        _request_id_counter (int):
            the request id counter that is used and incremented for each request
    """

    _request_id_counter = 0
    """The request id counter that is used and incremented for each request"""

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
        self._request_id = IRequest._request_id_counter
        """The request id"""
        IRequest._request_id_counter += 1

        self._url = raw_url.format(**url_kwargs)
        """The url of the request"""
        self.request_mode = request_mode
        """The request method"""
        self._body = body
        """The additional data that is to be sent with the request"""
        self._url_kwargs = kwargs
        """The url kwargs that are to replace in the url"""
        self.client = client if isinstance(client, Client) else Client.get_instance(client)
        """The client that is used to make the request"""

    def _make_request_url(self) -> str:
        """
        Private method that returns the request url

        Returns:
            str:
                full request url
        """
        request_url = "".join((self.client.endpoint, quote(self._url)))
        if self._url_kwargs is not None:
            url_args = {key: value for key, value in self._url_kwargs.items() if value is not None}
            if url_args != {}:
                request_url = f"{request_url}?{urlencode(url_args)}"

        return request_url

    @abstractmethod
    async def request(self, client: Client | int | str = None) -> "IRequest":
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
        ...

    async def __aenter__(self) -> "IRequest":
        return await self.request()

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        return
