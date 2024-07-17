"""
``ModelWrapper`` decorator
"""

from typing import TypeVar, Callable

from pyclasher.exceptions import InvalidModelParams
from pyclasher.utils import snake_to_camel

T = TypeVar('T', bound=type)
"""Type variable for types/classes"""


class ModelWrapper:
    """
    Class decorator (class) for API models

    Attributes:
        __primary_attributes (str | list[str]):
            primary attributes that identify the decorated class
        __exclude_annotations (str | list[str]):
            annotations that are excluded from being converted to properties (they are ignored)
    """

    def __init__(self, primary_attributes: str | list[str] = None, exclude_annotations: str | list[str] = None) -> None:
        """
        Args:
            primary_attributes (str | list[str]):
                primary attributes that identify the decorated class
            exclude_annotations (str | list[str]):
                annotations that are excluded from being converted to properties (they are ignored)
        """
        if primary_attributes:
            assert isinstance(primary_attributes, (str, list[str]))
        if exclude_annotations:
            assert isinstance(exclude_annotations, (str, list[str]))

        self.__primary_attributes = primary_attributes
        self.__exclude_annotations = exclude_annotations or []

    def __call__(self, cls: T) -> T:
        """
        Args:
            cls (T):
                the decorated class
        Returns:
            T:
                the decorated class with properties instead of annotations
        """

        def make_getter(key: str) -> Callable:
            """
            method function to generate the properties

            Args:
                key (str):
                    the key that is used to access the data dictionary
            Returns:
                property:
                    property that accesses the field of the data dictionary
            """

            def getter(self_: T):
                return self_._get_data(key)

            return getter

        # make properties from annotations
        for annotation_key, annotation_value in cls.__annotations__.items():
            if annotation_key in self.__exclude_annotations:
                continue
            value = cls.__dict__.get(annotation_key)
            if value:
                # annotation values can be used to give additional information to the property
                match type(value):
                    case str.__class__:
                        fget = make_getter(value)
                    case _:
                        raise InvalidModelParams(f"{type(value)} is not a valid type for extra information.")
            else:
                fget = make_getter(snake_to_camel(annotation_key))
            setattr(cls, annotation_key, property(fget=fget))

        # set primary attributes
        if self.__primary_attributes:
            primary_attr_dict = {}
            if isinstance(self.__primary_attributes, str):
                if self.__primary_attributes in self.__dict__:
                    primary_attr_dict[self.__primary_attributes] = getattr(cls, self.__primary_attributes)
                else:
                    raise InvalidModelParams(
                        f"Primary attribute definition '{self.__primary_attributes}' failed because it "
                        "is not an attribute of the class object.")
            elif isinstance(self.__primary_attributes, list):
                for primary_attr in self.__primary_attributes:
                    if primary_attr in self.__dict__:
                        primary_attr_dict[primary_attr] = getattr(cls, primary_attr)
                    else:
                        raise InvalidModelParams(
                            f"Primary attribute definition '{primary_attr}' failed because it "
                            "is not an attribute of the class object.")

            setattr(cls, '_primary_attributes', primary_attr_dict)

        return cls
