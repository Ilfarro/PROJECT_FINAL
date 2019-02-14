from django.db import models
from django.utils import timezone 

class Our_talents(models.Model):
    title = models.CharField(max_length=255)
    created_date = models.DateTimeField(default=timezone.now)
    picture = models.CharField(max_length=255)

    def __str__(self):
        return self.title