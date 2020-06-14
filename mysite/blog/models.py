from django.db import models
from django.utils import timezone

# Create your models here.
class Posts(models.Model):
    author = models.ForeignKey('auth.user', on_delete=models.CASCADE)
    title = models.TextField(max_length=500)
    text = models.TextField()
    tag = models.TextField()
    comment = models.TextField(null=True)
    created_date = models.DateTimeField(default=timezone.now)
    update_date = models.DateTimeField(default=timezone.now)

    def update(self):
        self.update_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
