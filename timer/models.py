from django.db import models

class Profile(models.Model):
    name = models.CharField(max_length =30)
    description = models.TextField()

class TimeEntry(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    start_time = models.DateTimeField(auto_now_add=True)
    duration = models.PositiveIntegerField()
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

