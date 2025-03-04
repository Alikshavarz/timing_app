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


    def get(self, request, *args, **kwargs):
        projects = self.queryset
        serializer = self.get_serializer(projects, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)  # ذخیره کاربر جاری
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProjectRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    # permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return self.queryset.get(pk=pk)
        except Project.DoesNotExist:
            raise NotFound("پروژه‌ای با این شناسه وجود ندارد.")

    def get(self, request, pk, *args, **kwargs):
        project = self.get_object(pk)
        serializer = self.get_serializer(project)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk, *args, **kwargs):
        project = self.get_object(pk)
        serializer = self.get_serializer(project, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, *args, **kwargs):
        project = self.get_object(pk)
        project.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)







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

