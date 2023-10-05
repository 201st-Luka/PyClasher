"""
request_methods.py file

This file contains the RequestMethods Enum.
"""


from enum import Enum


__all__ = (
    'RequestMethods',
)


class RequestMethods(Enum):
    """
    request methods enum
    """

    REQUEST = "get"
    """get request"""
    POST = "post"
    """post request"""
