from pyclasher.Models.IconUrls import IconUrls


class Label:
    """
    Holds information about the labels of a clan or a player
    """

    def __init__(self, response: dict) -> None:
        self.__response = response
        return

    @property
    def id(self) -> int:
        return self.__response['id']

    @property
    def name(self) -> int:
        return self.__response['name']

    @property
    def icon_urls(self) -> IconUrls:
        return IconUrls(self.__response['iconUrls'])

    @property
    def is_clan_label(self) -> bool:
        return 56000000 <= self.id <= 56000016

    @property
    def is_player_label(self) -> bool:
        return 57000000 <= self.id <= 57000018

    def __repr__(self) -> str:
        return f"Label({self.id})"

    def __str__(self) -> str:
        return f"Label(id={self.id}, name={self.name}, iconUrls={self.icon_urls}, is_clan_label={self.is_clan_label}, is_player_label={self.is_player_label})"
