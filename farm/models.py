# farm/models.py

from django.conf import settings
from django.db import models

class Farm(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # Use AUTH_USER_MODEL here
    location = models.CharField(max_length=255)
    crop_type = models.CharField(max_length=255)
    boundaries = models.JSONField()  # Adjust this according to how you want to store boundaries

    def __str__(self):
        return self.location
