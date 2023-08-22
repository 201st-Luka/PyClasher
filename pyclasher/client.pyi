from asyncio import Queue, Future, Task, AbstractEventLoop
from enum import Enum
from logging import Logger
from typing import Iterable, Coroutine, Any

from aiohttp import ClientSession

from .api.models import BaseModel
from .exceptions import MISSING








class PyClasherClient:
    """
    this is the class for the ClashOfClans API client

    :cvar   __instance:             the private instance of the client
    :type   __instance:             PyClasherClient
    :cvar   base_url:               the public base URL for the requests (usually https://api.clashofclans.com)
    :type   base_url:               str
    :cvar   endpoint:               the public endpoint URL for the requests (usually /v1)
    :type   endpoint:               str
    :cvar   queue:                  the public request_queue where the requests are enqueued
    :type   queue:                  RequestQueue
    :cvar   requests_per_second:    the public number of requests done per consumer/token per second (usually 5)
    :type   requests_per_second:    int
    :cvar   logger:                 public logger to log the requests, ... (usually MISSING)
    :type   logger:                 Logger
    :cvar   initialised:            public boolean that indicates if the
    :type   initialised:            bool
    :cvar   __loop:                 abstract event loop that is used for making requests if no loop is running
    :type   __loop:                 AbstractEventLoop
    :cvar   __consumers:            private list of consumers of the request_queue and requests
    :type   __consumers:            list[Consumer]
    :cvar   __consume_tasks:        private list of tasks of the consumer
    :type   __consume_tasks:        list[Task]
    :cvar   __temporary_session:    private boolean that indicates if the session is temporary or not
    :type   __temporary_session:    bool
    :cvar   __tokens:               private list of tokens
    :type   __tokens:               list[str]
    :cvar   __client_running:       private boolean that indicates if the client is running or not
    :type   __client_running:       bool
    """

    __instance: PyClasherClient = None

    base_url: str = "https://api.clashofclans.com"
    endpoint: str = "/v1"
    queue: RequestQueue = None
    requests_per_second: int = 5
    logger: Logger = MISSING
    initialised = False
    __loop: AbstractEventLoop = MISSING
    __consumers: list[Consumer] = None
    __consume_tasks: list[Task] = None
    __temporary_session: bool = False
    __tokens: list[str] | None = None
    __client_running: bool = False

    def __new__(cls, *args, **kwargs):
        ...

    def __init__(
            self,
            tokens: str | Iterable[str] = None,
            requests_per_second: int = 5,
            request_timeout: float = 30,
            logger: Logger = MISSING,
            swagger_url: str = None
    ) -> None:
        """
        initialisation method for the client

        :param  tokens:                 the Bearer tokens for the authentication of the ClashOfClans API
        :type   tokens:                 str | list[str] | None
        :param  requests_per_second:    This integer limits the number of requests done per second (per token).
                                        This value is important to bypass the rate limit of the ClashOfClans API.
                                        More tokens allow more requests per second because each token can do
                                        as many requests per second as specified.
                                        Defaults to 5.
        :type   requests_per_second:    int
        :param  logger:                 logger for detailed logging
                                        Defaults to None
        :type   logger:                 Logger
        :param  swagger_url:            swagger url for requests
                                        Defaults to None
        :type   swagger_url:            str
        :return:                        None
        :rtype:                         None
        """
        self.request_timeout = request_timeout
        ...

    @classmethod
    def from_login(cls,
                   email: str,
                   password: str,
                   requests_per_second: int = 5,
                   request_timeout: float = 30,
                   logger: Logger = MISSING,
                   login_count: int = 1
                   ) -> PyClasherClient | Coroutine[Any, Any, PyClasherClient]:
        """
        login via the ClashOfClans login API to retrieve a temporary session (usually 1 hour)

        :param  email:                  user email address to log in to the ClashOfClans developer portal
        :param  password:               user password for the email
        :param  requests_per_second:    number of requests per token per second
        :param  request_timeout:        seconds until the request is cancelled due to a timeout
        :param  logger:                 logger
        :param  login_count:            number of logins that should be done (having more logins results more tokens and this leads to more requests that can be executed in parallel)
        .. note::                       do not set the ``login_count`` to high, otherwise the account could be banned (5 works fine)
        :return:                        an instance of the pyclasher client or a coroutine that returns an instance of the pyclasher client
        :rtype:                         PyClasherClient | Coroutine[Any, Any, PyClasherClient]
        """
        ...

    @property
    def is_running(self) -> bool:
        """
        property that indicates if the client is running

        status changes if the client is started or stopped

        :return:    boolean indicating if the client is running, True if running else otherwise
        :rtype:     bool
        """
        ...

    def start(self, tokens: str | Iterable[str] = None) -> PyClasherClient:
        """
        start the client

        :param tokens:  the Bearer tokens for the authentication of the ClashOfClans API
        :type tokens:   str | list[str] | None
        :return:        the instance of the client
        :rtype:         PyClasherClient
        """
        ...

    def close(self) -> PyClasherClient | Coroutine[Any, Any, PyClasherClient]:
        """
        close the client

        this method can be used in an asynchronous context using the ``await`` keyword
        but can also be used in non-asynchronous context without awaiting the method

        :return:    the instance of the client
        :rtype:     PyClasherClient | Coroutine[Any, Any, PyClasherClient]
        """
        ...

    def __enter__(self) -> PyClasherClient:
        ...

    def __exit__(self, exc_type, exc_val, exc_tb) -> PyClasherClient:
        ...

    async def __aenter__(self) -> PyClasherClient:
        ...

    async def __aexit__(self, exc_type, exc_val, exc_tb) -> PyClasherClient:
        ...

    def __del__(self) -> None:
        ...

    @property
    def loop(self) -> AbstractEventLoop:
        ...

    def reset_client(self, reset_queue: bool = True, reset_loop: bool = True, reset_tokens: bool = True) -> None:
        ...
