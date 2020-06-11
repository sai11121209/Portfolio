from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey('auth.user', on_delete=models.CASCADE)
    title = models.TextField(max_length=500)
    text = models.TextField()
    tag = models.TextField()
    comment = models.TextField(null=True)
    created_date = models.DateTimeField(default=timezone.now)
    Update_date = models.DateField(blank=True,null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class User(models.Model):
    username = models.TextField(max_length=150)
    email = models.TextField(max_length=254)
    password = models.TextField(max_length=128)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.username
