"""
``RequestMethods`` enum class
"""


from enum import Enum


class RequestMethods(Enum):
    """
    Enum that contains the request method types

    Attributes:
        GET (str):  get request
        POST (str):     post request
    """
    GET = "get"
    POST = "post"
