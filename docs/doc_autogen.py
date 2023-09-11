import os


def get_project_dir() -> str:
    return "/" + os.getcwd().strip("docs/doc_autogen.py")


if __name__ == '__main__':
    project_dir = get_project_dir()

    doc_dir = os.path.join(project_dir, "docs")

    api_ref_dir = os.path.join(doc_dir, "API Reference")
    api_dir = os.path.join(project_dir, "pyclasher", "api")

    print(os.listdir(),
          os.listdir(project_dir),
          os.listdir(doc_dir),
          os.listdir(api_ref_dir),
          os.listdir(api_dir),
          sep="\n")

