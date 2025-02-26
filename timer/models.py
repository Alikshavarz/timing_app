from django.db import models

from django.conf import settings





class TimeEntry(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)
    start_time = models.DateTimeField(auto_now_add=True)
    duration = models.PositiveIntegerField()
    update_time = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title

