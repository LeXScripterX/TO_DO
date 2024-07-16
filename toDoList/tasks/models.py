from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    TASK_STATUS = [
        ('pending', 'Pendiente'),
        ('Completed', 'Cpmpletado'),
        ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    creation_date = models.DateTimeField(auto_created=True)
    status = models.CharField(max_length=20,choices=TASK_STATUS,default='pendiente')


def __str__(self):
    return self.title