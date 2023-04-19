import asyncio
from collections.abc import Iterable
from urllib.parse import quote, urlencode

from aiohttp import ClientSession
from time import perf_counter

from clashofclansApi.Exceptions import ClientError, NoneToken, NoneArgument


class Interface:
    """
    class that serves as an interface for the ClashOfClans API
    """

    base_url: str = "https://api.clashofclans.com"
    session: ClientSession = None
    tasks: list = []
    tokens: str | Iterable[str] = None
    __token_index: int = 0
    __last_request: float = None
    __requests_per_second = 1

    def __init__(self, requests_per_second: int = None) -> None:
        if self.tokens is None:
            raise NoneToken
        elif isinstance(self.tokens, str):
            self.tokens = [self.tokens]
        self.__last_request = perf_counter()
        if requests_per_second is not None:
            self.__requests_per_second = requests_per_second
        return

    async def __aenter__(self):
        self.start()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb) -> None:
        await self.close()
        return

    def start(self) -> None:
        self.session = ClientSession(
            base_url=self.base_url
        )
        return

    async def close(self) -> None:
        await self.session.close()
        return

    async def request_get(self, url_extension: str, **values) -> dict:
        async with self.session.get(
            url="".join((url_extension, values))
        ) as response:
            return await response.json()

    @property
    async def header(self) -> dict:
        now = perf_counter()
        time_delta = now - self.__last_request
        time_tolerance = 1 / (self.__requests_per_second * len(self.tokens))
        if time_delta < time_tolerance:
            await asyncio.sleep(time_tolerance - time_delta)
        self.__token_index = (self.__token_index + 1) % len(self.tokens)
        self.__last_request = perf_counter()
        return {
                'Authorization': f'Bearer {self.tokens[self.__token_index]}'
            }

    def __repr__(self) -> str:
        return f"Interface({self.tokens})"

    def __str__(self) -> str:
        return f"Interface(base_url={self.base_url}, session={self.session}, tasks={self.tasks}, tokens={self.tokens})"


class RequestModel:
    """
    class for requesting
    """

    _response: dict = None
    _url_path: str | tuple[str, str] = None
    _url_args: dict = None
    api_interface: Interface = None

    def __init__(self, url_path: str | tuple[str, str], request_args: str | tuple[str, str] | None, **kwargs) -> None:
        """
        sets up all parameters for a request
        :param url_path: (str | tuple[str, str]) path for the API request (these can be splitted up in 2 parts if the request args have to be between those 2 parts
        :param request_args: (str | tuple[str, str]) request args for the API request (these can be splitted in 2 parts ig the there are 2 arguments to pass in the request
        :param kwargs: kew word arguments that can be encoded in the API request
        """
        self._url_path = url_path
        self._request_args = request_args
        self._url_args = kwargs
        return

    def __make_request_url(self) -> str:
        """
        method that returns the request url
        :return request_url: (str) full request url
        """
        if self._url_path is None or (self._request_args is None and self._url_args is None):
            raise NoneArgument
        if isinstance(self._url_path, tuple):
            if isinstance(self._request_args, tuple):
                request_url = "/".join((self._url_path[0], quote(self._request_args[0]), self._url_path[1], quote(self._request_args[1])))
            else:
                request_url = "/".join((self._url_path[0], quote(self._request_args), self._url_path[1]))
        else:
            request_url = "/".join((self._url_path, quote(self._request_args)))
        if self._url_args is not None:
            url_args = {key: value for key, value in self._url_args.items() if value is not None}
            return f"{request_url}?{urlencode(url_args)}"
        return request_url

    async def request(self) -> None:
        """
        makes a request with the ClashOfClans API
        :return:
        """
        async with self.api_interface.session.get(
            url=self.__make_request_url(),
            headers=await self.api_interface.header
        ) as response:
            response_json = await response.json()
            if 'reason' in response_json:
                raise ClientError(response, response_json)
            self._response = response_json
            return

    async def __aenter__(self):
        await self.request()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb) -> None:
        return

    def __repr__(self) -> str:
        return f"RequestModel()"

    def __str__(self) -> str:
        return f"RequestModel(url_path={self._url_path}, request_args={self._request_args}, url_args={self._url_args})"
