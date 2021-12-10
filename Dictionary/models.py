from django.db import models
from Authentication.models import UserInfo


# Create your models here.

class History(models.Model):
    userId = models.ForeignKey(UserInfo, on_delete=models.CASCADE)
    username = models.CharField(max_length=100)
    history = models.CharField(max_length=100)
    query_time = models.DateTimeField()

    def __str__(self):
        return self.userId
