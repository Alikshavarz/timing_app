from rest_framework import serializers
from timer.models import TimeEntry


class TimeEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeEntry
        fields = ['id', 'title', 'user', 'description', 'start_time', 'duration']