"""
``RequestMethods`` enum class
"""

from enum import Enum


class RequestMode(Enum):
    """
    Enum that contains the request modes

    Attributes:
        GET (str):  get request
        POST (str):     post request
    """

    GET = "get"
    POST = "post"
