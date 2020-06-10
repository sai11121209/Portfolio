from django.db import models
from django.utils import timezone

# Create your models here.
class Contact(models.Model):
    name = models.TextField(max_length=50)
    mail_address = models.TextField(max_length=264, unique=True)
    title = models.TextField(max_length=200)
    txt = models.TextField()
    timestamp = models.DateField(default=timezone.now)

    def __str__(self):
        return self.title