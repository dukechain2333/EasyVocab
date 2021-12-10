from django.db import models
from django.utils import timezone


# Create your models here.

class UserInfo(models.Model):
    username = models.CharField(max_length=150)
    password = models.CharField(max_length=150)
    email = models.EmailField()
    register_time = models.DateTimeField(default=timezone.now, )

    def __str__(self):
        return self.username
