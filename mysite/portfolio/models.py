from django.db import models
from django.utils import timezone

# Create your models here.
class Contact(models.Model):
    name = models.TextField(max_length=50)
    email = models.TextField(null=True, max_length=254)
    title = models.TextField(max_length=200)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now)
    update_date = models.DateTimeField(default=timezone.now)

    def update(self):
        self.update_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title