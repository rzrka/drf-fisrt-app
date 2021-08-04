from rest_framework.serializers import HyperlinkedModelSerializer
from rest_framework.serializers import ModelSerializer
from .models import Projects, Todo
from users.serializers import UsersModelSerializer

class ProjectSerializer(ModelSerializer):
    users = UsersModelSerializer()

    class Meta:
        model = Projects
        fields = '__all__'

class TodoSerializer(ModelSerializer):
    users = UsersModelSerializer()

    class Meta:
        model = Todo 
        fields = '__all__'