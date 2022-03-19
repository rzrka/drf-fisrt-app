"""service URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from graphene_django.views import GraphQLView
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
from users.views import UsersModelViewSet, UserModelViewSet
from todo.views import ProjectsModelViewSet, TodoModelViewSet

from mainapp.views import AuthorViewSet, BookViewSet

router = DefaultRouter()
router.register('projects', ProjectsModelViewSet, basename='projects')
router.register('todo', TodoModelViewSet, basename='todo')

router.register('authors', AuthorViewSet)
router.register('books', BookViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('', include(router.urls)),
    #users
    path('users/', UsersModelViewSet.as_view()),
    path('user/<int:pk>', UserModelViewSet.as_view()),
    path('api-token-auth/', views.obtain_auth_token),
    path("graphql/", GraphQLView.as_view(graphiql=True)),
]
