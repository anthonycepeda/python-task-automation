import csv
import json
from asyncio.log import logger
from pathlib import Path

import pandas as pd
from pydantic.types import Enum, List

from app.utils.logger import set_logger

LOGGER = set_logger(__name__)


class OpenMode(str, Enum):
    append = "a"
    read = "r"
    truncate = "w"


class Files(str, Enum):
    csv = "csv"
    json = "json"
    xls = "xls"


def write_file(file_name: str, content: List[dict]):
    """
    This funct. write a given content in a file based on its path and type
    example: write_file(file_name='users.csv')
    """
    file_type = _get_file_type(file_name)

    # same as: file_path = "your/path/python-tasks-automation/files/file_name
    file_path = Path() / "app" / "files" / "docs" / file_name

    LOGGER.info("file_type: %s", file_type)
    if file_type == Files.csv:
        return write_csv(file_path, content)

    if file_type == Files.json:
        return write_json(file_path, content)

    if file_type == Files.xls:
        return write_xls(file_path, content)

    return f"error: file_type: {file_type} not valid. Allowed values: (csv, json, xls)"


def write_csv(file_path: str, content: List[dict]):
    try:
        with open(file_path, mode="a") as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=content[0].keys())
            writer.writerows(content)
            return True

    except FileNotFoundError as e:
        LOGGER.exception(str(e))


def write_json(file_path: str, content: List[dict]):
    try:
        updated = False
        current_content = load_json(file_path)
        with open(file_path, mode="w") as json_file:
            current_content.extend(content)

            json.dump(current_content, json_file, indent=4)
            updated = True
    except FileNotFoundError as e:
        LOGGER.exception(str(e))

    return updated


def write_xls(file_path: str):
    try:
        return pd.read_excel(file_path).to_dict(orient="records")
    except FileNotFoundError as e:
        LOGGER.exception(str(e))


def load_json(file_path: str):
    try:
        with open(file_path) as json_file:
            return json.load(json_file)
    except FileNotFoundError as e:
        LOGGER.exception(str(e))


def _get_file_type(file_name: str):
    return file_name.split(".")[-1]
