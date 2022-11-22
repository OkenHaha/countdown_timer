from django.shortcuts import render, redirect
from rest_framework import viewsets
from rest_framework.views import APIView
from .serializers import TimerSerializer
from .models import Timer

# from datetime import datetime, timedelta

# d = datetime.timedelta(days =-1, seconds = 68400)
# d = datetime.now()

# #dt = datetime.strptime(d, "%Y-%m-%d %H:%M:%S.%F")
# end_timer = d + timedelta(seconds=300)


# def setTime():
#     set_end = Timer.objects.create(name="oken",end_time=end_timer, start_time=d)
#     set_end.save()

# remaining = Timer.objects.create(rt=end_timer - d.strftime("%Y-%m-%d %H:%M:%S.%F"))
# remaining.save()

# def cal():
#     endTimer = Timer.objects.get(end_time)
#     remaining = Timer.objects.create(remain_time=endTimer - d)
#     remaining.save()
#     if remaining <= 0:
#         #remaining = Timer.objects.get(remain_time)
#         remaining.delete()

# setV = Timer.objects.create(rt=20)
# setV.save()

class TimerView(viewsets.ModelViewSet):
    serializer_class = TimerSerializer
    queryset = Timer.objects.all()





def index(request):
    getV = Timer.objects.all()
    context = {'getV':Timer.objects.all()}
    return render(request, 'timer/index.html',context)
