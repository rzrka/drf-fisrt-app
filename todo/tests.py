import json
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIRequestFactory, force_authenticate, APIClient, APISimpleTestCase, APITestCase
from mixer.backend.django import mixer

from users.models import Users
from .models import Todo, Projects
from .views import TodoModelViewSet, ProjectsModelViewSet


class TestTodoViewSet(TestCase):

    def setUp(self):
        self.admin = Users.objects.create_superuser('admin', 'admin')
        return 0

    def test_get_list(self):
        factory = APIRequestFactory()
        request = factory.get('/todo/')
        force_authenticate(request, self.admin)
        view = TodoModelViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_retrieve(self):
        client = APIClient()
        todo = Todo.objects.create(title='test', text='test', user=self.admin)
        client.force_authenticate(self.admin)
        response = client.get(f'/todo/{todo.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_todo(self):
        factory = APIRequestFactory()
        request = factory.post('/todo/', {"title": "todo2", "text": "todo2"}, format='json')
        view = TodoModelViewSet.as_view(actions={'post': 'create'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_todo(self):
        factory = APIRequestFactory()
        request = factory.post('/todo/', {"title": "todo2", "text": "todo2"}, format='json')
        force_authenticate(request, self.admin)
        view = TodoModelViewSet.as_view(actions={'post': 'create'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_todo(self):
        factory = APIRequestFactory()
        todo = Todo.objects.create(title='test', text='test', user=self.admin)
        request = factory.patch('/todo/', {"title": "todo1", "text": "todo1"}, format='json')
        force_authenticate(request, self.admin)
        view = TodoModelViewSet.as_view(actions={'patch': 'update'})
        response = view(request, pk=todo.id)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'todo1')
        self.assertEqual(response.data['text'], 'todo1')
