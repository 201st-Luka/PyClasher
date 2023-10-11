"""
abc.py file

This file contains the abstract base classes of the bulk requests, and they
should not be instantiated.
"""


from asyncio import gather


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

    _request_model = ...
    _requests = None

    def __init__(self):
        """
        Initialisation method of the bulk requests
        """
        self._tasks = None

    @property
    def request_model(self):
        """
        Property that returns the request model used of the subclass

        Returns:
            Any: returns the request model used of the subclass
        """
        return self._request_model

    @property
    def requests(self):
        """
        Property that returns the requests that are running

        Returns:
            list: returns the requests that are running
        """
        return self._requests

    def __get_properties(self):
        """
        Method that returns a dictionary of the class' properties and its names.

        Returns:
            dict: dictionary of the class' properties and its names
        """
        return {
            name: prop.__get__(self)
            for name, prop in vars(self.__class__).items()
            if isinstance(prop, property)
        }

    async def request(self, client_id=None):
        """
        Coroutine method that requests the requests

        Args:
            client_id (int | str):
                ID of a client

        Returns:
            BulkRequestModel: returns itself
        """
        self._tasks = [request.request(client_id) for request in self._requests]
        await gather(*self._tasks)
        return self

    def __len__(self):
        """
        Magic method that retrieves the length of the bulk request tasks.

        Returns:
            int: the length of the bulk request tasks
        """
        return len(self._requests)

    def __getitem__(self, item):
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
        self._requests[0].to_dict()
        # test if the `to_dict()` method raises `RequestNotDone`
        if isinstance(item, int):
            return self._requests[item]
        if isinstance(item, slice):
            return [self._requests[i]
                    for i in range(*item.indices(len(self._requests)))]
        raise NotImplementedError

    def __iter__(self):
        """
        Iterator object of the requests

        Returns:
            typing.Iterator:
                Iterator object of the requests
        """
        self._iter = iter(self._requests)
        return self

    def __next__(self):
        """
        Next request of iteration

        Returns:
            typing.Any:
                Next request of the iteration
        """
        return next(self._iter)

    def __str__(self):
        """
        String of the bulk requests object

        Returns:
            str:
                String of the bulk requests object
        """
        return f"{self.__class__.__name__}()"

    def __repr__(self):
        """
        Representation of the bulk requests object

        Returns:
            str:
                Representation of the bulk request object
        """
        props = ', '.join(
            ('='.join((key, str(value)))
             for key, value in self.__get_properties().items())
        )
        return f"{self.__class__.__name__}({props})"
