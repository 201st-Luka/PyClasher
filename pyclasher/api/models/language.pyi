from .abc import BaseModel


__all__ = (
    'Language',
)


class Language(BaseModel):
    """
    language model
    """

    @property
    def name(self) -> str:
        """
        getter of the language name

        :return:    the language name
        :rtype:     str
        """
        ...

    @property
    def id(self) -> int:
        """
        getter of the language id

        :return:    the language id
        :rtype:     str
        """
        ...

    @property
    def language_code(self) -> str:
        """
        getter of the language code

        :return:    the language code
        :rtype:     str
        """
        ...
