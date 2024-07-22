"""
``Request`` class

This class is used in subclasses to make and execute requests to the ClashOfClans API.
"""

from .Client import Client
from .base import ObjectModel
from .base.IRequest import IRequest
from .exceptions import MISSING
from .utils.RequestMode import RequestMode


class Request(IRequest, ObjectModel):
    """
    Class for creating requests to the ClashOfClans API

    Attributes:
        _request_id (int):
            the request id
        _url (str):
            the url of the request
        request_mode (RequestMode):
            request method
        _body (dict):
            additional data that is to be sent with the request
        _url_kwargs (dict):
            the url kwargs that are to replace in the url
        client (Client | int | str):
            the client or its client ID that is used to make the request
        _data (dict):
            the response data of the request
    """

    def __init__(
        self,
        raw_url: str,
        request_mode: RequestMode = RequestMode.GET,
        body: dict = None,
        kwargs: dict[str, str] = None,
        client: Client | int | str = None,
        **url_kwargs: str,
    ) -> None:
        """
        Args:
            raw_url (str):
                the url of the request
            request_mode (RequestMode):
                request method
            body (dict):
                additional data that is to be sent with the request
            kwargs (dict[str, str]):
                dict of kew word arguments that can be encoded in the API request
            client (Client | int | str):
                the client or its client ID that is used to make the request
            url_kwargs (str):
                the url kwargs that are to replace in raw_url
        """
        IRequest.__init__(self, raw_url, request_mode, body, kwargs, client, **url_kwargs)
        ObjectModel.__init__(self, MISSING)
