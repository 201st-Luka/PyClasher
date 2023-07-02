from asyncio import run, Future, get_running_loop
from typing import Any, Self, Coroutine
from urllib.parse import quote, urlencode

from ..Exceptions import NoClient, ClientIsNotRunning, RequestNotDone, ApiException, MISSING, Missing
from ..models import Paging
from ..client import PyClasherClient, RequestMethods


request_id: int = 0


class RequestModel:
    """
    class for requesting
    """

    _data: dict = MISSING
    _main_attribute: Any = None
    _url: str = None
    _url_kwargs: dict | None = None
    _len: int = None

    def __init__(self, raw_url: str, kwargs: dict = None, request_method: RequestMethods = RequestMethods.REQUEST, **url_kwargs) -> None:
        """
        sets up all parameters for a request
        :param raw_url:         the url of the request
        :param kwargs:          dict of kew word arguments that can be encoded in the API request
        :param request_method:  request method
        :param url_kwargs:      the url kwargs that are to replace in raw_url
        """

        if PyClasherClient.initialised:
            global request_id

            self._request_id = request_id
            self.client = PyClasherClient()
            self.client.logger.info(f"request {self._request_id} initialised")

            self._url = raw_url.format(**url_kwargs)
            self.request_method = request_method
            self._url_kwargs = kwargs

            request_id += 1
            return
        raise NoClient

    def to_dict(self) -> dict | Missing | None:
        if self._data is MISSING:
            raise RequestNotDone
        return self._data

    def __make_request_url(self) -> str:
        """
        method that returns the request url
        :return request_url:    full request url
        :rtype:                 str
        """

        self.client.logger.debug(f"making request url for request {self._request_id}")

        request_url = "/".join((self.client.endpoint, quote(self._url)))
        if self._url_kwargs is not None:
            url_args = {key: value for key, value in self._url_kwargs.items() if value is not None}
            if url_args != {}:
                request_url = f"{request_url}?{urlencode(url_args)}"

        self.client.logger.debug(f"url for request {self._request_id} is {request_url}")
        return request_url

    async def _async_request(self) -> Self:
        """
        makes a request with the ClashOfClans API
        """

        self.client.logger.debug(f"requesting {self._request_id}")

        if not self.client.is_running:
            raise ClientIsNotRunning

        future = Future()

        await self.client.queue.put((future, self.__make_request_url(), self.request_method.value, None))

        self._data = await future

        if isinstance(self._data, ApiException):
            raise self._data

        self.client.logger.debug(f"request {self._request_id} done")
        return self

    def __get_properties(self) -> dict:
        return {name: prop.__get__(self) for name, prop in vars(self.__class__).items() if isinstance(prop, property)}

    @property
    def _response(self) -> dict:
        if self._data is None:
            raise RequestNotDone
        return self._data

    @_response.setter
    def _response(self, data: dict):
        self._data = data

    def request(self) -> Self | Coroutine[Any, Any, Self]:
        try:
            get_running_loop()
        except RuntimeError:
            return run(self._async_request())
        else:
            return self._async_request()

    async def __aenter__(self):
        return await self._async_request()

    async def __aexit__(self, exc_type, exc_val, exc_tb) -> None:
        return

    def __enter__(self):
        return self.request()

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        return

    def __repr__(self) -> str:
        if self.__class__.__name__ == "RequestModel":
            return f"RequestModel(url={self._url}, url_kwargs={self._url_kwargs})"
        else:
            return f"{self.__class__.__name__}({', '.join(('='.join((key, str(value))) for key, value in self.__get_properties().items()))})"

    def __str__(self) -> str:
        if self.__class__.__name__ == "RequestModel":
            return f"RequestModel({self.__make_request_url()})"
        else:
            main_attr = ",".join(self._main_attribute) if isinstance(self._main_attribute, (list, tuple)) else self._main_attribute
            return f"{self.__class__.__name__}({main_attr})"


class IterRequestModel(RequestModel):
    _iter_rtype: Any = ...
    _list_rtype: Any = ...
    _len = None

    async def _async_request(self) -> Self:
        await super()._async_request()
        self._len = len(self._response['items'])
        return self

    @property
    def items(self) -> _list_rtype:
        return self._list_rtype(self._response['items'])

    @property
    def paging(self) -> Paging:
        return Paging(self._response['paging'])

    def __getitem__(self, item: int) -> _iter_rtype:
        return self._iter_rtype(self._response['items'][item])

    def __iter__(self) -> Self:
        self._iter = iter(self._response['items'])
        return self

    def __next__(self) -> _iter_rtype:
        return self._iter_rtype(next(self._iter))

    def __contains__(self, item: _iter_rtype) -> bool:
        raise NotImplementedError

    def __len__(self) -> int:
        return self._len
