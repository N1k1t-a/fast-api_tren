from pydantic import BaseModel


class UserBase(BaseModel):
    username: str


class User(UserBase):
    id: int


class UserIn(UserBase):
    pass