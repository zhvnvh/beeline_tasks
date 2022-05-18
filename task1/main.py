from fastapi import FastAPI, Request
import json
from Storage import FileStorage
import uuid
import os

filename = os.getenv('APP_FILE', default='file.json')


app = FastAPI()

storage = FileStorage(filename)

@app.get("/")
async def get_all():
    return storage.get_all()

@app.post("/")
async def add(request:Request):
    data = await request.json()
    data['id'] = str(uuid.uuid4())
    storage.save(data)
    return {
        "id": data['id']
    }


@app.delete("/{id}")
async def delete(id):
    storage.delete(id)
    return {
        "message" : "Ok"
    }

@app.put("/{id}")
async def update(id, request:Request):
    data = await request.json()
    storage.update(id, data)
    return {
        "message" : "Ok"
    }

