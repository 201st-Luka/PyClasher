import shutil
from os import walk, makedirs, getcwd
from os.path import join, relpath, splitext


def get_project_dir() -> str:
    return getcwd().removeprefix(join("docs", "doc_autogen.py"))


def create_markdown_structure(package_path, output_path):
    """
    Create a directory structure mirroring the Python package structure, with
    markdown files containing '::: pyclasher.path.filename' for each module.

    Args:
        package_path (str): The path to the Python package.
        output_path (str):  The path where the directory structure and markdown
                            files will be generated.
    """
    for dir_path, _, filenames in walk(package_path):
        relative_dir = relpath(dir_path, package_path)
        output_dir = join(output_path, relative_dir)
        makedirs(output_dir, exist_ok=True)

        for filename in filenames:
            if filename.endswith(".py") and filename != "__init__.py":
                module_name = splitext(filename)[0]
                import_path = ("pyclasher." + join(relative_dir if relative_dir != "." else "", module_name)).replace(
                    "/", "."
                )
                markdown_content = f"::: {import_path}\n"

                markdown_file_path = join(output_dir, f"{module_name}.md")

                with open(markdown_file_path, "w") as markdown_file:
                    print(f"Creating markdown file for {import_path}")
                    markdown_file.write(markdown_content)


def copy_contributing(package_path, docs_path):
    source_file = join(package_path, "CONTRIBUTING.md")
    dest_file = join(docs_path, "CONTRIBUTING.md")

    with open(source_file, "r") as file:
        print(f"Reading {source_file}...")
        contributing = file.read()

    with open(dest_file, "w") as copy:
        print(f"Writing {dest_file}...")
        copy.write(contributing)


if __name__ == "__main__":
    project_dir = getcwd()

    doc_dir = join(project_dir, "docs")

    api_ref_dir = join(doc_dir, "API Reference")
    pyclasher_dir = join(project_dir, "pyclasher")

    shutil.rmtree(api_ref_dir, ignore_errors=True)

    makedirs(api_ref_dir)

    create_markdown_structure(pyclasher_dir, api_ref_dir)
    copy_contributing(project_dir, doc_dir)
