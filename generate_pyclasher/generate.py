from json import load
from os import mkdir, makedirs
from os.path import join

from jinja2 import Template

from .helper_functions import (
    convert_operation_id,
    camel_to_snake_case,
    find_array_sub_definition,
    format_request_url,
    screaming_snake_to_camel,
)


def generate_tags(yaml, generated_path: str):
    # generate requests
    for tag in yaml["tags"]:
        path = join(generated_path, "requests", tag["name"])

        makedirs(path)

        with open(join(path, "__init__.py"), "w", encoding="utf-8") as init_py:
            init_py.write(f"\"\"\"\n{tag['description'].replace("\n", "\n    ")}\n\"\"\"\n\n\n")

    # generate exceptional requests to avoid errors in the future
    with open(join("generate_pyclasher", "json_data", "extra_tags.json"), "r", encoding="utf-8") as extra_tags_file:
        extra_tags = load(extra_tags_file)
    for tag in extra_tags:
        path = join(generated_path, "requests", tag)

        makedirs(path)

        with open(join(path, "__init__.py"), "w", encoding="utf-8") as init_py:
            init_py.write(f'"""\n{tag} tag"""\n\n\n')


def generate_responses(yaml, generated_path: str):
    path = join(generated_path, "responses")
    mkdir(path)

    jinja_template = Template(
        open(join("generate_pyclasher", "jinja_templates", "response_template.py.jinja"), "r", encoding="utf-8").read()
    )

    init_imports = []

    imports = {"definitions": {"import_level": 1, "imports": {"ClientError"}}}

    # generate responses
    for resp_key, resp_value in yaml["responses"].items():
        resp = resp_key.removesuffix("Spec")
        init_imports.append(resp)

        with open(join(path, resp + ".py"), "w", encoding="utf-8") as response_py:
            response_py.writelines(
                jinja_template.generate(
                    imports=imports,
                    class_name=resp,
                    parents=["ClientError"],
                    description=resp_value["description"].replace("\n", "\n    "),
                )
            )

    with open(join(path, "__init__.py"), "w", encoding="utf-8") as init_py:
        init_py.writelines((f"from .{init_import} import {init_import}\n" for init_import in sorted(init_imports)))


def generate_definitions(yaml, generated_path: str):
    path = join(generated_path, "definitions")
    mkdir(path)

    # load main attribute mapping
    with open(
        join("generate_pyclasher", "json_data", "primary_attribute_mapping.json"), "r", encoding="utf-8"
    ) as primary_attribute_mapping_file:
        primary_attribute_mapping = load(primary_attribute_mapping_file)

    # load base definitions
    with open(
        join("generate_pyclasher", "json_data", "base_definitions.json"), "r", encoding="utf-8"
    ) as base_definitions_file:
        base_definitions = load(base_definitions_file)

    # load custom parents
    with open(
        join("generate_pyclasher", "json_data", "custom_parents.json"), "r", encoding="utf-8"
    ) as custom_parents_file:
        custom_parents = load(custom_parents_file)["definitions"]

    # load enum mapping
    with open(join("generate_pyclasher", "json_data", "enum_mapping.json"), "r", encoding="utf-8") as enum_mapping_file:
        enum_mapping = load(enum_mapping_file)

    # load jinja template
    jinja_template = Template(
        open(
            join("generate_pyclasher", "jinja_templates", "definition_template.py.jinja"), "r", encoding="utf-8"
        ).read()
    )

    # imports if the module __init__.py file
    init_imports = []

    # generate definitions
    with open(
        join("generate_pyclasher", "json_data", "definitions_matcher.json"), "r", encoding="utf-8"
    ) as definitions_matcher_file:
        definitions_matcher = load(definitions_matcher_file)
    for def_key, def_value in yaml["definitions"].items():
        if def_key in definitions_matcher or def_key.endswith("List"):
            continue

        annotations = []
        imports = {"base": {"import_level": 3, "imports": {"ObjectModel", "ModelWrapper"}}}

        # get parent
        parents = ["ObjectModel"]
        parent_fields = []

        # check if custom parent
        custom_parent = custom_parents.get(def_key)
        if custom_parent is not None:
            if "ObjectModel" in parents:
                parents.remove("ObjectModel")
            parents.append(custom_parent["parent"])
            imports[custom_parent["import"]] = {
                "import_level": custom_parent["import_level"],
                "imports": {custom_parent["parent"]},
            }

        for base_def, base_values in base_definitions.items():
            if def_key in base_values["children"]:
                if "ObjectModel" in parents:
                    parents.remove("ObjectModel")
                parents.append(base_def)
                imports[base_def] = {"import_level": 1, "imports": {base_def}}
                parent_fields.extend(base_values["fields"].keys())

        # generate annotations
        if def_value["type"] == "object":
            for prop_key, prop_value in def_value["properties"].items():
                if prop_key in definitions_matcher or prop_key in parent_fields:
                    continue

                # generate annotation
                annotation = {"name": camel_to_snake_case(prop_key)}

                # generate type
                if "type" in prop_value:
                    type_ = prop_value["type"]

                    if "enum" in prop_value:
                        type_ = enum_mapping[prop_key][def_key]
                        imports.setdefault("enums", {"import_level": 2, "imports": set()})["imports"].add(type_)

                    elif type_ in definitions_matcher:
                        type_ = definitions_matcher[type_]

                    annotation["type"] = type_

                else:  # not a type but a definition
                    type_ = prop_value["$ref"].removeprefix("#/definitions/")

                    if type_ in definitions_matcher:  # type can be JsonNode or JsonLocalizedName
                        type_ = definitions_matcher[type_]
                        annotation["type"] = type_
                    else:
                        add_import = True
                        if type_.endswith("List"):
                            type_ = find_array_sub_definition(type_, yaml["definitions"])

                            matched_type = definitions_matcher.get(type_)
                            if matched_type is not None:
                                add_import = False
                                type_ = matched_type
                            elif type_ == def_key:
                                add_import = False
                                type_ = f"'{type_}'"

                            annotation["type"] = f"ArrayModel[{type_}]"
                            imports["base"]["imports"].add("ArrayModel")

                        else:
                            annotation["type"] = type_

                        if add_import:
                            imports.setdefault(type_, {"import_level": 1, "imports": set()})["imports"].add(type_)

                annotations.append(annotation)

        init_imports.append(def_key)

        # write definition file
        with open(join(path, def_key + ".py"), "w", encoding="utf-8") as definition_py:
            definition_py.writelines(
                jinja_template.generate(
                    class_name=def_key,
                    primary_attributes=primary_attribute_mapping.get(def_key),
                    exclude_annotations=None,
                    description=None,
                    annotations=sorted(annotations, key=lambda x: x["name"]),
                    imports=imports,
                    parents=parents,
                    sorted=sorted,
                )
            )

    # generate base definitions
    for base_def, base_values in base_definitions.items():
        with open(join(path, base_def + ".py"), "w", encoding="utf-8") as base_definition_py:
            base_definition_py.writelines(
                jinja_template.generate(
                    class_name=base_def,
                    imports={"base": {"import_level": 3, "imports": {"ObjectModel", "ModelWrapper"}}},
                    primary_attributes=sorted(
                        (camel_to_snake_case(field) for field in base_values["primary_attributes"])
                    ),
                    parents=["ObjectModel"],
                    annotations=sorted(
                        [
                            {"name": camel_to_snake_case(field), "type": type_}
                            for field, type_ in base_values["fields"].items()
                        ],
                        key=lambda x: x["name"],
                    ),
                    exclude_annotations=None,
                    sorted=sorted,
                )
            )

    # write module __init__.py file
    with open(join(path, "__init__.py"), "w", encoding="utf-8") as init_py:
        init_py.writelines((f"from .{init_import} import {init_import}\n" for init_import in sorted(init_imports)))


