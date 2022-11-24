from rest_framework import serializers

from .models import Timer

class TimerSerializer(serializers.ModelSerializer):
	class Meta:
		model = Timer
		fields = ('name', 'start_time', 'end_time')


class CreateTimeSerializer(serializers.ModelSerializer):
	class Meta:
		model = Timer
		fields = ('start_time', 'end_time')
