class District:
    """
    Holds information about a clan capital district
    """

    def __init__(self, response: dict):
        self.__response = response
        return

    @property
    def id(self) -> int:
        return self.__response['id']

    @property
    def name(self) -> str:
        return self.__response['name']

    @property
    def district_hall_level(self) -> int:
        return self.__response['districtHallLevel']

    def __repr__(self) -> str:
        return f"District({repr(self.id)})"

    def __str__(self) -> str:
        return f"District(id={str(self.id)}, name={str(self.name)}, district_hall_level={str(self.district_hall_level)})"


class ClanCapital:
    """
    Holds information about the clan capital
    """

    def __init__(self, response: dict):
        self.__response = response
        return

    @property
    def capital_hall_level(self) -> int:
        return self.__response['capitalHallLevel']

    @property
    def districts(self) -> list[District]:
        return [District(district) for district in self.__response['districts']]

    def __repr__(self) -> str:
        return f"ClanCapital({self.capital_hall_level})"

    def __str__(self) -> str:
        return f"ClanCapital(capital_hall_level={self.capital_hall_level}, districts={self.districts})"