def generate_enums(yaml, generated_path: str):
    path = join(generated_path, "enums")
    mkdir(path)

    with open(join("generate_pyclasher", "json_data", "enum_mapping.json"), "r", encoding="utf-8") as enum_mapping_file:
        enum_mapping = load(enum_mapping_file)

    jinja_template = Template(
        open(join("generate_pyclasher", "jinja_templates", "enum_template.py.jinja"), "r", encoding="utf-8").read()
    )

    enums = {}
    for def_name, def_value in yaml["definitions"].items():
        for prop_name, prop_value in def_value.get("properties", {}).items():
            enum_value = prop_value.get("enum")
            if enum_value is not None:
                enums[enum_mapping[prop_name][def_name]] = enum_value
    for enum_name, enum_items in enums.items():
        with open(join(path, enum_name + ".py"), "w", encoding="utf-8") as enum_py:
            enum_py.writelines(
                jinja_template.generate(
                    class_name=enum_name, items={name: screaming_snake_to_camel(name) for name in enum_items}
                )
            )

    with open(join(path, "__init__.py"), "w", encoding="utf-8") as init_py:
        init_py.write(f'"""\nGenerated enums\n"""\n\n\n')
        init_py.writelines((f"from .{enum_name} import {enum_name}\n" for enum_name in sorted(enums.keys())))


