from django.db import models
from django.contrib.auth.models import AbstractUser


class Users(AbstractUser):
    email = models.EmailField(default='email@email.com', blank=True)
    username = models.CharField(max_length=64, unique=True)