from json import dumps
from asyncio import run, Queue, sleep, Future, create_task, get_running_loop
from enum import Enum
from logging import Logger
from typing import Iterable, Self, Coroutine, Any
from urllib.parse import urlparse
from aiohttp import ClientSession, request

from .Exceptions import InvalidLoginData, InvalidType, LoginNotDone, ClientIsRunning, ClientIsNotRunning, \
    NoneToken
from .models.BaseModels import BaseModel
from .logger import PyClasherLogger
from .models import ApiExceptions


class RequestMethods(Enum):
    REQUEST = "get"
    POST = "post"


class Status(BaseModel):
    """
    class representing the status of the ClashOfClans API login
    """
    def __init__(self, data: dict) -> None:
        super().__init__(data)
        self._main_attribute = self.code
        return

    @property
    def code(self) -> int:
        return self._data['code']

    @property
    def message(self) -> str:
        return self._data['message']

    @property
    def detail(self):
        return self._data['detail']


class Auth(BaseModel):
    """
    class representing the authentication of the ClashOfClans API login
    """
    def __init__(self, data: dict) -> None:
        super().__init__(data)
        self._main_attribute = self.uid
        return

    @property
    def uid(self) -> str:
        return self._data['uid']

    @property
    def token(self) -> str:
        return self._data['token']

    @property
    def ua(self):
        return self._data['ua']

    @property
    def ip(self):
        return self._data['ip']


class Developer(BaseModel):
    """
    class representing the developer that logged in via the ClashOfClans login API
    """
    def __init__(self, data: dict) -> None:
        super().__init__(data)
        self._main_attribute = self.email
        return

    @property
    def id(self) -> str:
        return self._data['id']

    @property
    def name(self) -> str:
        return self._data['name']

    @property
    def game(self) -> str:
        return self._data['game']

    @property
    def email(self) -> str:
        return self._data['email']

    @property
    def tier(self) -> str:
        return self._data['tier']

    @property
    def allowed_scopes(self):
        return self._data['allowedScopes']

    @property
    def max_cidrs(self):
        return self._data['maxCidrs']

    @property
    def prev_login_ts(self) -> str:
        return self._data['prevLoginTs']

    @property
    def prev_login_ip(self) -> str:
        return self._data['prevLoginIp']

    @property
    def prev_login_ua(self) -> str:
        return self._data['prevLoginUa']


class Login:
    """
    class to log in via the ClashOfClans login API
    """

    login_url = "https://developer.clashofclans.com/api/login"
    __response: dict

    def __init__(self, email: str, password: str) -> None:
        self.email = email
        self.__password = password

        return

    @property
    def status(self) -> Status:
        if self.__response is None:
            raise LoginNotDone
        return Status(self.__response['status'])

    @property
    def session_expires_in_seconds(self) -> int:
        return self.__response['sessionExpiresInSeconds']

    @property
    def auth(self) -> Auth:
        return Auth(self.__response['auth'])

    @property
    def developer(self) -> Developer:
        return Developer(self.__response['developer'])

    @property
    def temporary_api_token(self) -> str:
        return self.__response['temporaryAPIToken']

    @property
    def swagger_url(self) -> str:
        return self.__response['swaggerUrl']

    async def __async_login(self):
        async with request("post", self.login_url, json={
            "email": self.email,
            "password": self.__password
        }) as response:
            if response.status == 200:
                self.__response = await response.json()
                return self
            else:
                raise InvalidLoginData

    def login(self) -> Self | Coroutine[Any, Any, Self]:
        try:
            get_running_loop()
        except RuntimeError:
            return run(self.__async_login())
        else:
            return self.__async_login()

    def __repr__(self) -> str:
        return f"Login(email={self.email}, password={'*' * len(self.__password)}, " \
               f"status={self.status}, session_expires_in_seconds={self.session_expires_in_seconds}, auth={self.auth}, " \
               f"developer={self.developer}, temporary_api_token={self.temporary_api_token}, swagger_url={self.swagger_url})"

    def __str__(self) -> str:
        return f"Login({self.email})"


class Consumer:
    def __init__(self, queue: Queue, token: str, requests_per_s: int, url: str):
        self.queue = queue
        self.header = {
            'Authorization': f'Bearer {token}'
        }
        self.r_p_s = requests_per_s
        self.wait = 1 / self.r_p_s
        self.url = url
        self.session = ClientSession(
            base_url=url,
            headers=self.header
        )
        return

    async def _request(self, future: Future, url: str, method: str, body: dict | None) -> None:
        async with self.session.request(method=method, url=url, data=None if body is None else dumps(body)) as response:
            response_json = await response.json()
            future.set_result(response_json if response.status == 200 else ApiExceptions.from_exception(response.status, response_json).value)
            return

    async def consume(self):
        while True:
            future, url, method, body = await self.queue.get()

            create_task(self._request(future, url, method, body))

            self.queue.task_done()

            await sleep(self.wait)

    async def close(self):
        await self.session.close()
        return


