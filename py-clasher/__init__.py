import clashofclansApi.Models
import clashofclansApi.Requests
from .apiInterface import *
from .Exceptions import *

INTERFACE: Interface | None = None


def init(bearer_token: Iterable[str] | str, requests_per_second: int = 1):
    global INTERFACE
    Interface.tokens = bearer_token
    INTERFACE = Interface(requests_per_second)
    INTERFACE.start()
    apiInterface.RequestModel.api_interface = INTERFACE
    return
