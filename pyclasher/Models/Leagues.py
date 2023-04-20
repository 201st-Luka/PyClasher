from pyclasher.Exceptions import RequestNotDone
from pyclasher.Models.IconUrls import IconUrls


class __League:
    """
    Holds information about a league
    """

    __response: dict = None
    __league_id: int = None

    def __init__(self, league_id: int) -> None:
        self.__league_id = league_id
        return

    @classmethod
    def from_json(cls, league_json: dict):
        cls.__response = league_json
        return cls(league_json['id'])

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
    def icon_urls(self) -> IconUrls | None:
        if 29000000 <= self.id <= 29000022:
            return IconUrls(self.__response['iconUrls'])
        return None

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.id})"

    def __str__(self) -> str:
        if 29000000 <= self.id <= 29000022:
            return f"{self.__class__.__name__}(id={self.id}, name={self.name}, iconUrls={self.icon_urls})"
        return f"{self.__class__.__name__}(id={self.id}, name={self.name})"


class CapitalLeague(__League):
    """
    Holds capital league information
    """

    def __init__(self, capital_league_id: int) -> None:
        super().__init__(capital_league_id)
        return


class WarLeague(__League):
    """
    Holds war league information
    """

    def __init__(self, war_league_id: int) -> None:
        super().__init__(war_league_id)
        return


class PlayerLeague(__League):
    """
    Holds player league information
    """

    def __init__(self, player_league_id: int) -> None:
        super().__init__(player_league_id)
        return
