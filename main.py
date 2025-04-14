import json


from fastapi import FastAPI, Response
from views.items import router as items_router
from views.users import router as user_router


app = FastAPI()
app.include_router(items_router)
app.include_router(user_router)


@app.get("/")
def read_root():
    return {"hello": "root"}


# тут так можно набирать http://127.0.0.1:8000/hello?name=Sergey
@app.get("/hello")
def hello_default(name: str = "OTUS"):
    return {"message": f"hello {name}"}


# вот так можно писать адрес тут http://127.0.0.1:8000/hello/name/hyesos
@app.get("/hello/name/{name}")
def hello_with_name(name: str):
    return {"message": f"hello {name}"}


