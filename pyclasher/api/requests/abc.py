from asyncio import Future
from typing import Any
from urllib.parse import quote, urlencode

from ..models import Paging
from ...client import Client
from ...exceptions import (NoClient, ClientIsNotRunning, RequestNotDone,
                           MISSING, InvalidClientId)
from ...utils.request_methods import RequestMethods


__all__ = (
    'RequestModel',
    'IterRequestModel',
)


request_id = 0


class RequestModel:
    """
    class for requesting
    """

    _data = MISSING
    _url = None
    _url_kwargs = None
    _len = None

    def __init__(self,
                 raw_url,
                 kwargs=None,
                 request_method=RequestMethods.REQUEST,
                 **url_kwargs):
        """
        sets up all parameters for a request
        :param raw_url:         the url of the request
        :param kwargs:          dict of kew word arguments that can be encoded in the API request
        :param request_method:  request method
        :param url_kwargs:      the url kwargs that are to replace in raw_url
        """

        if Client.initialized():
            global request_id

            self._request_id = request_id
            self.client = None

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

    def __get_properties(self):
        return {
            name: prop.__get__(self)
            for name, prop in vars(self.__class__).items()
            if isinstance(prop, property)
        }

    def _get_data(self, item):
        if self._data is None:
            return None
        if self._data is MISSING:
            raise RequestNotDone
        if item in self._data:
            return self._data[item]
        else:
            return MISSING

    async def request(self, client_id=None):
        """
        makes a request to the ClashOfClans API
        """
        self.client = Client.get_instance(client_id)
        if self.client is None:
            raise NoClient
        if self.client is MISSING:
            raise InvalidClientId(f"Cannot find a client with the client_id "
                                  f"{client_id}.")

        if not self.client.is_running:
            raise ClientIsNotRunning

        future, status, error = Future(), Future(), Future()

        self.client.logger.debug(f"requesting {self._request_id}")

        await self.client.queue.put(
            future, self.__make_request_url(),
            self.request_method, None,
            status,
            error
        )

        self._data, req_status, req_error = (await future,
                                             await status,
                                             await error)

        if req_status != 200:
            raise req_error

        self.client.logger.debug(f"request {self._request_id} done")

        self.client = None
        return self

    async def __aenter__(self):
        return await self.request()

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        return

    def __repr__(self):
        props = ', '.join((
            '='.join((key, str(value)))
            for key, value in self.__get_properties().items())
        )
        return f"{self.__class__.__name__}({props})"

    def __str__(self):
        return f"{self.__class__.__name__}()"


class IterRequestModel(RequestModel):
    _iter_rtype: Any = ...
    _list_rtype: Any = ...

    def __init__(self,
                 raw_url,
                 kwargs=None,
                 request_method=RequestMethods.REQUEST,
                 **url_kwargs):
        super().__init__(raw_url,
                         kwargs=kwargs,
                         request_method=request_method,
                         **url_kwargs)
        return

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
        try:
            return len(self._get_data('items'))
        except RequestNotDone:
            return None
