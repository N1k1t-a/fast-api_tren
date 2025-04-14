from fastapi import APIRouter

from . import crud
from .schemas import User, UserIn

router = APIRouter(prefix="/users", tags=["Users"])


@router.get("")
def get_users() -> list[User]:
    return crud.get_users()


@router.post("")
def create_user(user_in: UserIn) -> User:
    return crud.create_user(user_in)


@router.get("/{user_id}")
def get_user(user_id: int) -> User | None:
    return (crud.get_user(user_id))


@router.delete("/{user_id}")
def delete_user(user_id: int) -> None:
    return crud.delete_user(user_id)
