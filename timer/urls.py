from .views import ProjectListCreateView, ProjectRetrieveUpdateDestroyView, TimeEntryListCreateView, TimeEntryRetrieveUpdateDestroyView
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView

# from timer.views import TimeEntryListCreateView, TimeEntryRetrieveUpdateDestroyView

urlpatterns = [
    path('time-entries/', TimeEntryListCreateView.as_view(), name='time-entry'),
    path('time-entries/<int:pk>/', TimeEntryRetrieveUpdateDestroyView.as_view(), name='time-entry-detail'), # To retrieve, update, or delete a specific entry.

    path('project/', ProjectListCreateView.as_view(), name='projects'),
    path('project/<int:pk>/', ProjectRetrieveUpdateDestroyView.as_view(), name='project-detail'),

]