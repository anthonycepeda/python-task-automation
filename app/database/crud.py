from sqlmodel import Session, select

from app.database import create_tables, get_session
from app.database.models import User, UserCreate, UserRead


def create_user(user: UserCreate, db: Session):
    user_to_db = User.from_orm(user)
    db.add(user_to_db)
    db.commit()
    db.refresh(user_to_db)
    return user_to_db


def read_users(db: Session):
    users = db.exec(select(User)).all()
    users = [user.dict() for user in users]
    return users


def read_user(user_id: int, db: Session):
    user = db.get(User, user_id)
    if user:
        return user
