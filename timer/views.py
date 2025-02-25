from django.shortcuts import render
from .models import TimeEntry, Profile
from .serializers import TimeEntrySerializer, ProfileSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics

class TimeEntryListCreateView(generics.ListCreateAPIView):
    queryset = TimeEntry.objects.all()
    serializer_class = TimeEntrySerializer
    permission_classes = [IsAuthenticated]

# Get, Update, Delete
class TimeEntryRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TimeEntry.objects.all()
    serializer_class = TimeEntrySerializer
    permission_classes = [IsAuthenticated]
