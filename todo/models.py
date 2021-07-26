from django.db import models


from users.models import Users

class Projects(models.Model):
    title = models.CharField(max_length=128)
    link_rep = models.TextField()
    users = models.ForeignKey(Users, on_delete=models.CASCADE)



class Todo(models.Model):
    title = models.CharField(max_length=128)
    text = models.TextField()
    date_create = models.DateField(auto_now_add=True)
    date_update = models.DateField(auto_now_add=True)
    status = models.BooleanField(default=True)
    users = models.ForeignKey(Users, on_delete=models.CASCADE)