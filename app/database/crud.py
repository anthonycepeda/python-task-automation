from sqlmodel import Session, select

from app.database import create_database_tables
from app.database.models import User, UserCreate, UserRead, UserUpdate


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


def read_user(uid: int, db: Session):
    user = db.get(User, uid)
    if user:
        return user


def update_user(user: UserUpdate, db: Session):
    user_to_update = read_user(user.uid, db)
    if user_to_update:
        # user will be updated here
        pass


def delete_user():
    # TODO
    pass
