import graphene
from graphene_django import DjangoObjectType
from todo.models import Projects, Todo


class TodoType(DjangoObjectType):
    class Meta:
        model = Todo
        fields = '__all__'


class Query(graphene.ObjectType):
    all_todos = graphene.List(TodoType)

    def resolve_all_todos(root, info):
        return Todo.objects.all()


schema = graphene.Schema(query=Query)



