"""
abc.pyi file

This file contains the type hints of the abstract base classes of the bulk
requests.
"""


from typing import Any, Coroutine, Iterator, Generator


__all__ = (
    'BulkRequestModel',
)


class BulkRequestModel:
    """
    bulk request base class

    Attributes:
        _request_model (Any):
            request model of the requests
        _requests (list):
            list of the requests
        _tasks (list[typing.Coroutine]):
            list of request tasks
    """

    _request_model: Any = ...
    _requests: list = None

    def __init__(self):
        """
        Initialisation method of the bulk requests
        """
        self._tasks: list[Coroutine] = ...

    @property
    def request_model(self) -> Any:
        """
        Property that returns the request model used of the subclass

        Returns:
            Any: returns the request model used of the subclass
        """
        ...

    @property
    def requests(self) -> list:
        """
        Property that returns the requests that are running

        Returns:
            list: returns the requests that are running
        """
        ...

    def __get_properties(self) -> dict:
        """
        Method that returns a dictionary of the class' properties and its names.

        Returns:
            dict: dictionary of the class' properties and its names
        """
        ...

    async def request(self, client_id: int | str = None) -> BulkRequestModel:
        """
        Coroutine method that requests the requests

        Args:
            client_id (int | str):
                ID of a client

        Returns:
            BulkRequestModel: returns itself
        """
        self._tasks = [request.request(client_id) for request in self._requests]
        ...

    def __len__(self) -> int:
        """
        Magic method that retrieves the length of the bulk request tasks.

        Returns:
            int: the length of the bulk request tasks
        """
        ...

    def __getitem__(self, item: int | slice) -> Generator | _request_model:
        """
        Getter of a single request or multiple requests

        Args:
            item (int | slice):
                index or slice of the request(s)

        Returns:
            typing.Any:
                A single request
            list[typing.Any]:
                A list of requests if a slice was used
        """
        ...

    def __iter__(self) -> Iterator[_request_model]:
        """
        Iterator object of the requests

        Returns:
            typing.Iterator:
                Iterator object of the requests
        """
        self._iter = iter(self._requests)
        ...

    def __next__(self) -> _request_model:
        """
        Next request of iteration

        Returns:
            typing.Any:
                Next request of the iteration
        """
        ...

    def __str__(self) -> str:
        """
        String of the bulk requests object

        Returns:
            str:
                String of the bulk requests object
        """
        ...

    def __repr__(self) -> str:
        """
        Representation of the bulk requests object

        Returns:
            str:
                Representation of the bulk request object
        """
        ...
