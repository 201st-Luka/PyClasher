from asyncio import gather


__all__ = (
    'BulkRequestModel',
)


class BulkRequestModel:
    _request_model = ...
    _requests = None

    def __init__(self):
        self._tasks = None

    @property
    def request_model(self):
        return self._request_model

    @property
    def requests(self):
        return self._requests

    def __get_properties(self):
        return {
            name: prop.__get__(self)
            for name, prop in vars(self.__class__).items()
            if isinstance(prop, property)
        }

    async def request(self, client_id=None):
        self._tasks = [request.request(client_id) for request in self._requests]
        await gather(*self._tasks)
        return self

    def __len__(self):
        return len(self._requests)

    def __getitem__(self, item):
        self._requests[0].to_dict()
        # test if the `to_dict()` method raises `RequestNotDone`
        if isinstance(item, int):
            return self._requests[item]
        if isinstance(item, slice):
            return (self._requests[i]
                    for i in range(*item.indices(len(self._requests))))
        raise NotImplementedError

    def __iter__(self):
        self._iter = iter(self._requests)
        return self

    def __next__(self):
        return next(self._iter)

    def __str__(self):
        return f"{self.__class__.__name__}()"

    def __repr__(self):
        props = ', '.join(
            ('='.join((key, str(value)))
             for key, value in self.__get_properties().items())
        )
        return f"{self.__class__.__name__}({props})"
