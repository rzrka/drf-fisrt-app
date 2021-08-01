from django.shortcuts import render, get_object_or_404
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework.viewsets import ModelViewSet, ViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Users
from .serializers import UsersModelSerializer

class UsersPaggination(LimitOffsetPagination):
    default_limit = 3

class UsersModelViewSet(APIView):
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    pagination_class = UsersPaggination

    def get(self, request, format=None):
        users = Users.objects.all()
        paginator = UsersPaggination()
        result_page = paginator.paginate_queryset(users, request)
        serializer = UsersModelSerializer(result_page, many=True)
        return Response(serializer.data)


class UserModelViewSet(APIView):
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    serializer = UsersModelSerializer

    def get(self, request, pk=None):
        user = get_object_or_404(Users, id=pk)
        serializer = UsersModelSerializer(user)
        return Response(serializer.data)


    def post(self, request, *args, **kwargs):
        user_data = request.data
        new_user = Users.objects.create(
            email=user_data['email'],
            username=user_data['username'],
            firstname=user_data['firstname'],
            lastname=user_data['lastname'],
        )
        new_user.save()

        serializer = UsersModelSerializer(new_user)
        return Response(serializer.data)

    def patch(self, request, *args, **kwargs):
        user = Users.objects.get(id=kwargs['pk'])
        response = request.data
        for el in response:
            user.__dict__[el] = response[el]
        user.save()
        serializer = UsersModelSerializer(user)
        return Response(serializer.data)




