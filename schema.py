import graphene
from graphene import ObjectType, List, Mutation, String, Schema

from database import session
from models import Todo


class TodoType(ObjectType):
    id = graphene.Int()
    title = graphene.String()
    description = graphene.String()


# Define a basic query class
class Query(ObjectType):
    todos = List(TodoType)

    def resolve_todos(self, info):
        todos = session.query(Todo).all()
        return todos


class CreateTodoMutation(Mutation):
    class Arguments:
        title = String()
        description = String()

    todo = graphene.Field(TodoType)

    def mutate(self, info, title, description):
        todo = Todo(title=title, description=description)
        session.add(todo)
        session.commit()
        return CreateTodoMutation(todo=todo)


class Mutation(ObjectType):
    create_todo = CreateTodoMutation.Field()


todo_schema = Schema(query=Query, mutation=Mutation)
