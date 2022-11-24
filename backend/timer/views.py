from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import TimerSerializer, CreateTimeSerializer
from .models import Timer
# from datetime import datetime, timedelta
# import time as tm

from datetime import datetime, timedelta

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

# time_format = "%H:%M:%S"

# def to_dt(dateTime):
#     dateDT = datetime.strptime(dateTime, fr_data)   
#     return dateDT



# class TimerView(viewsets.ModelViewSet):
#     serializer_class = TimerSerializer
#     queryset = Timer.objects.all()


def index(request):
    return render(request, 'timer/index.html')


# class TimerView(APIView):
#     serializer_class = CreateTimeSerializer
#     def post(self, request, format=None):
#         pass

class TimerView(APIView):
    def get(self, request, pk=None, format=None):
        queryset = Timer.objects.all()
        serializer = TimerSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        d = datetime.now()
        endT = d + timedelta(seconds=3)
        set_time = Timer.objects.create(name="hi",start_time=d,end_time=endT)
        
        serializer = TimerSerializer(data=set_time)
        if serializer.is_valid():
            serializer.save()
        return Response("Posted successfully")

