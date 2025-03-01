from rest_framework.response import Response
from .models import TimeEntry
from .serializers import TimeEntrySerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics


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

