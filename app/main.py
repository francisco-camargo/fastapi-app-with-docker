from typing import Union

from fastapi import FastAPI
import redis

app = FastAPI()

r = redis.Redis(host='redis-container', port=6379)


@app.get("/")
def front_page():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.get("/hits")
def read_root():
    r.set("foo", "bar")
    r.incr("hits")
    return {"Number of hits:": r.get("hits"), "foo": r.get("foo")}
