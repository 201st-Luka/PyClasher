"""
``Model`` class
"""

from ..exceptions import MISSING, Missing, RequestNotDone


class Model:
    """
    Abstract base class for API models

    Attributes:
        _data (dict[str, int | str | float | list | dict] | None):
            Data dictionary of the API response
    """

    def __new__(cls, *args, data: dict | Missing = None, **kwargs) -> "Model":
        """
        Args:
            data (dict | Missing):
                Data dictionary of the API response
        """
        if data is MISSING:
            return MISSING
        return super().__new__(cls)

    def __init__(self, data: dict[str, int | str | float | list | dict] | Missing = None) -> None:
        """
        Args:
            data (dict[str, int | str | float | list | dict] | Missing):
                Data dictionary of the API response
        """
        self._data = data

    def to_dict(self) -> dict[str, int | str | float | list | dict] | None:
        """
        Return the data dictionary of the model

        Returns:
            dict[str, int | str | float | list | dict] | None:
                Data dictionary of the model
        """
        return self._data

    def _get_data(self, item: str) -> int | str | float | list | dict | Missing | None:
        """
        Data accessor that handles wrong or the absence of data

        Args:
            item (str):
                The key in the data dictionary

        Returns:
            int | str | float | list | dict:
                Value of the key in the data dictionary
            MISSING:
                The request was done but the key is missing in the data dictionary (most likely because the API got
                an update, and it has not been implemented yet)
            None:
                The data dictionary is None (most likely because the ``RequestNotDone`` exception is wanted to be
                suppressed by a subclass)

        Raises:
            RequestNotDone:
                The request was not executed before accessing the data
        """
        if self._data is None:
            return None
        if self._data is MISSING:
            raise RequestNotDone
        if item in self._data:
            return self._data[item]
        else:
            return MISSING

    def __str__(self) -> str:
        if self._data is MISSING:
            return f"{self.__class__.__name__}(RequestNotDone)"
        if hasattr(self, "_primary_attributes"):
            return (
                f"{self.__class__.__name__}"
                f"({', '.join((f'{primary_attr}={self._primary_attributes[primary_attr].__get__(self)}'
                               for primary_attr in self._primary_attributes))})"
            )
        return f"{self.__class__.__name__}()"

    def _get_properties(self) -> dict[str, int | str | float | list | dict] | Missing | None:
        """
        Return a dictionary containing the names of properties and their values

        Returns:
            dict[str, int | str | float | list | dict]:
                Dictionary containing the names of properties and their values
            MISSING:
                The request was not executed before accessing the data
            None:
                The data dictionary is None (most likely because the ``RequestNotDone`` exception is wanted to be
                suppressed by a subclass)
        """
        if isinstance(self._data, dict) and hasattr(self, "_properties"):
            return {name: prop.__get__(self) for name, prop in self._properties.items()}
        return self._data

    def __repr__(self) -> str:
        props = ", ".join(
            (
                "=".join((key, str(value))) for key, value in self._get_properties().items()
            )  # map all properties in the object representation
        )
        return f"{self.__class__.__name__}({props})"
