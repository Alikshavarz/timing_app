import uuid
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import UserSerializer
from .models import CustomUser
from rest_framework.permissions import IsAuthenticated


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
            password = CustomUser.objects.make_random_password()
            user = CustomUser.objects.create_user(
                username=device_id,
                password=password
            )
            is_new_user = True

        refresh = RefreshToken.for_user(user)

        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'user_id': user.id_user,
            'device_id': device_id,
            'is_new_user': is_new_user
        }, status=status.HTTP_201_CREATED if is_new_user else status.HTTP_200_OK)


class UserDetailView(APIView):
    permission_classes = [IsAuthenticated]  # اطمینان از اعتبار توکن

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)