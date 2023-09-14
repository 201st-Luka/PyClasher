# Contributing

Contributing to this open-source project is appreciated. To contribute please 
visit the Discord server as well.

---

## Where to start

The contribution starts with an issue. The created issue should explain what to
do. Based on this issue you can start contributing. If so, refer to the issue in
the pull request. 

### Issues

The issues must follow these guidelines:
- An issue must not be a duplicate of an existing issue.
- A bug issue must provide clear information about the bug.
- A feature request should contain information about what the feature should do
and what it serves.

Irrelevant issues, duplicates or issues failing to comply to these guidelines 
will be closed. 

### Pull requests

After solving the issue it is possible to create a pull request. This pull 
request must target the `unstable` branch. From there it will be part of the bot 
in the next release.

Requirements for a pull request are:
- Commits must be clear
- The pull request must be up-to-date with the `stable` branch
- All checks (if applicable) must pass
- A review must be requested from at least one developer (201st-Luka)

### Recognising the contribution

When the PR is merged in the `stable` branch. GitHub will automatically add the 
user to the repository's contributor list. It is also possible to earn a role 
on the Discord server for contribution.

---

## Installation

1. Fork the repository and copy it to your local machine.
2. Install the requirements:
   - for developing:
     - [aiohttp](https://pypi.org/project/aiohttp/) (`pip install aiohttp`)
     
     You can simply do 
     ```bash
     pip install -r requirements.txt
     ```
  - for testing:
    - [aiohttp](https://pypi.org/project/aiohttp/) (`pip install aiohttp`)
    - [pytest](https://pypi.org/project/pytest/) (`pip install pytest`)
    - [pytest-asyncio](https://pypi.org/project/pytest-asyncio/) 
(`pip install pytest-asyncio`)
    You can simply do
    ```bash
    pip install -r requirements-tests.txt
    ```
  - for creating the documentation:
    - [mkdocs](https://pypi.org/project/mkdocs/) (`pip install mkdocs`)
    - [mkdocs-material](https://pypi.org/project/mkdocs-material/) 
(`pip install mkdocs-material`)
    - [mkdocstrings[python]](https://pypi.org/project/mkdocstrings/) 
(`pip install mkdocstrings[python]`)
    - [mkdocs-awesome-pages-plugin](https://pypi.org/project/mkdocs-awesome-pages-plugin/) 
(`pip install mkdocs-awesome-pages-plugin`)
    You can simply do
    ```bash
    pip install -r requirements-docs.txt
    ```
  In total, you should have installed 7 packages.

---

You're done! Happy coding.
