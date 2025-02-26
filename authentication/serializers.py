from rest_framework import serializers
from .models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id_user', 'username', 'email', 'first_name', 'last_name', 'created_at']

        read_only_fields = ['created_at']