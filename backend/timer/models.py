from django.db import models
from django.utils import timezone
# Create your models here.

class Timer(models.Model):
    name = models.CharField(max_length=50)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    #remain_time = models.DateTimeField()
    #rt = models.IntegerField(default=0)

    def __str__(self):
        return self.name