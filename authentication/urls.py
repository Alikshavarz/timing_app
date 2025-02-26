from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import AuthView, UserDetailView

urlpatterns = [
    path('auth/', AuthView.as_view(), name='auth'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('user/', UserDetailView.as_view(), name='user-detail'),
]

