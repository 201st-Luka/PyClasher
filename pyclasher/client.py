from asyncio import run, create_task, get_running_loop, new_event_loop
from typing import Iterable
from urllib.parse import urlparse

from .request_queue import PcConsumer, PcQueue
from .utils.login import Login
from .exceptions import (InvalidType, ClientIsRunning, ClientIsNotRunning,
                         NoneToken, MISSING)


class Client:
    __instance = None

    base_url = "https://api.clashofclans.com"
    endpoint = "/v1"
    requests_per_second = 5
    logger = MISSING
    initialised = False

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(
            self,
            tokens=None,
            requests_per_second=5,
            request_timeout=30,
            logger=MISSING,
            swagger_url=None
    ):
        if not Client.initialised:
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

            self.queue = PcQueue()
            self.request_timeout = request_timeout

            Client.initialised = True
            self.__client_running = False
            self.__temporary_session = False
            self.__consumers = None
            self.__consume_tasks = None

        return

    @classmethod
    async def from_login(cls, email, password, requests_per_second=5,
                         request_timeout=30, logger=MISSING, login_count=1):
        if logger is None:
            logger = MISSING

        logins = [
            await Login(email, password).login() for _ in range(login_count)
        ]

        logger.info("initialising pyclasher client via login")

        self = cls([login.temporary_api_token for login in logins],
                   requests_per_second,
                   request_timeout,
                   swagger_url=logins[0].swagger_url)
        self.logger = logger
        self.__temporary_session = True
        return self

    @property
    def is_running(self) -> bool:
        return self.__client_running

    async def start(self, tokens=None):
        if tokens is None:
            tokens = self.__tokens

            if tokens is None:
                raise NoneToken

        elif isinstance(tokens, str):
            tokens = [tokens]

        if not isinstance(tokens, Iterable):
            raise InvalidType(tokens, (str, Iterable[str]))

        if self.__client_running or self.__consume_tasks is not None:
            self.logger.error("the client is already running")
            raise ClientIsRunning

        self.__client_running = True
        self.logger.info("starting pychlasher client")

        self.__consumers = [
            PcConsumer(self.queue, token, self.requests_per_second,
                       self.request_timeout, self.base_url)
            for token in tokens
        ]
        self.__consume_tasks = [
            create_task(consumer.consume()) for consumer in self.__consumers
        ]
        self.logger.debug("pyclasher client started")

        return self

    async def close(self):
        self.logger.info("closing pyclasher client")
        if not self.__client_running:
            self.logger.error("the client is not running")
            raise ClientIsNotRunning
        else:
            self.__client_running = False

        for task in self.__consume_tasks:
            task.cancel()
        self.__consume_tasks = None
        for consumer in self.__consumers:
            await consumer.close()
        self.__consumers = None

        self.logger.debug("pyclasher client closed")
        return self

    async def __aenter__(self):
        return await self.start()

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.close()
        return

    def __del__(self):
        Client.__instance = None
        Client.initialised = False

        if self.__client_running:
            self.close()
            self.logger.warning("The client was still running, closed now.")

        return
