from typing import Any, Coroutine, Iterator, Generator


__all__ = (
    'BulkRequestModel',
)


class BulkRequestModel:
    """
    bulk request base model

    can be inherited from

    :cvar   _request_model:     the request model that is used to make the bulk request
    :type   _request_model:     Any
    :cvar   _requests:          list of requests
    :type   _requests:          list
    """

    _request_model: Any = ...
    _requests: list = None

    def __init__(self):
        self._tasks: list[Coroutine] = ...

    @property
    def request_model(self) -> Any:
        """
        property of the request model

        :return:    the specified request model
        :rtype:     Any
        """
        ...

    @property
    def requests(self) -> list:
        """
        property of the requests

        :return:    the list of the requests or None if the requests are not done yet
        :rtype:     list
        """
        ...

    def __get_properties(self) -> dict:
        """
        private method that creates a dictionary of the properties

        key:    name of the property

        value:  value of the property

        :return:    a dictionary of the properties
        :rtype:     dict
        """
        ...

    async def request(self, client_id: int | str = None) -> BulkRequestModel:
        """
        asynchronous method that executes the requests

        :return:    the instance of the bulk request model
        :rtype:     BulkRequestModel
        """
        self._tasks = [request.request(client_id) for request in self._requests]
        ...

    def __len__(self) -> int:
        ...

    def __getitem__(self, item: int | slice) -> Generator | _request_model:
        ...

    def __iter__(self) -> Iterator[_request_model]:
        self._iter = iter(self._requests)
        ...

    def __next__(self) -> _request_model:
        ...

    def __str__(self) -> str:
        ...

    def __repr__(self) -> str:
        ...
