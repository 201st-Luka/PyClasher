from pyclasher.Exceptions import RequestNotDone
from pyclasher.Models.ImageUrl import ImageUrl


class BadgeUrl(ImageUrl):
    """
    class to hold a url for one badge
    """

    def __init__(self, badge_url: str):
        super().__init__(badge_url)
        return


class BadgeUrls:
    """
    class to hold data of a clan badge
    """

    __response: dict = None

    def __init__(self, badge_urls_json: dict):
        self.__response = badge_urls_json
        return

    @property
    def small(self) -> BadgeUrl:
        if self.__response is None:
            raise RequestNotDone
        return BadgeUrl(self.__response['small'])

    @property
    def medium(self) -> BadgeUrl:
        if self.__response is None:
            raise RequestNotDone
        return BadgeUrl(self.__response['medium'])

    @property
    def large(self) -> BadgeUrl:
        if self.__response is None:
            raise RequestNotDone
        return BadgeUrl(self.__response['large'])

    def __repr__(self) -> str:
        return f"BadgeUrls({self.medium})"

    def __str__(self) -> str:
        return f"BadgeUrls(small={self.small}, medium={self.medium}, large={self.large})"

