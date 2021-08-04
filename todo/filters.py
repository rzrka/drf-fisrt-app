from django_filters import rest_framework as filters

from .models import Projects, Todo

class ProjectsFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='contains')

    class Meta:
        model = Projects
        fields = ['title']