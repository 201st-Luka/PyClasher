import os
import shutil


def get_project_dir() -> str:
    return "/" + os.getcwd().strip("docs/doc_autogen.py")


def create_markdown_structure(package_path, output_path):
    """
    Create a directory structure mirroring the Python package structure, with
    markdown files containing '::: pyclasher.path.filename' for each module.

    Args:
        package_path (str): The path to the Python package.
        output_path (str): The path where the directory structure and markdown files will be generated.
    """
    for dirpath, dirnames, filenames in os.walk(package_path):
        relative_dir = os.path.relpath(dirpath, package_path)
        output_dir = os.path.join(output_path, relative_dir)
        os.makedirs(output_dir, exist_ok=True)

        for filename in filenames:
            if filename.endswith('.py') and filename != "__init__.py":
                module_name = os.path.splitext(filename)[0]
                import_path = (
                        "pyclasher." +
                        os.path.join(relative_dir if relative_dir != '.'
                                     else '',
                                     module_name)
                ).replace('/', '.')
                markdown_content = f"::: {import_path}\n"

                markdown_file_path = os.path.join(output_dir,
                                                  f"{module_name}.md")

                with open(markdown_file_path, 'w') as markdown_file:
                    print(f"Creating docs for {import_path}")
                    markdown_file.write(markdown_content)


if __name__ == '__main__':
    project_dir = get_project_dir()

    doc_dir = os.path.join(project_dir, "docs")

    api_ref_dir = os.path.join(doc_dir, "docs/API Reference")
    pyclasher_dir = os.path.join(project_dir, "pyclasher")

    shutil.rmtree(api_ref_dir)

    os.mkdir(api_ref_dir)

    create_markdown_structure(pyclasher_dir, api_ref_dir)
