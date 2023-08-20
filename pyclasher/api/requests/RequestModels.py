from asyncio import Future, get_running_loop
from typing import Any
from urllib.parse import quote, urlencode

from Exceptions import NoClient, ClientIsNotRunning, RequestNotDone, MISSING
from client import PyClasherClient, RequestMethods
from api.models import Paging

request_id = 0


class RequestModel:
    """
    class for requesting
    """

    _data = MISSING
    _main_attribute = None
    _url = None
    _url_kwargs = None
    _len = None

    def __init__(self, raw_url, kwargs=None, request_method=RequestMethods.REQUEST, **url_kwargs):
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

    def to_dict(self):
        if self._data is MISSING:
            raise RequestNotDone
        return self._data

    def __make_request_url(self):
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

    async def _async_request(self):
        """
        makes a request to the ClashOfClans API
        """
        if not self.client.is_running:
            raise ClientIsNotRunning

        future, status, error = Future(), Future(), Future()

        self.client.logger.debug(f"requesting {self._request_id}")

        await self.client.queue.put(future, self.__make_request_url(), self.request_method, None, status, error)

        self._data, req_status, req_error = await future, await status, await error

        if req_status != 200:
            raise req_error.value

        self.client.logger.debug(f"request {self._request_id} done")
        return self

    def __get_properties(self):
        return {name: prop.__get__(self) for name, prop in vars(self.__class__).items() if isinstance(prop, property)}

    def _get_data(self, item):
        if self._data is None:
            return None
        if self._data is MISSING:
            raise RequestNotDone
        if item in self._data:
            return self._data[item]
        else:
            return MISSING

    def request(self):
        try:
            get_running_loop()
        except RuntimeError:
            return self.client.loop.run_until_complete(self._async_request())
        else:
            return self._async_request()

    async def __aenter__(self):
        return await self._async_request()

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        return

    def __enter__(self):
        return self.request()

    def __exit__(self, exc_type, exc_val, exc_tb):
        return

    def __repr__(self):
        if self.__class__.__name__ == "RequestModel":
            return f"RequestModel(url={self._url}, url_kwargs={self._url_kwargs})"
        else:
            return f"{self.__class__.__name__}({', '.join(('='.join((key, str(value))) for key, value in self.__get_properties().items()))})"

    def __str__(self):
        if self.__class__.__name__ == "RequestModel":
            return f"RequestModel({self.__make_request_url()})"
        else:
            main_attr = ",".join(self._main_attribute) if isinstance(self._main_attribute, (list, tuple)) else self._main_attribute
            return f"{self.__class__.__name__}({main_attr})"


class IterRequestModel(RequestModel):
    _iter_rtype: Any = ...
    _list_rtype: Any = ...
    _len = None

    async def _async_request(self):
        await super()._async_request()
        self._len = len(self._get_data('items'))
        self._main_attribute = self._len
        return self

    @property
    def items(self):
        return self._list_rtype(self._get_data('items'))

    @property
    def paging(self):
        return Paging(self._get_data('paging'))

    def __getitem__(self, item):
        if self._data is MISSING:
            raise RequestNotDone
        if self._data is None:
            return None
        if isinstance(item, int):
            return self.items[item]
        if isinstance(item, slice):
            return (self.items[i] for i in range(*item.indices(len(self))))
        raise NotImplementedError

    def __iter__(self):
        self._iter = iter(self._get_data('items'))
        return self

    def __next__(self):
        return self._iter_rtype(next(self._iter))

    def __contains__(self, item):
        raise NotImplementedError

    def __len__(self):
        return self._len
