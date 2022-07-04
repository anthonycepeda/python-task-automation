from typing import Optional

from pydantic.types import Optional
from sqlmodel import Field, SQLModel


class UserBase(SQLModel):
    name: Optional[str]
    email: Optional[str]
    profession: Optional[str]

    class Config:
        inherit_cache = False


class User(UserBase, table=True):
    uid: Optional[int] = Field(default=None, primary_key=True)


class UserCreate(UserBase):
    pass


class UserRead(UserBase):
    id: int
