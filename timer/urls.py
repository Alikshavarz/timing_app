from django.urls import path
from .views import TimeEntryListCreateView, TimeEntryRetrieveUpdateDestroyView

urlpatterns = [
    path('time-entries/', TimeEntryListCreateView.as_view(), name='time-entry-list-create'), # This URL is used for both creating a new time entry (POST) and listing existing time entries (GET)
    path('time-entries/<int:pk>/', TimeEntryRetrieveUpdateDestroyView.as_view(), name='time-entry-detail'), # To retrieve, update, or delete a specific entry.

]