from django.conf import settings
from django.db import models

class Projects(models.Model):
    title = models.CharField(max_length=128)
    link_rep = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)



class Todo(models.Model):
    title = models.CharField(max_length=128)
    text = models.TextField()
    date_create = models.DateField(auto_now_add=True)
    date_update = models.DateField(auto_now_add=True)
    status = models.BooleanField(default=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)