"""
``ModelWrapper`` decorator
"""

from typing import TypeVar, Callable

from .ArrayModel import ArrayModel
from .ObjectModel import ObjectModel
from .EnumModel import EnumModel
from ..utils import snake_to_camel

T = TypeVar("T", bound=type)
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
            assert isinstance(primary_attributes, (str, list))
        if exclude_annotations:
            assert isinstance(exclude_annotations, (str, list))

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
        from ..exceptions import InvalidModelParams  # import here to avoid circular imports

        def make_getter(key: str, type_: type) -> Callable:
            """
            method function to generate the properties

            Args:
                key (str):
                    the key that is used to access the data dictionary
                type_ (type):
                    the type of the data field
            Returns:
                property:
                    property that accesses the field of the data dictionary
            """
            if type_ in (str, int, float, bool, dict):

                def getter(self_: T):
                    return self_._get_data(key)

                return getter

            try:
                if issubclass(type_, (ObjectModel, EnumModel)):

                    def getter(self_: T):
                        return type_(self_._get_data(key))

                    return getter

            except TypeError:

                def getter(self_: T):
                    return ArrayModel(items=self_._get_data(key), type_=type_.__args__[0])

                return getter

        # make properties from annotations
        properties = {}
        for annotation_key, annotation_value in cls.__annotations__.items():
            if annotation_key in self.__exclude_annotations:
                continue
            value = cls.__dict__.get(annotation_key)
            if value:
                # annotation values can be used to give additional information to the property
                if isinstance(value, str):
                    fget = make_getter(value, annotation_value)
                else:
                    raise InvalidModelParams(f"{type(value)} is not a valid type for extra information.")
            else:
                fget = make_getter(snake_to_camel(annotation_key), annotation_value)
            prop = property(fget=fget)
            setattr(cls, annotation_key, prop)
            properties[annotation_key] = prop

        # set properties attribute
        if properties:
            setattr(cls, "_properties", properties)

        # set primary attributes
        if self.__primary_attributes:
            primary_attr_dict = {}
            if isinstance(self.__primary_attributes, str):
                if self.__primary_attributes in cls.__dict__:
                    primary_attr_dict[self.__primary_attributes] = getattr(cls, self.__primary_attributes)
                else:
                    raise InvalidModelParams(
                        f"Primary attribute definition '{self.__primary_attributes}' failed because it "
                        "is not an attribute of the class object."
                    )
            elif isinstance(self.__primary_attributes, list):
                for primary_attr in self.__primary_attributes:
                    if primary_attr in cls.__dict__ or primary_attr in getattr(cls, "_primary_attributes", {}):
                        primary_attr_dict[primary_attr] = getattr(cls, primary_attr)
                    else:
                        raise InvalidModelParams(
                            f"Primary attribute definition '{primary_attr}' failed because it "
                            "is not an attribute of the class object."
                        )

            setattr(cls, "_primary_attributes", primary_attr_dict)

        return cls
