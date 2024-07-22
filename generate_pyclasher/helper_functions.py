def convert_operation_id(operation_id: str) -> str:
    operation_id = operation_id.removeprefix("get")
    if operation_id[0].islower():
        operation_id = operation_id[0].upper() + operation_id[1:]

    return operation_id


def camel_to_snake_case(camel_case: str) -> str:
    return "".join(["_" + i.lower() if i.isupper() else i for i in camel_case]).lstrip("_")


def find_array_sub_definition(type_, definitions) -> str:
    definition = definitions[type_]

    assert definition["type"] == "array"

    items = definition["items"]

    if "$ref" in items:
        return items["$ref"].removeprefix("#/definitions/")
    else:
        return items["type"]


def format_request_url(raw_url: str) -> str:
    start = raw_url.find("{")
    end = raw_url.find("}") + 1
    if start == -1 and end == 0:
        return raw_url
    else:
        return raw_url[:start] + camel_to_snake_case(raw_url[start:end]) + raw_url[end:]


def screaming_snake_to_camel(screaming_snake_str: str) -> str:
    words = screaming_snake_str.lower().split("_")
    return words[0] + "".join(word.capitalize() for word in words[1:])
