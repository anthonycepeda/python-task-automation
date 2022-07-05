from sqlmodel import Session
from pydantic.types import Optional
from app.database.crud import create_user, read_users
from app.database.models import UserCreate
from app.email import connect, send_mail
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


def add_users_to_database(users: list, db: Session):
    for user in users:
        create_user(UserCreate(**user), db)


def get_users_from_database(db: Session):
    return read_users(db)


def connect_to_mail():
    connect()


def send_report(content: Optional[dict]):
    if not content:
        content = {
            "message": "This message has been sent from Python",
            "receiver_email": "acpytest@gmail.com",
            "subject": "[Test] Universidad Europea",
        }
    return send_mail(content)
