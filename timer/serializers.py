from rest_framework import serializers
from timer.models import TimeEntry, Profile

class TimeEntrySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = TimeEntry
        fields = ['id', 'title', 'description', 'start_time', 'duration', 'profile']
        
class ProfileSerializer(serializers.ModelSerializer):
    
    model = Profile
    fields = ['id', 'name', 'description']    
        
        