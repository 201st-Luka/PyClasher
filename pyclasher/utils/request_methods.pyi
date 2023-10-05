"""
request_methods.pyi file

This file contains the RequestMethods Enum type hints.
"""


from enum import Enum


__all__ = (
    'RequestMethods',
)


class RequestMethods(Enum):
    """
    request methods enum
    """

    REQUEST: str = ...
    """get request"""
    POST: str = ...
    """post request"""
