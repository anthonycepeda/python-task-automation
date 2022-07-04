import json
from textwrap import indent

from app.database.crud import create_user, read_users
from app.database.models import UserCreate
from app.files import reader, writer
from app.utils.logger import set_logger

logger = set_logger(__name__)


def load_a_file():
    file_name = "users.json"

    users = reader.load_file(file_name)
    logger.debug("%s.load_a_file.users: %s", __name__, len(users))

    return users


def write_a_file():
    file_name = "users.json"
    users = [
        {
            "name": "Alvaro",
            "email": "alc@me.com",
            "profession": "officer",
        }
    ]

    result = writer.write_file(file_name, users)
    logger.debug("%s.write_a_file.%s - updated: %s", __name__, file_name, result)

    return result


def add_users_to_database(users: list):
    for user in users:
        create_user(UserCreate(**user))


def get_users_from_database():
    users = read_users()

    for user in users:
        print(user, "\n")
