from typing import DefaultDict
from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey('auth.user', on_delete=models.CASCADE)
    title = models.TextField(max_length=500)
    text = models.TextField()
    info = models.TextField()
    tag = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    Update_date = models.DateField(blank=True,null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title