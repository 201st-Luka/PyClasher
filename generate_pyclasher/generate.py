from json import load
from os import mkdir, makedirs
from os.path import join

from jinja2 import Template

from .helper_functions import convert_operation_id, camel_to_snake_case

EXCEPTIONAL_TAGS = ['labels']
EXCEPTIONAL_PATHS = {
    'leagues': [
        "capitalleagues",
        "clanwarleagues",
        "builderbaseleagues",
        "warleagues",
    ]
}
EXCEPTIONAL_DEFINITIONS = {
    'JsonLocalizedName': "str",
    'JsonNode': "dict",
    'Float': "float",
    'String': "str",
    'string': "str",
    'integer': "int",
    'boolean': "bool",
    'object': "dict",
}


def generate_requests(yaml, generated_path: str):
    for tag in yaml['tags']:
        path = join(generated_path, 'requests', tag['name'])

        makedirs(path)

        with open(join(path, "__init__.py"), "w", encoding="utf-8") as init_py:
            init_py.write(f"\"\"\"\n{tag['description']}\n\"\"\"")

    for tag in EXCEPTIONAL_TAGS:
        path = join(generated_path, 'requests', tag)

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

    with open(join("generate_pyclasher", "main_attribute_mapping.json"), "r",
              encoding="utf-8") as main_attribute_mapping_file:
        main_attribute_mapping = load(main_attribute_mapping_file)

    jinja_template = Template(open("generate_pyclasher/model_template.py.jinja", "r", encoding="utf-8").read())

    init_imports = []

    for def_key, def_value in yaml['definitions'].items():
        if def_key in EXCEPTIONAL_DEFINITIONS or def_key.endswith("List"):
            continue

        file_import_level = 2
        annotations = []
        imports = {'model_abc': {
            'import_level': 2,
            'imports': {'Model', 'ModelWrapper'}
        }}

        if def_value['type'] == 'object':
            for prop_key, prop_value in def_value['properties'].items():
                if prop_key in EXCEPTIONAL_DEFINITIONS:
                    continue

                annotation = {'name': camel_to_snake_case(prop_key)}

                if 'type' in prop_value:
                    type_ = prop_value['type']

                    if type_ in EXCEPTIONAL_DEFINITIONS:
                        type_ = EXCEPTIONAL_DEFINITIONS[type_]

                    annotation['type'] = type_

                else:
                    type_ = prop_value['$ref'].removeprefix('#/definitions/')

                    if type_ in EXCEPTIONAL_DEFINITIONS:
                        type_ = EXCEPTIONAL_DEFINITIONS[type_]
                        annotation['type'] = type_
                    else:
                        if type_.endswith("List"):
                            type_ = type_.removesuffix("List")

                            annotation['type'] = f"ArrayIterator[{type_}]"
                            imports['model_abc']['imports'].add('ArrayIterator')
                        else:
                            annotation['type'] = type_

                        imports.setdefault(type_, {'import_level': 0, 'imports': set()})['imports'].add(type_)

                annotations.append(annotation)

        init_imports.append(def_key)

        with open(join(path, def_key + ".py"), "w", encoding="utf-8") as definition_py:
            definition_py.writelines(jinja_template.generate(
                class_name=def_key,
                file_import_level=file_import_level,
                main_attributes=main_attribute_mapping.get(def_key),
                exclude_annotations=None,
                description=None,
                annotations=sorted(annotations, key=lambda x: x['name']),
                imports=imports
            ))

    with open(join(path, "__init__.py"), "w", encoding="utf-8") as init_py:
        init_py.writelines((f"from .{init_import} import {init_import}\n" for init_import in init_imports))


def generate_paths(yaml, generated_path: str):
    path = join(generated_path, 'requests')

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
    print("Generating requests...")
    generate_requests(yaml, generated_path)

    print("Generating responses...")
    generate_responses(yaml, generated_path)

    print("Generating definitions...")
    generate_definitions(yaml, generated_path)

    print("Generating paths...")
    generate_paths(yaml, generated_path)
