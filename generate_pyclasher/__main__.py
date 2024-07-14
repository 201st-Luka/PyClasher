from argparse import ArgumentParser
from asyncio import run
from os import environ, makedirs
from os.path import exists
from shutil import rmtree
from tempfile import NamedTemporaryFile

from yaml import safe_load

from . import get_yaml, generate

if __name__ == '__main__':
    parser = ArgumentParser(
        prog="generate_pyclasher",
        description="Generate the API models of the Clash of Clans API wrapper",
        epilog="The generated models are placed in the 'generated' directory",
    )
    parser.add_argument("--path", help="The path to the generated directory", required=True)
    parser.add_argument("-e", "--email", help="The email address of the Clash of Clans developer account")
    parser.add_argument("-p", "--password", help="The password of the Clash of Clans developer account")

    parsed_args = parser.parse_args()

    generate_path = parsed_args.path

    email, password = environ.get("EMAIL") or parsed_args.email, environ.get("PASSWORD") or parsed_args.password

    if not email:
        exit("Email is required, provide it as an argument or as an environment variable ('EMAIL').")
    if not password:
        exit("Password is required, provide it as an argument or as an environment variable ('PASSWORD').")

    with NamedTemporaryFile("w", encoding="utf-8", delete_on_close=False) as tmp_file:
        run(get_yaml(email, password, tmp_file.name))
        tmp_file.close()

        if exists(generate_path):
            rmtree(generate_path)
        makedirs(generate_path)

        with open(tmp_file.name, "r", encoding="utf-8") as file:
            yaml_file = safe_load(file)

        generate(yaml_file, generate_path)
