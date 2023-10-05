"""
functions.py file

This file contains helper functions that are used in the package.
"""


__all__ = (
    'snake_to_camel',
)


def snake_to_camel(snake_str: str) -> str:
    """
    function that transforms a string in snake case form into a string in
    camel case from

    Args:
        snake_str (str):    the string in snake case form

    Returns:
        str:    ``snake_str`` but transformed from snake case to camel case
    """
    components = snake_str.split('_')
    camel_str = components[0] + ''.join(
        x.title() for x in components[1:]
    )
    return camel_str
