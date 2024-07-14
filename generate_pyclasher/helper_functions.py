def convert_operation_id(operation_id: str) -> str:
    operation_id = operation_id.removeprefix("get")
    if operation_id[0].islower():
        operation_id = operation_id[0].upper() + operation_id[1:]

    return operation_id


def camel_to_snake_case(camel_case: str) -> str:
    return "".join(["_" + i.lower() if i.isupper() else i for i in camel_case]).lstrip("_")
