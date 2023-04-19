class PlayerHouse:
    """
    Holds information of a player capital house
    """

    def __init__(self, response: dict):
        self.__response = response
        return

    @property
    def ground(self) -> int:
        for element in self.__response['elements']:
            if element['type'] == "ground":
                return element['id']

    @property
    def walls(self) -> int:
        for element in self.__response['elements']:
            if element['type'] == "walls":
                return element['id']

    @property
    def roof(self) -> int:
        for element in self.__response['elements']:
            if element['type'] == "roof":
                return element['id']

    @property
    def decoration(self) -> int:
        for element in self.__response['elements']:
            if element['type'] == "decoration":
                return element['id']

    def __repr__(self) -> str:
        return "PlayerHouse()"

    def __str__(self) -> str:
        return f"PlayerHouse(ground={self.ground}, walls={self.walls}, roof={self.roof}, decoration={self.decoration})"
