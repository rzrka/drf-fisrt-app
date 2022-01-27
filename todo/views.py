from django.shortcuts import render, get_object_or_404
from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet, ViewSet
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from .models import Projects, Todo
from users.models import Users
from .serializers import ProjectSerializer, TodoSerializer


class UsersPaggination(LimitOffsetPagination):
    default_limit = 10


class ProjectsModelViewSet(ViewSet):
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    permission_classes = [permissions.AllowAny]

    def list(self, request):
        title = request.query_params.get('title', '')
        projects = Projects.objects.all()
        if title:
            projects = projects.filter(title__contains=title)
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        project = get_object_or_404(Projects, pk=pk)
        serializer = ProjectSerializer(project)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        poject_data = request.data
        new_project = Projects.objects.create(
            title=poject_data['title'],
            link_rep=poject_data['link_rep'],
            user=request.user
        )
        new_project.save()

        serializer = ProjectSerializer(new_project)
        return Response(serializer.data)

    def delete(self, request, *args, **kwargs):
        project = Projects.objects.get(id=kwargs['pk'])
        project.delete()
        serializer = ProjectSerializer(project)
        return Response(serializer.data)

    def patch(self, request, *args, **kwargs):
        project_id = Projects.objects.get(id=kwargs['pk'])
        project_data = request.data
        for el in project_data:
            project_id.__dict__[el] = project_data[el]
        project_id.save()
        serializer = ProjectSerializer(project_id)
        return Response(serializer.data)


class TodoModelViewSet(ViewSet):
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request):
        title = request.query_params.get('title', '')
        todo = Todo.objects.all()
        if title:
            todo = todo.filter(title__contains=title)
        serializer = TodoSerializer(todo, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        todo = get_object_or_404(Todo, pk=pk)
        serializer = TodoSerializer(todo)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        todo_data = request.data
        new_todo = Todo.objects.create(
            title=todo_data['title'],
            text=todo_data['text'],
            user=request.user,
        )
        new_todo.save()

        serializer = TodoSerializer(new_todo)
        return Response(serializer.data, status=201)

    def delete(self, request, *args, **kwargs):
        todo = Todo.objects.get(id=kwargs['pk'])
        todo.status = False
        todo.save()
        serializer = TodoSerializer(todo)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        todo_id = Todo.objects.get(id=kwargs['pk'])
        todo_data = request.data
        for el in todo_data:
            todo_id.__dict__[el] = todo_data[el]
        todo_id.save()
        serializer = TodoSerializer(todo_id)
        return Response(serializer.data)
