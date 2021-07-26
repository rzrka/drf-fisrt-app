from rest_framework.serializers import HyperlinkedModelSerializer

from .models import Projects, Todo
from users.serializers import UsersModelSerializer

class ProjectSerializer(HyperlinkedModelSerializer):
    users = UsersModelSerializer()


    class Meta:
        model = Projects
        fields = '__all__'

class TodoSerializer(HyperlinkedModelSerializer):
    users = UsersModelSerializer()

    
    class Meta:
        model = Todo 
        fields = '__all__'