from django.db import models
from django.utils import timezone 

class Contact_us(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    created_date = models.DateTimeField(default=timezone.now)
    comment = models.TextField()

    def __str__(self):
        return self.name