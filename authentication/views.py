import uuid
import string
import random
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import UserSerializer
from .models import CustomUser

def generate_random_password(length=12):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

class AuthView(APIView):
    def post(self, request):
        device_id = request.data.get('device_id')

        if not device_id:
            return Response({
                'error': 'device_id is required'
            }, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = CustomUser.objects.get(username=device_id)
            is_new_user = False
        except CustomUser.DoesNotExist:
            password = generate_random_password()
            user = CustomUser.objects.create_user(
                username=device_id,
                password=password
            )
            is_new_user = True

        refresh = RefreshToken.for_user(user)
        
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'user_id': str(user.id_user), 
            'device_id': device_id,
            'is_new_user': is_new_user
        }, status=status.HTTP_201_CREATED if is_new_user else status.HTTP_200_OK)

class UserDetailView(APIView):
    def get(self, request):
        try:
            serializer = UserSerializer(request.user)
            return Response(serializer.data)
        except Exception:
            return Response({
                'error': 'Invalid token'
            }, status=status.HTTP_401_UNAUTHORIZED)







