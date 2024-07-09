"""
``RequestMethods`` enum class
"""


from enum import Enum


class RequestMethods(Enum):
    """
    Enum that contains the request method types

    Attributes:
        REQUEST (str):  get request
        POST (str):     post request
    """
    REQUEST = "get"
    POST = "post"
