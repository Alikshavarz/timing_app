from .views import TimeEntryListCreateView, TimeEntryRetrieveUpdateDestroyView
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView

from timer.views import TimeEntryListCreateView, TimeEntryRetrieveUpdateDestroyView

urlpatterns = [
    path('time-entries/', TimeEntryListCreateView.as_view(), name='time-entry'),
    path('time-entries/<int:pk>/', TimeEntryRetrieveUpdateDestroyView.as_view(), name='time-entry-detail'), # To retrieve, update, or delete a specific entry.
]