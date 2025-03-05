from .models import (Project, TimeEntry)
from .serializers import  ProjectSerializer, TimeEntrySerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework.exceptions import NotFound

class ProjectListCreateView(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    # permission_classes = [IsAuthenticated]  # فقط کاربران وارد شده اجازه دارند

class ProjectRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    # permission_classes = [IsAuthenticated]

    def put(self, request, *args, **kwargs):
        project = self.get_object()
        serializer = self.get_serializer(project, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)







class TimeEntryListCreateView(generics.ListCreateAPIView):
    queryset = TimeEntry.objects.all()
    serializer_class = TimeEntrySerializer
    # permission_classes = [IsAuthenticated]


# Get, Update, Delete
class TimeEntryRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TimeEntry.objects.all()
    serializer_class = TimeEntrySerializer
    # permission_classes = [IsAuthenticated]

    # update
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)

        return Response(serializer.errors, status=400)

