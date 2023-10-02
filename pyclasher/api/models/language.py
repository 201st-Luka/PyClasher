from .abc import BaseModel


__all__ = (
    'Language',
)


class Language(BaseModel):
    def __init__(self, data: dict):
        super().__init__(data)
        return

    @property
    def name(self):
        return self._get_data('name')

    @property
    def id(self):
        return self._get_data('id')

    @property
    def language_code(self):
        return self._get_data('languageCode')
