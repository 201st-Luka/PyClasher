from ..BaseModels import BaseModel


class Language(BaseModel):
    def __init__(self, data: dict):
        super().__init__(data)
        self._main_attribute = self.id
        return

    @property
    def name(self) -> str:
        return self._get_data('name')

    @property
    def id(self) -> int:
        return self._get_data('id')

    @property
    def language_code(self) -> str:
        return self._get_data('languageCode')






