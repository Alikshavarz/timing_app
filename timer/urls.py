from .views import ProjectList, ProjectDetail, TimeEntryListCreateView, TimeEntryRetrieveUpdateDestroyView
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

# from timer.views import TimeEntryListCreateView, TimeEntryRetrieveUpdateDestroyView

urlpatterns = [
    path('time-entries/', TimeEntryListCreateView.as_view(), name='time-entry'),
    path('time-entries/<int:pk>/', TimeEntryRetrieveUpdateDestroyView.as_view(), name='time-entry-detail'), # To retrieve, update, or delete a specific entry.
    path('projects/', ProjectList.as_view(), name='projects'),
    path('projects/<int:pk>/', ProjectDetail.as_view(), name='project-detail'),
]