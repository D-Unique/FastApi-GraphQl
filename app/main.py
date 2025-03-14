from fastapi import FastAPI
from routes.user import user_router
from routes.auth import auth_router
from ariadne.asgi import GraphQL
from routes.graphapis.schemas import schema
import asyncio
from createtable import create_table
import uvicorn
from ariadne.asgi.handlers import GraphQLTransportWSHandler
from fastapi import FastAPI, Depends, Request
from fastapi.websockets import WebSocket
from routes.graphapis.schemas import graphql_app


api = FastAPI(
    title="Fastapi and GraphQl Api",
    description=
    """
    We implement 
    ## User endpoints
    ## Auth endpoints
    ## Payment endpoints
    """,
    summary="This Api looks into fintech and secrurity ",
    version="0.0.1"
    )
@api.get("/")
def read_root():
    return {"Welcome to Unique FastApi and GraphQl Work"}

api.include_router(user_router)
api.include_router(auth_router)
api.mount("/graphql/", graphql_app)


if __name__ == "__main__":
    asyncio.run(create_table())
    uvicorn.run("main:api", host="127.0.0.1", port=8000, reload=True)
