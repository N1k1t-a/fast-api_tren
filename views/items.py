from fastapi import APIRouter
from pydantic import BaseModel, constr

router = APIRouter(prefix="/items", tags=["Items"])


class ItemCreate(BaseModel):
    name: constr(min_length=1, max_length=30)


@router.get("/")
def items_list():
    return {
        "data": [
            {"id": 1, "name": "foo"},
            {"id": 2, "name": "bar"},
        ]
    }


@router.post("/")
def create_item(item_in: ItemCreate):
    return {
        "data": {
            "id": 0,
            "name": item_in.name,
        },
        "raw": item_in.model_dump(),
    }


@router.get("/{item_id}")
def get_item(item_id: int):
    return {
        "data": {
            "id": item_id,
            "name": f"item {item_id}",
        }
    }
