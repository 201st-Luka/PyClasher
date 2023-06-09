from typing import Any, Coroutine


class BulkRequestModel:
    """
    bulk request base model

    can be inherited from

    :cvar   _request_model:     the request model that is used to make the bulk request
    :type   _request_model:     Any
    :cvar   _main_attribute:    the main attribute used for the string representation (default is None)
    :type   _main_attribute:    Any
    :cvar   _requests:          list of requests
    :type   _requests:          list
    """

    _request_model: Any = ...
    _main_attribute: Any = None
    _requests: list = None

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

    async def _async_request(self) -> BulkRequestModel:
        """
        asynchronous method that executes the requests

        :return:    the instance of the bulk request model
        :rtype:     BulkRequestModel
        """
        self._tasks = [request.request() for request in self._requests]
        ...

    def request(self) -> BulkRequestModel | Coroutine[Any, Any, BulkRequestModel]:
        """
        method that executes the request

        this method can be used in an asynchronous context using the ``await`` keyword
        but can also be used in non-asynchronous context without awaiting the method

        :return:    the instance of the model
        :rtype:     BulkRequestModel | Coroutine[Any, Any, BulkRequestModel]
        """
        ...

    def __len__(self) -> int:
        ...

    def __getitem__(self, item: int) -> _request_model:
        ...

    def __iter__(self):
        self._iter = iter(self._requests)
        ...

    def __next__(self) -> _request_model:
        ...

    def __str__(self) -> str:
        ...

    def __repr__(self) -> str:
        ...
