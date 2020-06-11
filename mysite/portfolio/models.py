from django.db import models
from django.utils import timezone

# Create your models here.
class Contact(models.Model):
    name = models.TextField(max_length=50)
    email = models.TextField(null=True)
    title = models.TextField(max_length=200)
    txt = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title