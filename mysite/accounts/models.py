from django.db import models
from django.utils import timezone

# Create your models here.
class User(models.Model):
    email = models.TextField(max_length=254)
    username = models.TextField(max_length=150)
    password = models.TextField(max_length=128)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.username
