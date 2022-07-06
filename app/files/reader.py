import csv
import json
from pathlib import Path

import pandas as pd
from pydantic.types import Enum

from app.utils.logger import set_logger

LOGGER = set_logger(__name__)


class Files(str, Enum):
    csv = ".csv"
    json = ".json"
    xls = ".xlsx"


def load_file(file_name: str):
    """
    Returns a list of dictionaries with the content of a file
    Parameter: file_name

    Example: load_file('users.json')

    """
    file_path = Path() / "docs" / file_name
    LOGGER.debug("%sload_file.path: %s", __name__, file_path)
    LOGGER.debug("%sload_file.type: %s", __name__, file_path.suffix)

    if file_path.suffix == Files.csv:
        return load_csv(file_path)

    if file_path.suffix == Files.json:
        return load_json(file_path)

    if file_path.suffix == Files.xls:
        return load_xls(file_path)

    raise TypeError(
        f"error: file type: {file_path.suffix} not valid. Allowed values: (csv, json, xls)"
    )


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
