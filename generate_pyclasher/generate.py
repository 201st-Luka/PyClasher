from os import mkdir, makedirs
from os.path import join

from .helper_functions import convert_operation_id, camel_to_snake_case

EXCEPTIONAL_TAGS = ['labels']
EXCEPTIONAL_PATHS = {
    'leagues': [
        'capitalleagues',
        'clanwarleagues',
        'builderbaseleagues',
        'warleagues',
    ]
}


def generate_tags(yaml, generated_path: str):
    for tag in yaml['tags']:
        path = join(generated_path, 'tags', tag['name'])

        makedirs(path)

        with open(join(path, "__init__.py"), "w", encoding="utf-8") as init_py:
            init_py.write(f"\"\"\"\n{tag['description']}\n\"\"\"")

    for tag in EXCEPTIONAL_TAGS:
        path = join(generated_path, 'tags', tag)

        makedirs(path)

        with open(join(path, "__init__.py"), "w", encoding="utf-8") as init_py:
            init_py.write(f"\"\"\"\n{tag} tag\n\"\"\"")


def generate_responses(yaml, generated_path: str):
    path = join(generated_path, 'responses')
    mkdir(path)

    for resp_key, resp_value in yaml['responses'].items():
        with open(join(path, resp_key + ".py"), "w", encoding="utf-8") as response_py:
            response_py.write(f"class {resp_key}:\n")
            response_py.write(f"    \"\"\"{resp_value['description']}\"\"\"\n")
            response_py.write("    pass\n")


def generate_definitions(yaml, generated_path: str):
    path = join(generated_path, 'definitions')
    mkdir(path)

    for def_key, def_value in yaml['definitions'].items():
        if def_value['type'] == 'object' and 'properties' in def_value:
            with open(join(path, def_key + ".py"), "w", encoding="utf-8") as definition_py:
                definition_py.write(f"class {def_key}:\n")

                for prop_key, prop_value in def_value['properties'].items():
                    key = camel_to_snake_case(prop_key)

                    if 'type' in prop_value:
                        type_ = prop_value['type']

                        match type_:
                            case "string":
                                type_ = "str"
                            case "integer":
                                type_ = "int"
                            case "boolean":
                                type_ = "bool"
                            case "object":
                                type_ = "dict"
                    else:
                        type_ = prop_value['$ref'].removeprefix('#/definitions/')
                    definition_py.write(f"    {key}: {type_}\n")


def generate_paths(yaml, generated_path: str):
    path = join(generated_path, 'tags')

    for path_key, path_value in yaml['paths'].items():
        request_url = path_key.strip("/").split('/')

        if 'get' in path_value:
            operation_id = convert_operation_id(path_value['get']['operationId'])
            summary = path_value['get']['summary']
            description = path_value['get']['description']
        elif 'post' in path_value:
            operation_id = path_value['post']['operationId']
            summary = path_value['post']['summary']
            description = path_value['post']['description']
        else:
            raise Exception(f"Invalid request method for path {path_key}: {path_value}.")

        try:
            with open(join(path, request_url[0], operation_id + ".py"), "w", encoding="utf-8") as path_py:
                path_py.write(f"class {operation_id}:\n")
                path_py.write(f"    \"\"\"{summary}\n\n{description}\"\"\"\n")
                path_py.write("    pass\n")
        except FileNotFoundError:
            for tag_key, tag_values in EXCEPTIONAL_PATHS.items():
                if request_url[0] in tag_values:
                    with open(join(path, tag_key, operation_id + ".py"), "w", encoding="utf-8") as path_py:
                        path_py.write(f"class {operation_id}:\n")
                        path_py.write(f"    \"\"\"{summary}\n\n{description}\"\"\"\n")
                        path_py.write("    pass\n")
                    break
            else:
                raise Exception(f"Invalid path {path_key}.")


def generate(yaml, generated_path: str):
    generate_tags(yaml, generated_path)
    generate_responses(yaml, generated_path)
    generate_definitions(yaml, generated_path)
    generate_paths(yaml, generated_path)
