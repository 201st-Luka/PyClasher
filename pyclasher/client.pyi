from logging import Logger
from typing import Iterable

from .exceptions import MISSING
from .request_queue import PQueue


global_client_id: int = ...


class Client:
    """
    this is the class for the ClashOfClans API client

    :cvar   __instances:            the private instance of the client
    :type   __instances:            Client
    :cvar   base_url:               the public base URL for the requests (usually https://api.clashofclans.com)
    :type   base_url:               str
    :cvar   endpoint:               the public endpoint URL for the requests (usually /v1)
    :type   endpoint:               str
    :cvar   requests_per_second:    the public number of requests done per consumer/token per second (usually 5)
    :type   requests_per_second:    int
    :cvar   logger:                 public logger to log the requests, ... (usually MISSING)
    :type   logger:                 Logger
    :ivar   queue:                  the public request_queue where the requests are enqueued
    :type   queue:                  RequestQueue
    :ivar   __consumers:            private list of consumers of the request_queue and requests
    :type   __consumers:            list[Consumer]
    :ivar   __consume_tasks:        private list of tasks of the consumer
    :type   __consume_tasks:        list[Task]
    :ivar   __temporary_session:    private boolean that indicates if the session is temporary or not
    :type   __temporary_session:    bool
    :ivar   __tokens:               private list of tokens
    :type   __tokens:               list[str]
    :ivar   __client_running:       private boolean that indicates if the client is running or not
    :type   __client_running:       bool
    """

    __instances: list[Client] = None

    base_url: str = "https://api.clashofclans.com"
    endpoint: str = "/v1"
    requests_per_second: int = 5
    logger: Logger = MISSING

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
        self.logger: Logger = ...
        self.__tokens: list[str] = ...
        self.requests_per_second: int = ...
        self.queue: PQueue = ...
        self.request_timeout: float = ...
        self.__client_running: bool = ...
        self.__temporary_session: bool = ...
        self.__consumers: list = ...
        self.__consume_tasks: list = ...
        self._client_id: int | str = ...
        self._event_client: bool = ...
        ...

    @classmethod
    async def from_login(cls,
                         email: str,
                         password: str,
                         requests_per_second: int = 5,
                         request_timeout: float = 30,
                         logger: Logger = MISSING,
                         login_count: int = 1
        ) -> Client:
        """
        login via the ClashOfClans login API to retrieve a temporary session (usually 1 hour)

        :param  email:                  user email address to log in to the ClashOfClans developer portal
        :param  password:               user password for the email
        :param  requests_per_second:    number of requests per token per second
        :param  request_timeout:        seconds until the request is cancelled due to a timeout
        :param  logger:                 logger
        :param  login_count:            number of logins that should be done (having more logins results more tokens
                                        and this leads to more requests that can be executed in parallel)
        .. note::                       do not set the ``login_count`` to high, otherwise the account could be banned
                                        (5 works fine)
        :return:                        an instance of the pyclasher client or a coroutine that returns an instance of
                                        the pyclasher client
        :rtype:                         Client
        """
        ...

    async def start(self, tokens: str | Iterable[str] = None) -> Client:
        """
        start the client

        :param tokens:  the Bearer tokens for the authentication of the ClashOfClans API
        :type tokens:   str | list[str] | None
        :return:        the instance of the client
        :rtype:         PyClasherClient
        """
        ...

    async def close(self) -> Client:
        """
        close the client

        :return:    the instance of the client
        :rtype:     Client
        """
        ...

    async def __aenter__(self) -> Client:
        ...

    async def __aexit__(self, exc_type, exc_val, exc_tb) -> Client:
        ...

    def __del__(self) -> None:
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

    @property
    def client_id(self):
        ...

    @client_id.setter
    def client_id(self, new_id: int | str):
        self._client_id: int | str = ...

    @classmethod
    def get_instance(cls, client_id: int | str = None) -> None | Client:
        ...

    @classmethod
    def initialized(cls) -> bool:
        ...