def generate_paths(yaml, generated_path: str):
    path = join(generated_path, "requests")

    with open(
        join("generate_pyclasher", "json_data", "definitions_matcher.json"), "r", encoding="utf-8"
    ) as definitions_matcher_file:
        definitions_matcher = load(definitions_matcher_file)
    with open(join("generate_pyclasher", "json_data", "custom_paths.json"), "r", encoding="utf-8") as custom_paths_file:
        custom_paths = load(custom_paths_file)
    jinja_template = Template(
        open(join("generate_pyclasher", "jinja_templates", "path_template.py.jinja"), "r", encoding="utf-8").read()
    )

    tags_init_import = {}

    # generate paths
    for path_key, path_value in yaml["paths"].items():
        if "get" in path_value:
            mode = "get"
        elif "post" in path_value:
            mode = "post"
        else:
            raise Exception(f"Invalid request mode for path {path_key}: {path_value}.")

        # write to file
        class_name = convert_operation_id(path_value[mode]["operationId"])
        tag = path_value[mode]["tags"][0]
        tags_init_import.setdefault(tag, []).append(class_name)
        args, kwargs, body, imports, generic, methods = [], [], None, [], None, []
        parent = path_value[mode]["responses"]["200"]["schema"]["$ref"].removeprefix("#/definitions/")
        if yaml["definitions"][parent]["type"] == "array":
            generic = find_array_sub_definition(parent, yaml["definitions"])
            parent = None
            if generic in definitions_matcher:
                generic = definitions_matcher[generic]
            else:
                imports.append({"module": "definitions", "import_level": 3, "imports": {generic}})
        for param in path_value[mode].get("parameters", []):
            match param["in"]:
                case "path":
                    args.append(
                        {
                            "name": camel_to_snake_case(param["name"]),
                            "type": definitions_matcher[param["type"]],
                            "description": param["description"],
                        }
                    )
                case "query":
                    kwargs.append(
                        {
                            "original_name": param["name"],
                            "name": camel_to_snake_case(param["name"]),
                            "type": definitions_matcher[param["type"]],
                            "description": param["description"],
                        }
                    )
                case "body":
                    type_ = param["schema"]["$ref"].removeprefix("#/definitions/")
                    body = {
                        "name": param["name"],
                        "type": type_,
                        "description": param["description"],
                    }
                    imports.append({"module": "definitions", "import_level": 3, "imports": {type_}})
                case _:
                    raise Exception(f"Invalid parameter location for path {path_key}: {param}.")

        for param in (param for param in path_value[mode].get("parameters", []) if param["required"]):
            custom_path = custom_paths["parameters"].get(param["name"], {})
            class_methods = custom_path.get("class_methods", {})
            for c_m_name, c_m_def in class_methods.items():
                kwargs_string = (
                    ", " + ", ".join((f"{kwarg['name']}={kwarg['name']}" for kwarg in kwargs)) if kwargs else ""
                )
                methods.append(
                    {
                        "name": c_m_name,
                        "args": [{"name": "cls", "type": None}] + c_m_def["args"],
                        "kwargs": kwargs,
                        "return": {
                            "type": c_m_def["return"]["type"].format(class_name=class_name),
                            "description": c_m_def["return"]["description"].format(class_name=class_name),
                        },
                        "description": c_m_def["description"].format(class_name=class_name),
                        "body": [
                            line.format(class_name=class_name, kwargs_string=kwargs_string) for line in c_m_def["body"]
                        ],
                        "decorator": "classmethod",
                    }
                )
            if "imports" in custom_path:
                imports.extend(custom_path["imports"])

        custom_class = custom_paths["classes"].get(class_name, None)
        if custom_class is not None:
            parameter_type_overrides = custom_class.get("parameter_type_overrides", {})
            pto_args = parameter_type_overrides.get("args", {})
            pto_kwargs = parameter_type_overrides.get("kwargs", {})
            for arg, types in pto_args.items():
                index = 0
                for i, a in enumerate(args):
                    if a["name"] == arg:
                        index = i
                        break
                args[index]["type"] = " | ".join(types)
            for kwarg, types in pto_kwargs.items():
                index = 0
                for i, k in enumerate(kwargs):
                    if k["original_name"] == kwarg:
                        index = i
                        break
                kwargs[index]["type"] = " | ".join(types)
            new_imports = custom_class.get("imports", [])
            imports.extend(new_imports)

        with open(join(path, tag, class_name + ".py"), "w", encoding="utf-8") as path_py:
            path_py.writelines(
                jinja_template.generate(
                    request_type="IterativeRequest" if generic else "Request",
                    generic=generic,
                    class_name=class_name,
                    summary=path_value[mode]["summary"],
                    parent=parent,
                    description=path_value[mode]["description"].replace("\n", "\n    "),
                    raw_url=format_request_url(path_key),
                    url_args=args,
                    url_kwargs=kwargs,
                    body=body,
                    imports=imports,
                    methods=methods,
                )
            )

    # write tags __init__.py files
    for tag, classes in tags_init_import.items():
        with open(join(path, tag, "__init__.py"), "a", encoding="utf-8") as init_py:
            init_py.writelines((f"from .{class_name} import {class_name}\n" for class_name in sorted(classes)))

    # write module __init__.py file
    with open(join(path, "__init__.py"), "w", encoding="utf-8") as init_py:
        init_py.writelines((f"from .{init_import} import *\n" for init_import in sorted(tags_init_import.keys())))


def generate_api(yaml, generated_path: str):
    print("Generating requests...")
    generate_tags(yaml, generated_path)

    print("Generating responses...")
    generate_responses(yaml, generated_path)

    print("Generating definitions...")
    generate_definitions(yaml, generated_path)

    print("Generating enums...")
    generate_enums(yaml, generated_path)

    print("Generating paths...")
    generate_paths(yaml, generated_path)

    with open(join(generated_path, "__init__.py"), "w", encoding="utf-8") as init_py:
        init_py.write(f'"""\nGenerated API models, requests and responses\n"""\n\n\n')

    print("Done.")
