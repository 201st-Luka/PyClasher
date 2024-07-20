"""
``Request`` class

This class is used in subclasses to make and execute requests to the ClashOfClans API.
"""

from asyncio import Future
from urllib.parse import quote, urlencode

from ..client import Client
from ..exceptions import NoClient, ClientIsNotRunning, RequestNotDone, MISSING, InvalidClientId
from ..utils.RequestMethods import RequestMethods

request_id_counter = 0
"""The request id counter that is used and incremented for each request"""


class Request:
    """
    Class for creating requests to the ClashOfClans API

    Attributes:
        _request_id (int):
            the request id
        _url (str):
            the url of the request
        request_method (RequestMethods):
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

    def __init__(self,
                 raw_url: str,
                 request_method: RequestMethods = RequestMethods.GET,
                 body: dict = None,
                 kwargs: dict = None,
                 client: Client | int | str = None,
                 **url_kwargs) -> None:
        """
        Args:
            raw_url (str):
                the url of the request
            request_method (RequestMethods):
                request method
            body (dict):
                additional data that is to be sent with the request
            kwargs (dict):
                dict of kew word arguments that can be encoded in the API request
            client (Client | int | str):
                the client or its client ID that is used to make the request
            url_kwargs:
                the url kwargs that are to replace in raw_url
        """
        global request_id_counter

        self._request_id = request_id_counter
        """The request id"""
        request_id_counter += 1

        self._url = raw_url.format(**url_kwargs)
        """The url of the request"""
        self.request_method = request_method
        """The request method"""
        self._body = body
        """The additional data that is to be sent with the request"""
        self._url_kwargs = kwargs
        """The url kwargs that are to replace in the url"""
        self.client = client if isinstance(client, Client) else Client.get_instance(client)
        """The client that is used to make the request"""

        # initialise
        self._data: dict = MISSING
        """The response data of the request"""

        return

    def to_dict(self) -> dict:
        """
        Returns the response data of the request

        Returns:
            dict:
                the response data of the request
        """
        if self._data is MISSING:
            raise RequestNotDone
        return self._data

    def __make_request_url(self) -> str:
        """
        Private method that returns the request url

        Returns:
            str:
                full request url
        """
        request_url = "/".join((self.client.endpoint, quote(self._url)))
        if self._url_kwargs is not None:
            url_args = {
                key: value
                for key, value in self._url_kwargs.items()
                if value is not None
            }
            if url_args != {}:
                request_url = f"{request_url}?{urlencode(url_args)}"

        return request_url

    def __get_properties(self) -> dict:
        """
        Private method that returns the properties of the instance

        Returns:
            dict:
                dictionary of properties containing the names and values of the properties
        """
        return {
            name: prop.__get__(self)
            for name, prop in vars(self.__class__).items()
            if isinstance(prop, property)
        }

    def _get_data(self, item):
        """
        Private method that returns the value of the item in the data or raises exceptions and handles exceptional data

        Args:
            item:
                the key of the item that is to be returned from the data

        Returns:
            typings.Any:
                the value of the item in the data

        Raises:
            RequestNotDone:
                if the request is not done yet
        """
        if self._data is None:
            return None
        if self._data is MISSING:
            raise RequestNotDone
        if item in self._data:
            return self._data[item]
        else:
            return MISSING

    async def request(self, client: Client | int | str = None) -> 'Request':
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
        self.client = Client.get_instance(client)
        if self.client is None:
            raise NoClient
        if self.client is MISSING:
            raise InvalidClientId(f"Cannot find a client with the client_id {client}.")
        if not self.client.is_running:
            raise ClientIsNotRunning

        # create futures
        future, status, error = Future(), Future(), Future()

        self.client.logger.debug(f"Requesting {self._request_id}")

        # put request in queue
        await self.client.queue.put((
            future, self.__make_request_url(),
            self.request_method, self._body,
            status,
            error
        ))

        # wait and get data, status and error
        self._data, req_status, req_error = await future, await status, await error

        # raise error if status is not 200
        if req_status != 200:
            raise req_error

        self.client.logger.debug(f"Request {self._request_id} done")

        self.client = None
        return self

    async def __aenter__(self) -> 'Request':
        return await self.request()

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        return

    def __repr__(self):
        props = ', '.join(('='.join((key, str(value)))
                           for key, value in self.__get_properties().items())
                          )
        return f"{self.__class__.__name__}({props})"

    def __str__(self):
        return f"{self.__class__.__name__}()"
