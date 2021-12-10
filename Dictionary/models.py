from django.db import models
from django.utils import timezone


# Create your models here.

class History(models.Model):
    userId = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    history = models.CharField(max_length=100)
    query_time = models.DateTimeField(default=timezone.now, )

    def __str__(self):
        return self.userId
