from aiohttp import ClientResponse


ClientCodes = {
    200: "Successful response",
    400: "Client provided incorrect parameters for the request.",
    403: "Access denied, either because of missing/incorrect credentials or used API token does not grant access to the requested resource.",
    404: "Resource was not found.",
    429: "Request was throttled, because amount of requests was above the threshold defined for the used API token.",
    500: "Unknown error happened when handling the request.",
    503: "Service is temporarily unavailable because of maintenance."
}


class ClientError(Exception):
    """
    exception class to handle ClashOfClans API client errors
    """

    def __init__(self, response: ClientResponse, response_json: ClientResponse.json) -> None:
        self.__response = response
        self.__response_json = response_json
        return

    @property
    def status_code(self) -> int:
        return self.__response.status

    def __str__(self) -> str:
        return_str = ["ClashOfClans API Client Error:",
                      f"Code: {self.status_code} {ClientCodes[self.status_code]}",
                      f"Reason: {self.__response_json['reason']}" if 'reason' in self.__response_json else None,
                      f"Message: {self.__response_json['message']}" if 'message' in self.__response_json else None,
                      f"Type: {self.__response_json['type']}" if 'type' in self.__response_json else None,
                      f"Detail: {self.__response_json['detail']}" if 'detail' in self.__response_json else None
                      ]
        return "\n".join(string for string in return_str if string is not None)


class NoneArgument(Exception):
    def __str__(self):
        return "an argument is None"


class RequestNotDone(Exception):
    def __str__(self):
        return "the request was not done"


class NoneToken(Exception):
    def __str__(self):
        return "the token must be set globally using clashofclansApi.init(<your token>)"

