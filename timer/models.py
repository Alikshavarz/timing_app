from django.db import models
from django.conf import settings


class Project(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='projects', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class TimeEntry(models.Model):
    title = models.CharField(max_length=50)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='time_entries')
    description = models.TextField(blank=True)
    start_time = models.DateTimeField(auto_now_add=True)
    duration = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title




