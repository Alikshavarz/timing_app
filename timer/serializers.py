from django.template.context_processors import request
from rest_framework import serializers
from timer.models import Project,TimeEntry


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'title', 'description', 'user', 'created_at', 'updated_at']


class TimeEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeEntry
        fields = ['id', 'title', 'description', 'project', 'start_time', 'duration', 'created_at', 'update_time']



