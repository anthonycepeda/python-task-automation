from pyrsistent import s
from app.files import reader, writer
import json
from app.utils.logger import set_logger

logger = set_logger(__name__)


def load_a_file():
    file_name = "users.json"

    users = reader.load_file(file_name)
    logger.debug("%s.load_a_file.users: %s", __name__, json.dumps(users, indent=2))


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
    logger.debug("%s.write_a_file.%s - updated: %s", __name__, file_name, result)


# load_a_file()
# write_a_file()
