from pyclasher.apiInterface import Interface
from pyclasher.Exceptions import  ClientError, NoneArgument, RequestNotDone


class Location:
    """
    Holds information about specific location
    """

    __response: dict = None
    __id: int = None
    url_path: str = "/v1/locations"
    api_interface: Interface = None

    def __init__(self, location_id: int) -> None:
        self.__id = location_id
        return

    @classmethod
    def from_json(cls, location_json: dict):
        cls.__response = location_json
        return cls(location_json['id'])

    async def __aenter__(self):
        await self.request()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        return

    async def request(self):
        if self.__id is None:
            raise NoneArgument
        async with self.api_interface.session.get(
            url="/".join((self.url_path, self.__id))
        ) as response:
            response_json = await response.json()
            if 'reason' in response_json:
                raise ClientError(response, response_json)
            self.__response = response_json
            return

    @property
    def id(self) -> int:
        if self.__response is None:
            raise RequestNotDone
        return self.__response['id']

    @property
    def name(self) -> str:
        if self.__response is None:
            raise RequestNotDone
        return self.__response['name']

    @property
    def is_country(self) -> bool:
        if self.__response is None:
            raise RequestNotDone
        return self.__response['isCountry']

    @property
    def country_code(self) -> str | None:
        if self.is_country:
            return self.__response['countryCode']
        return None

    def __repr__(self) -> str:
        return f"Location({self.id})"

    def __str__(self) -> str:
        if self.is_country:
            return f"Location(id={self.id}, name={self.name}, isCountry={self.is_country}, countryCode={self.country_code})"
        return f"Location(id={self.id}, name={self.name}, isCountry={self.is_country})"
