class ChatLanguage:
    """
    Holds information about the chat language
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
    def language_code(self) -> str:
        return self.__response['languageCode']

    def __repr__(self) -> str:
        return f"ChatLanguage({self.id})"

    def __str__(self) -> str:
        return f"ChatLanguage(id={self.id}, name={self.name}, language_code={self.language_code})"
