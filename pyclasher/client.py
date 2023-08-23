from sys import stderr
from asyncio import create_task, run
from typing import Iterable
from urllib.parse import urlparse

from .request_queue import PConsumer, PQueue
from .utils.login import Login
from .exceptions import (InvalidType, ClientIsRunning, ClientIsNotRunning,
                         NoneToken, MISSING, ClientAlreadyInitialised)


client_id = 0


class Client:
    __instances = None

    base_url = "https://api.clashofclans.com"
    endpoint = "/v1"
    requests_per_second = 5
    logger = MISSING

    def __new__(cls, *args, **kwargs):
        if cls.__instances is None:
            cls.__instances = [super().__new__(cls)]
            return cls.__instances[0]
        if 'tokens' in kwargs:
            if isinstance(kwargs['tokens'], str):
                tokens = [kwargs['tokens']]
            elif isinstance(kwargs['tokens'], Iterable):
                tokens = list(kwargs['tokens'])
            else:
                raise InvalidType(kwargs['tokens'], (str, Iterable[str]))
            for token in tokens:
                for client in Client.__instances:
                    if client.__tokens is not None:
                        if token in client.__tokens:
                            raise ClientAlreadyInitialised
                        continue

        cls.__instances.append(super().__new__(cls))
        return cls.__instances[-1]

    def __init__(
            self,
            tokens=None,
            requests_per_second=5,
            request_timeout=30,
            logger=MISSING,
            swagger_url=None
    ):
        global client_id

        if logger is None:
            logger = MISSING
        self.logger = logger
        self.logger.info("initialising client")
        if tokens is not None:
            if isinstance(tokens, str):
                self.__tokens = [tokens]
            elif isinstance(tokens, Iterable):
                self.__tokens = list(tokens)
            else:
                raise TypeError(f"Expected types str, list got {type(tokens)} "
                                f"instead")

        if swagger_url is not None:
            parsed_url = urlparse(swagger_url)
            self.base_url = f"{parsed_url.scheme}://{parsed_url.netloc}"
            self.endpoint = parsed_url.path[:-1]

        self.requests_per_second = requests_per_second

        self.logger.debug("client initialised")

        self.queue = PQueue()
        self.request_timeout = request_timeout

        self.__client_running = False
        self.__temporary_session = False
        self.__consumers = None
        self.__consume_tasks = None
        self._client_id = client_id

        client_id += 1

        self._event_client = False

        return

    @classmethod
    async def from_login(cls, email, password, requests_per_second=5,
                         request_timeout=30, logger=MISSING, login_count=1):
        if logger is None:
            logger = MISSING

        logins = [
            await Login(email, password).login() for _ in range(login_count)
        ]

        logger.info("initialising client via login")

        self = cls([login.temporary_api_token for login in logins],
                   requests_per_second,
                   request_timeout,
                   swagger_url=logins[0].swagger_url)
        self.logger = logger
        self.__temporary_session = True
        return self

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
        self.logger.info("starting client")

        self.__consumers = [
            PConsumer(self.queue, token, self.requests_per_second,
                      self.request_timeout, self.base_url)
            for token in tokens
        ]
        self.__consume_tasks = [
            create_task(consumer.consume()) for consumer in self.__consumers
        ]
        self.logger.debug("client started")

        return self

    async def close(self):
        self.logger.info("closing client")
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

        self.logger.debug("client closed")
        return self

    async def __aenter__(self):
        return await self.start()

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.close()
        return

    def __del__(self):
        Client.__instances.remove(self)
        if not len(Client.__instances):
            Client.__instances = None

        if self.__client_running:
            run(self.close())
            if self.logger is not MISSING:
                self.logger.warning("The client was still running, closed now.")
            else:
                print("The client was still running, closed now.", file=stderr)

        return

    @property
    def is_running(self) -> bool:
        return self.__client_running

    @property
    def client_id(self):
        return self._client_id

    @client_id.setter
    def client_id(self, new_id):
        if not isinstance(new_id, (int, str)):
            raise TypeError(f"Expected types int, str got {type(new_id)} "
                            f"instead.")
        self._client_id = new_id
        return

    @classmethod
    def get_instance(cls, client_id=None):
        if cls.__instances is None:
            return None
        clients = [client
                   for client in cls.__instances
                   if not client._event_client]
        if len(clients):
            if client_id is None:
                return clients[0]
            return clients[client_id]
        return None

    @classmethod
    def initialized(cls):
        return isinstance(cls.__instances, list)
