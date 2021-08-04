from django.shortcuts import render, get_object_or_404
from rest_framework.viewsets import ModelViewSet, ViewSet
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response

from .models import Projects, Todo
from .serializers import ProjectSerializer, TodoSerializer
from .filters import ProjectsFilter




class UsersPaggination(LimitOffsetPagination):
    default_limit = 10


class ProjectsModelViewSet(ViewSet):
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    filterset_class = ProjectsFilter

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
            users_id=51
        )
        new_project.save()

        serializer = ProjectSerializer(new_project)
        return Response(serializer.data)


    def patch(self, request, *args, **kwargs):
        project_id = Projects.objects.get(id=kwargs['pk'])
        project_data = request.data
        for el in project_data:
            project_id.__dict__[el] = project_data[el]
        project_id.save()
        serializer = ProjectSerializer(project_id)
        return Response(serializer.data)

class TodoModelViewSet(ModelViewSet):
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer 