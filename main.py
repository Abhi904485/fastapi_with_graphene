from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from starlette_graphene3 import GraphQLApp, make_graphiql_handler

from schema import todo_schema

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.mount("/", GraphQLApp(schema=todo_schema, on_get=make_graphiql_handler()))


@app.get("/")
def read_root():
    return {"message": "Welcome to the Todo API!"}
