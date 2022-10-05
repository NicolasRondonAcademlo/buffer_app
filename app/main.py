import pickle

import redis
from fastapi import FastAPI

from app.buffer import Buffer

app = FastAPI()


r = redis.Redis(host="cache", port=6379, db=0)


@app.post("/insert/")
def insert_item(item, policy: str, buffer_key: int = None):
    if not buffer_key:
        buffer = Buffer(policy)
        buffer.insert(item)
        pickled_object = pickle.dumps(buffer)
        buffer_key = 1
        r.set(str(buffer_key), pickled_object)
        unpacked_object = pickle.loads(r.get(str(buffer_key)))
    else:
        unpacked_object = pickle.loads(r.get(str(buffer_key)))
        unpacked_object.insert(item)
    return {
        "data": {
            "count": unpacked_object.count,
            "id": str(buffer_key),
            "policy": policy,
        }
    }


@app.get("/items/{item_id}")
def read_item(buffer_key: int):
    unpacked_object = pickle.loads(r.get(buffer_key))
    return {
        "data": {
            "count": unpacked_object.count,
            "id": str(buffer_key),
            "value": unpacked_object.extract(),
        }
    }
