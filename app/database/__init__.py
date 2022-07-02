from pathlib import Path
from typing import Optional

from pydantic import BaseModel
from sqlmodel import Field, Session, SQLModel, create_engine

file_path = Path() / "users.db"
engine = create_engine(f"sqlite:///{file_path}")


class UserRead(BaseModel):
    uid: Optional[int]
    name: Optional[str]
    email: Optional[str]
    profession: Optional[str]


class User(SQLModel, table=True):
    uid: Optional[int] = Field(default=None, primary_key=True)
    name: str
    email: str
    profession: Optional[str] = None


def create_db_and_tables():
    SQLModel.metadata.create_all()


def get_session():
    with Session(engine) as session:
        yield session
