from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Users

class UsersModelSerializer(ModelSerializer):
    class Meta:
        model = Users
        fields = ('id', 'email', 'username', 'firstname', 'lastname')