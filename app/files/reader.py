import csv
import json
from pathlib import Path

import pandas as pd

from pydantic.types import Enum

from app.utils.logger import set_logger

LOGGER = set_logger(__name__)


class Files(str, Enum):
    csv = "csv"
    json = "json"
    xls = "xls"


def load_file(file_name: str):
    """
    This funct. loads a file based on its path and type
    example: load_file(file_name='users.csv')
    """
    file_type = _get_file_type(file_name)
    LOGGER.debug("%sload_file.type: %s", __name__, file_type)

    file_path = Path() / "app" / "files" / "docs" / file_name
    LOGGER.debug("%sload_file.path: %s", __name__, file_path)

    if file_type == Files.csv:
        return load_csv(file_path)

    if file_type == Files.json:
        return load_json(file_path)

    if file_type == Files.xls:
        return load_xls(file_path)

    return f"error: file_type: {file_type} not valid. Allowed values: (csv, json, xls)"


def load_csv(file_path: str):
    try:
        with open(file_path) as csv_file:
            csv_reader = csv.DictReader(csv_file, delimiter=",")
            file_content = []

            for row in csv_reader:
                file_content.append(row)

            return file_content

    except FileNotFoundError as e:
        LOGGER.exception(str(e))


def load_json(file_path: str):
    try:
        with open(file_path) as json_file:
            return json.load(json_file)
    except FileNotFoundError as e:
        LOGGER.exception(str(e))


def load_xls(file_path: str):
    try:
        return pd.read_excel(file_path).to_dict(orient="records")
    except FileNotFoundError as e:
        LOGGER.exception(str(e))


def _get_file_type(file_name: str):
    return file_name.split(".")[-1]


# users = load_file("users.json")
# users = load_file("users.csv")
# users = load_file("users.xls")

# print(json.dumps(users, indent=2))
