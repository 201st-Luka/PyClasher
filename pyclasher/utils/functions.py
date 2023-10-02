__all__ = (
    'snake_to_camel',
)


def snake_to_camel(snake_str: str) -> str:
    components = snake_str.split('_')
    camel_str = components[0] + ''.join(
        x.title() for x in components[1:])
    return camel_str