class PyClasherClient:
    """
    This is the class for the ClashOfClans API client
    """

    __instance: Self = None

    base_url: str = "https://api.clashofclans.com"
    endpoint: str = "/v1"
    queue: Queue
    requests_per_second = 5
    logger: PyClasherLogger = None
    initialised: bool = False
    __consumers: list[Consumer] = None
    __consume_tasks = None
    __temporary_session: bool = False
    __tokens: list[str] | None = None
    __client_running: bool = False

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(
        self,
        tokens: str | Iterable[str] = None,
        requests_per_second: int = None,
        logger: Logger = None,
        swagger_url: str = None
    ) -> None:
        """
        initialisation method for the client
        :param tokens:                  the Bearer tokens for the authentication of the ClashOfClans API
        :type tokens:                   str | list[str] | None
        :param requests_per_second:     This integer limits the number of requests done per second (per token).
                                        This value is important to bypass the rate limit of the ClashOfClans API.
                                        More tokens allow more requests per second because each token can do
                                        as many requests per second as specified.
                                        Defaults to None.
        :type requests_per_second:      int
        :param logger:                  logger for detailed logging
                                        Defaults to None
        :type logger:                   Logger
        :param swagger_url:             swagger url for requests
                                        Defaults to None
        :type swagger_url:              str
        :return:                        initialises the class
        :rtype:                         None
        """

        if not PyClasherClient.initialised:
            self.logger = PyClasherLogger(logger)
            self.logger.info("initialising pyclasher client")
            if tokens is not None:
                if isinstance(tokens, str):
                    self.__tokens = [tokens]
                elif isinstance(tokens, Iterable):
                    self.__tokens = list(tokens)
                else:
                    raise InvalidType(tokens, (str, Iterable[str]))

            if swagger_url is not None:
                parsed_url = urlparse(swagger_url)
                self.base_url = f"{parsed_url.scheme}://{parsed_url.netloc}"
                self.endpoint = parsed_url.path[:-1]

            self.requests_per_second = requests_per_second

            self.logger.debug("pyclasher client initialised")

            self.queue = Queue()

            PyClasherClient.initialised = True
        return

    @classmethod
    def from_login(cls, email: str, password: str, requests_per_second: int = 5, logger: Logger = None, login_count: int = 1):
        """
        login via the ClashOfClans login API to retrieve a temporary session (usually 1 hour)
        """

        async def from_async_login():
            logins = [await Login(email, password).login() for _ in range(login_count)]
            pc_logger = PyClasherLogger(logger)

            pc_logger.info("initialising pyclasher client via login")

            self = cls([login.temporary_api_token for login in logins], requests_per_second, swagger_url=logins[0].swagger_url)
            self.logger = pc_logger
            self.__temporary_session = True
            return self

        try:
            get_running_loop()
        except RuntimeError:
            return run(from_async_login())
        else:
            return from_async_login()

    @property
    def is_running(self) -> bool:
        return self.__client_running

    def start(self, tokens: str | Iterable[str] = None):
        """
        start the client
        :param tokens:                  the Bearer tokens for the authentication of the ClashOfClans API
        :type tokens:                   str | list[str] | None
        """
        if tokens is not None:
            if isinstance(tokens, str):
                self.__tokens = [tokens]
            elif isinstance(tokens, Iterable):
                self.__tokens = list(tokens)
            else:
                raise InvalidType(tokens, (str, Iterable[str]))

        if self.__tokens is None:
            raise NoneToken

        if self.__client_running or self.__consume_tasks is not None:
            self.logger.error("the client is already running")
            raise ClientIsRunning
        else:
            self.__client_running = True
        self.logger.info("starting pychlasher client")
        self.__consumers = [Consumer(self.queue, token, self.requests_per_second, self.base_url) for token in self.__tokens]
        self.__consume_tasks = [create_task(consumer.consume()) for consumer in self.__consumers]
        self.logger.debug("pyclasher client started")
        return self

    def close(self):
        """
        close the client
        """

        async def async_close():
            self.logger.info("closing pyclasher client")
            if not self.__client_running or self.__consume_tasks is None:
                self.logger.error("the client is not running")
                raise ClientIsNotRunning
            else:
                self.__client_running = False

            for task in self.__consume_tasks:
                task.cancel()
            for consumer in self.__consumers:
                await consumer.close()
            self.logger.debug("pyclasher client closed")
            return

        try:
            get_running_loop()
        except RuntimeError:
            return run(async_close())
        else:
            return async_close()

    def __enter__(self):
        return self.start()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()
        return

    async def __aenter__(self):
        return self.start()

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.close()
        return

    def __del__(self):
        PyClasherClient.__instance = None
        PyClasherClient.initialised = False

        if self.__client_running:
            self.close()
            self.logger.warning("The client was still running, closed now.")
        return
