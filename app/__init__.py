from sqlmodel import Session
from pydantic.types import Optional
from app.database.crud import create_user, read_users
from app.database.models import UserCreate
from app.email import connect, send_mail
from app.files import reader, writer
from app.utils.logger import set_logger

logger = set_logger(__name__)


def load_file(file_name: str = "users.json"):
    users = reader.load_file(file_name)
    logger.debug("%s.load_file.users: %s", __name__, len(users))

    return users


def add_user_to_file(user: UserCreate, file_name: str = "users.json"):
    result = writer.write_file(file_name, user)
    logger.debug("%s.add_user_to_file.%s - updated: %s", __name__, file_name, result)

    return result


def add_users_to_database(users: list, db: Session):
    for user in users:
        create_user(UserCreate(**user), db)


def get_users_from_database(db: Session):
    return read_users(db)


def send_report(content: Optional[dict]):
    if not content:
        content = {
            "message": "This message has been sent from Python",
            "receiver_email": "acpytest@gmail.com",
            "subject": "[Test] Universidad Europea",
        }
    return send_mail(content)
