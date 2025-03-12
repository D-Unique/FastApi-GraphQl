from fastapi import FastAPI
import asyncio
from createtable import create_table
import uvicorn

api = FastAPI()

@api.get("/")
def read_root():
    return {"Day 1"}

@api.get("/users")
def get_user():
    return {"Note": "Welcome to Day 1"}


if __name__ == "__main__":
    asyncio.run(create_table())
    uvicorn.run("main:api", host="127.0.0.1", port=8000, reload=True)
