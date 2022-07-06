from pathlib import Path

from sqlmodel import Session, SQLModel, create_engine

connect_args = {"check_same_thread": False}

db_path = Path() / "docs" / "user.db"
engine = create_engine(f"sqlite:///{db_path}", echo=True, connect_args=connect_args)


def create_database_tables():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        return session
