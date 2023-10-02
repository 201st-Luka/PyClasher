from enum import Enum


__all__ = (
    'RequestMethods',
)


class RequestMethods(Enum):
    REQUEST = "get"
    POST = "post"
