from pydantic import BaseModel
from datetime import datetime


class User(BaseModel):
    id: int
    name: str = "ALisa Psheno"
    signup_ts: datetime | None = None
    friends: list[int] = []


external_data = {
    "id": "123",
    "signup_ts": str(datetime.now()),
    "friends": [1, "2", b"3"],
}

user = User(**external_data)  # ** перед словарём преобразует пары "ключ-значение" из словаря в именованные аргументы.
print(user)
print(user.id)