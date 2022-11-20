from django.shortcuts import render, redirect
from rest_framework import viewsets

from .serializers import TimerSerializer
from .models import Timer

from datetime import datetime, timedelta

#d = datetime.timedelta(days =-1, seconds = 68400)
d = datetime.now()

#dt = datetime.strptime(d, "%Y-%m-%d %H:%M:%S.%F")
end_timer = d + timedelta(seconds=300)

# obj = Timer.objects.create(duration = d)
# obj.save()
'''
while True:
    remaining = endTime - current Time
    if remaining < 0:
        break
'''

def setTime():
    set_end = Timer.objects.create(name="oken",end_time=end_timer, start_time=d)
    set_end.save()


def cal():
    endTimer = Timer.objects.get(end_time)
    remaining = endTimer - d

class TimerView(viewsets.ModelViewSet):
    serializer_class = TimerSerializer
    queryset = Timer.objects.all()





def index(request):
    return render(request, 'timer/index.html')
