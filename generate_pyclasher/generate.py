from json import load
from os import mkdir, makedirs
from os.path import join

from jinja2 import Template

from .helper_functions import convert_operation_id, camel_to_snake_case

EXCEPTIONAL_TAGS = [
    'labels'
]
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
    # generate requests
    for tag in yaml['tags']:
        path = join(generated_path, 'requests', tag['name'])

        makedirs(path)

        with open(join(path, "__init__.py"), "w", encoding="utf-8") as init_py:
            init_py.write(f"\"\"\"\n{tag['description']}\n\"\"\"")

    # generate exceptional requests to avoid errors in the future
    for tag in EXCEPTIONAL_TAGS:
        path = join(generated_path, 'requests', tag)

        makedirs(path)

        with open(join(path, "__init__.py"), "w", encoding="utf-8") as init_py:
            init_py.write(f"\"\"\"\n{tag} tag\n\"\"\"")


def generate_responses(yaml, generated_path: str):
    path = join(generated_path, 'responses')
    mkdir(path)

    jinja_template = Template(open(join("generate_pyclasher", "jinja_templates", "response_template.py.jinja"), "r",
                                   encoding="utf-8").read())

    init_imports = []

    imports = {
        'definitions': {
            'import_level': 1,
            'imports': {"ClientError"}
        }
    }

    # generate responses
    for resp_key, resp_value in yaml['responses'].items():
        resp = resp_key.removesuffix("Spec")
        init_imports.append(resp)

        with open(join(path, resp + ".py"), "w", encoding="utf-8") as response_py:
            response_py.writelines(jinja_template.generate(
                imports=imports,
                class_name=resp,
                parents=["ClientError"],
                description=resp_value['description']
            ))

    with open(join(path, "__init__.py"), "w", encoding="utf-8") as init_py:
        init_py.writelines((f"from .{init_import} import {init_import}\n"
                            for init_import in sorted(init_imports)))


def generate_definitions(yaml, generated_path: str):
    path = join(generated_path, 'definitions')
    mkdir(path)

    # load main attribute mapping
    with open(join("generate_pyclasher", "json_data", "primary_attribute_mapping.json"), "r",
              encoding="utf-8") as primary_attribute_mapping_file:
        primary_attribute_mapping = load(primary_attribute_mapping_file)

    # load base definitions
    with open(join("generate_pyclasher", "json_data", "base_definitions.json"), "r",
              encoding="utf-8") as base_definitions_file:
        base_definitions = load(base_definitions_file)

    # load jinja template
    jinja_template = Template(open(join("generate_pyclasher", "jinja_templates", "definition_template.py.jinja"), "r",
                                   encoding="utf-8").read())

    # imports if the module __init__.py file
    init_imports = []

    # generate definitions
    for def_key, def_value in yaml['definitions'].items():
        if def_key in EXCEPTIONAL_DEFINITIONS or def_key.endswith("List"):
            continue

        annotations = []
        imports = {'model_abc': {
            'import_level': 3,
            'imports': {"Model", "ModelWrapper"}
        }}

        # get parent
        parents = ["Model"]
        parent_fields = []
        for base_def, base_values in base_definitions.items():
            if def_key in base_values['children']:
                parents.append(base_def)
                imports[base_def] = {
                    'import_level': 1,
                    'imports': {base_def}
                }
                parent_fields.extend(base_values['fields'].keys())

        # generate annotations
        if def_value['type'] == 'object':
            if def_key == "Clan":
                pass
            for prop_key, prop_value in def_value['properties'].items():
                if prop_key in EXCEPTIONAL_DEFINITIONS or prop_key in parent_fields:
                    continue

                # generate annotation
                annotation = {'name': camel_to_snake_case(prop_key)}

                # generate type
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

                        imports.setdefault(type_, {'import_level': 1, 'imports': set()})['imports'].add(type_)

                annotations.append(annotation)

        init_imports.append(def_key)

        # write definition file
        with open(join(path, def_key + ".py"), "w", encoding="utf-8") as definition_py:
            definition_py.writelines(jinja_template.generate(
                class_name=def_key,
                primary_attributes=primary_attribute_mapping.get(def_key),
                exclude_annotations=None,
                description=None,
                annotations=sorted(annotations, key=lambda x: x['name']),
                imports=imports,
                parents=parents,
                sorted=sorted
            ))

    # generate base definitions
    for base_def, base_values in base_definitions.items():
        with open(join(path, base_def + ".py"), "w", encoding="utf-8") as base_definition_py:
            base_definition_py.writelines(jinja_template.generate(
                class_name=base_def,
                imports={
                    'abc': {
                        'import_level': 0,
                        'imports': {"ABC"}
                    },
                    'model_abc': {
                        'import_level': 3,
                        'imports': {"Model", "ModelWrapper"}
                    }
                },
                primary_attributes=sorted((camel_to_snake_case(field) for field in base_values['fields'].keys())),
                parents=["ABC", "Model"],
                annotations=sorted([{'name': field, 'type': type_} for field, type_ in base_values['fields'].items()],
                                   key=lambda x: x['name']),
                exclude_annotations=None,
                sorted=sorted
            ))

    # write module __init__.py file
    with open(join(path, "__init__.py"), "w", encoding="utf-8") as init_py:
        init_py.writelines((f"from .{init_import} import {init_import}\n"
                            for init_import in sorted(init_imports)))


def generate_paths(yaml, generated_path: str):
    path = join(generated_path, 'requests')

    # generate paths
    for path_key, path_value in yaml['paths'].items():
        request_url = path_key.strip("/").split('/')

        # get operation id, summary and description
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

        # write path file
        try:
            with open(join(path, request_url[0], operation_id + ".py"), "w", encoding="utf-8") as path_py:
                path_py.write(f"class {operation_id}:\n")
                path_py.write(f"    \"\"\"{summary}\n\n{description}\"\"\"\n")
                path_py.write("    pass\n")
        # if the path is exceptional
        except FileNotFoundError:
            # check if the path is exceptional
            for tag_key, tag_values in EXCEPTIONAL_PATHS.items():
                if request_url[0] in tag_values:
                    # write path file
                    with open(join(path, tag_key, operation_id + ".py"), "w", encoding="utf-8") as path_py:
                        path_py.write(f"class {operation_id}:\n")
                        path_py.write(f"    \"\"\"{summary}\n\n{description}\"\"\"\n")
                        path_py.write("    pass\n")
                    break
                else:
                    raise Exception(f"Invalid path {path_key}.")


def generate_api(yaml, generated_path: str):
    print("Generating requests...")
    generate_requests(yaml, generated_path)

    print("Generating responses...")
    generate_responses(yaml, generated_path)

    print("Generating definitions...")
    generate_definitions(yaml, generated_path)

    print("Generating paths...")
    generate_paths(yaml, generated_path)

    with open(join(generated_path, "__init__.py"), "w", encoding="utf-8") as init_py:
        init_py.write(f"\"\"\"\nGenerated API models, requests and responses\n\"\"\"\n\n\n")
        init_py.write("from .definitions import *\n")
        init_py.write("from .requests import *\n")
        init_py.write("from .responses import *\n")
