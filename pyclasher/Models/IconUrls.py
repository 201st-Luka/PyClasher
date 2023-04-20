from pyclasher.Models.ImageUrl import ImageUrl


class IconUrl(ImageUrl):
    """
    Holds an icon url
    """

    def __init__(self, icon_url: str) -> None:
        super().__init__(icon_url)
        return


class IconUrls:
    """
    Holds icon urls
    """

    def __init__(self, response: dict) -> None:
        self.__response = response
        return

    @property
    def tiny(self) -> IconUrl | None:
        if 'tiny' in self.__response:
            return IconUrl(self.__response['tiny'])
        return None

    @property
    def small(self) -> IconUrl:
        return IconUrl(self.__response['small'])

    @property
    def medium(self) -> IconUrl | None:
        if 'medium' in self.__response:
            return IconUrl(self.__response['medium'])
        return None

    def __repr__(self) -> str:
        return f"IconUrls({self.small})"

    def __str__(self) -> str:
        return f"IconUrls(tiny={self.tiny}, small={self.small}, medium={self.medium})"
