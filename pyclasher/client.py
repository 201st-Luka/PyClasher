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
    queue = None
    requests_per_second = 5
    logger = MISSING
    initialised = False
    __loop = MISSING
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
            self.__loop = new_event_loop()
            self.request_timeout = request_timeout

            Client.initialised = True
        return

    @classmethod
    def from_login(cls, email, password, requests_per_second=5, request_timeout=30, logger=MISSING, login_count=1):
        if logger is None:
            logger = MISSING

        async def from_async_login():
            logins = [await Login(email, password).login() for _ in range(login_count)]

            logger.info("initialising pyclasher client via login")

            self = cls([login.temporary_api_token for login in logins],
                       requests_per_second,
                       request_timeout,
                       swagger_url=logins[0].swagger_url)
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
        async def async_consumer_start(tokens_):
            self.__consumers = [PcConsumer(self.queue, token, self.requests_per_second, self.request_timeout, self.base_url) for token in tokens_]
            self.__consume_tasks = [create_task(consumer.consume()) for consumer in self.__consumers]
            self.logger.debug("pyclasher client started")
            return self

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

        try:
            get_running_loop()
        except RuntimeError:
            return self.__loop.run_until_complete(async_consumer_start(tokens))
        else:
            self.__consumers = [
                PcConsumer(
                    self.queue, token, self.requests_per_second, self.request_timeout, self.base_url)
                for token in tokens
            ]
            self.__consume_tasks = [create_task(consumer.consume()) for consumer in self.__consumers]
            self.logger.debug("pyclasher client started")
            return self

    def close(self):
        async def async_close():
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

        try:
            get_running_loop()
        except RuntimeError:
            return self.__loop.run_until_complete(async_close())
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
        Client.__instance = None
        Client.initialised = False

        if self.__client_running:
            self.close()
            self.logger.warning("The client was still running, closed now.")

        self.__loop.stop()
        self.__loop.close()

        return

    @property
    def loop(self):
        return self.__loop

    def reset_client(self, reset_queue=True, reset_loop=True, reset_tokens=True):
        if not self.is_running:
            if reset_queue:
                del self.queue
                self.queue = PcQueue()

            if reset_loop:
                self.__loop.stop()
                self.__loop.close()
                del self.__loop
                self.__loop = new_event_loop()

            if reset_tokens:
                self.__tokens = None

            return
        else:
            raise ClientIsRunning
