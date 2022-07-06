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
    csv = ".csv"
    json = ".json"
    xlsx = ".xlsx"


def write_file(file_name: str, content: dict) -> bool:
    """
    Returns True if the file has been written. False if not.
    Parameters:
        - file_name: an existent file name in /docs
        - content: dictionary to be included in a given file_name

    example: write_file(file_name='users.csv', content={'user': 'peter'...})
    """

    # same as: file_path = "your/path/python-tasks-automation/files/file_name.something
    file_path = Path() / "docs" / file_name
    LOGGER.debug("%s.write_file.path: %s", __name__, file_path)
    LOGGER.info("file type: %s", file_path.suffix)

    if file_path.suffix == Files.csv:
        return write_csv(file_path, content)

    if file_path.suffix == Files.json:
        return write_json(file_path, content)

    if file_path.suffix == Files.xlsx:
        return write_xls(file_path, content)

    raise TypeError(
        f"error: file type: {file_path.suffix} not valid. Allowed values: (csv, json, xls)"
    )


def write_csv(file_path: str, content: dict):
    try:
        updated = False
        with open(file_path, mode="a") as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=content.keys())
            writer.writerow(content)
            updated = True

    except FileNotFoundError as e:
        LOGGER.exception(str(e))

    return updated


def write_json(file_path: str, content: dict):
    try:
        updated = False
        current_content = load_json(file_path)
        with open(file_path, mode="w") as json_file:
            current_content.append(content)
            json.dump(current_content, json_file, indent=4)
            updated = True
    except FileNotFoundError as e:
        LOGGER.exception(str(e))

    return updated


def write_xls(file_path: str, content: dict):
    try:
        updated = False
        current_content = pd.read_excel(file_path)
        current_content = current_content.append(content, ignore_index=True)

        with pd.ExcelWriter(file_path, engine="openpyxl", mode="a") as writer:
            current_content.to_excel(writer, sheet_name="users", index=False)
            writer.save()
            updated = True

    except FileNotFoundError as e:
        LOGGER.exception(str(e))

    return updated


def load_json(file_path: str):
    try:
        with open(file_path) as json_file:
            return json.load(json_file)
    except (FileNotFoundError, json.decoder.JSONDecodeError) as e:
        LOGGER.exception(str(e))
