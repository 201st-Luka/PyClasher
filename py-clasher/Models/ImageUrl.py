from clashofclansApi.apiInterface import Interface


class ImageUrl:
    """
    Holds an image url and can return the content
    """

    api_interface: Interface = None
    __url: str = None

    def __init__(self, url: str):
        self.__url = url
        return

    async def get_image(self):
        ...

    @property
    def url(self) -> str:
        return self.__url

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__url})"

    def __str(self) -> str:
        return f"{self.__class__.__name__}({self.__url})"
