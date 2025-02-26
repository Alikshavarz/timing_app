from rest_framework import serializers
from .models import CustomUser

class UserSerializer(serializers.ModelSerializer):
    device_id = serializers.CharField(write_only=True, required=True)
    
    class Meta:
        model = CustomUser
        fields = ('id_user', 'username', 'created_at', 'device_id')
        read_only_fields = ('id_user', 'username', 'created_at')


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id_user', 'username', 'email', 'first_name', 'last_name', 'created_at']

        read_only_fields = ['created_at']
