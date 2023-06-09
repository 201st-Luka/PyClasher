from asyncio import run, Queue, sleep, create_task, get_running_loop
from enum import Enum
from json import dumps
from typing import Iterable
from urllib.parse import urlparse

from aiohttp import ClientSession, request

from .Exceptions import InvalidLoginData, InvalidType, LoginNotDone, ClientIsRunning, ClientIsNotRunning, \
    NoneToken, MISSING
from .models import ApiCodes
from .models.BaseModels import BaseModel


class RequestMethods(Enum):
    REQUEST = "get"
    POST = "post"


class Status(BaseModel):
    """
    class representing the status of the ClashOfClans API login
    """

    def __init__(self, data):
        super().__init__(data)
        self._main_attribute = self.code
        return

    @property
    def code(self):
        return self._get_data('code')

    @property
    def message(self):
        return self._get_data('message')

    @property
    def detail(self):
        return self._get_data('detail')


class Auth(BaseModel):
    def __init__(self, data):
        super().__init__(data)
        self._main_attribute = self.uid
        return

    @property
    def uid(self):
        return self._get_data('uid')

    @property
    def token(self):
        return self._get_data('token')

    @property
    def ua(self):
        return self._get_data('ua')

    @property
    def ip(self):
        return self._get_data('ip')


class Developer(BaseModel):
    def __init__(self, data):
        super().__init__(data)
        self._main_attribute = self.email
        return

    @property
    def id(self):
        return self._get_data('id')

    @property
    def name(self):
        return self._get_data('name')

    @property
    def game(self):
        return self._get_data('game')

    @property
    def email(self):
        return self._get_data('email')

    @property
    def tier(self):
        return self._get_data('tier')

    @property
    def allowed_scopes(self):
        return self._get_data('allowedScopes')

    @property
    def max_cidrs(self):
        return self._get_data('maxCidrs')

    @property
    def prev_login_ts(self):
        return self._get_data('prevLoginTs')

    @property
    def prev_login_ip(self):
        return self._get_data('prevLoginIp')

    @property
    def prev_login_ua(self):
        return self._get_data('prevLoginUa')


class Login:
    login_url = "https://developer.clashofclans.com/api/login"
    __response = None

    def __init__(self, email, password):
        self.email = email
        self.__password = password

        return

    @property
    def status(self):
        if self.__response is None:
            raise LoginNotDone
        return Status(self.__response['status'])

    @property
    def session_expires_in_seconds(self):
        return self.__response['sessionExpiresInSeconds']

    @property
    def auth(self):
        return Auth(self.__response['auth'])

    @property
    def developer(self):
        return Developer(self.__response['developer'])

    @property
    def temporary_api_token(self):
        return self.__response['temporaryAPIToken']

    @property
    def swagger_url(self):
        return self.__response['swaggerUrl']

    def login(self):
        async def async_login():
            async with request("post", self.login_url, json={
                "email": self.email,
                "password": self.__password
            }) as response:
                if response.status == 200:
                    self.__response = await response.json()
                    return self
                else:
                    raise InvalidLoginData

        try:
            get_running_loop()
        except RuntimeError:
            return run(async_login())
        else:
            return async_login()

    def __repr__(self):
        return f"Login(email={self.email}, password={'*' * len(self.__password)}, " \
               f"status={self.status}, session_expires_in_seconds={self.session_expires_in_seconds}, auth={self.auth}, " \
               f"developer={self.developer}, temporary_api_token={self.temporary_api_token}, swagger_url={self.swagger_url})"

    def __str__(self):
        return f"Login({self.email})"


class Consumer:
    def __init__(self, queue, token, requests_per_s, url):
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

    async def _request(self, future, url, method, body):
        async with self.session.request(method=method, url=url, data=None if body is None else dumps(body)) as response:
            response_json = await response.json()
            future.set_result(response_json if response.status == 200 else ApiCodes.from_exception(response.status, response_json).value)
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
    __instance = None

    base_url = "https://api.clashofclans.com"
    endpoint = "/v1"
    queue = None
    requests_per_second = 5
    logger = MISSING
    initialised = False
    __consumers = None
    __consume_tasks = None
    __temporary_session = False
    __tokens = None
    __client_running = False

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(
            self,
            tokens=None,
            requests_per_second=None,
            logger=MISSING,
            swagger_url=None
    ):
        if not PyClasherClient.initialised:
            if logger is None:
                logger = MISSING
            self.logger = logger
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
    def from_login(cls, email, password, requests_per_second=5, logger=MISSING, login_count=1):
        if logger is None:
            logger = MISSING

        async def from_async_login():
            logins = [await Login(email, password).login() for _ in range(login_count)]

            logger.info("initialising pyclasher client via login")

            self = cls([login.temporary_api_token for login in logins], requests_per_second, swagger_url=logins[0].swagger_url)
            self.logger = logger
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

    def start(self, tokens=None):
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
            return self

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
