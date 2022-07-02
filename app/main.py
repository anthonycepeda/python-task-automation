from pyrsistent import s
from files import reader, writer
import json
from utils.logger import set_logger

logger = set_logger(__name__)


def load_a_file():
    file_name = "users.json"

    users = reader.load_file(file_name)
    print(json.dumps(users, indent=2))


def write_a_file():
    file_name = "users.json"
    users = [
        {
            "id": 107,
            "firstname": "Alvaro",
            "lastname": "Cruz",
            "email": "alc@me.com",
            "email2": "alc2@me.com",
            "profession": "officer",
        }
    ]

    result = writer.write_file(file_name, users)

    if result:
        logger.debug("content added to file: %s", file_name)


# load_a_file()
write_a_file()
