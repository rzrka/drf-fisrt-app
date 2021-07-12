from django.db import models

class Users(models.Model):
    email = models.EmailField()
    username = models.CharField(max_length=64, default='user')
    firstname = models.CharField(max_length=64, default='user')
    lastname = models.CharField(max_length=64, default='user')