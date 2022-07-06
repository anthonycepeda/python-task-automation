from pydantic.types import Optional, Enum
from sqlmodel import Field, SQLModel


class Cities(str, Enum):
    madrid = "madrid"
    roma = "roma"
    london = "london"
    paris = "paris"
    alicante = "alicante"
    lisbon = "lisbon"
    santo_domingo = "santo domingo"
    barcelona = "barcelona"


class UserBase(SQLModel):
    name: Optional[str]
    email: Optional[str]
    profession: Optional[str]
    city: Optional[Cities]
    vehicule: Optional[bool]
    since: Optional[str]

    class Config:
        inherit_cache = False


class User(UserBase, table=True):
    uid: Optional[int] = Field(default=None, primary_key=True)

    __table_args__ = {"extend_existing": True}


class UserCreate(UserBase):
    pass


class UserUpdate(UserBase):
    pass


class UserRead(UserBase):
    id: int
