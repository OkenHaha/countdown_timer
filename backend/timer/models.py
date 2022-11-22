from django.db import models
from django.utils import timezone
# Create your models here.

class Timer(models.Model):
    name = models.CharField(max_length=50 ,null=True)
    #start_time = models.DateTimeField(null=True)
    #end_time = models.DateTimeField(null=True)
    #remain_time = models.DateTimeField()
    rt = models.IntegerField(default=0)

    def __str__(self):
        return self.name