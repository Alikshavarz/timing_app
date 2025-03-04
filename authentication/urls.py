
from django.urls import path
from .views import AuthView, UserDetailView
urlpatterns = [
    path('auth/', AuthView.as_view(), name='auth'),  # URL برای AuthView
    path('user/', UserDetailView.as_view(), name='user-detail'),  # URL برای UserDetailView
]



