from django.db import models
from django.utils import timezone
from django.utils.safestring import mark_safe
from mdeditor.fields import MDTextField # 追加

# Create your models here.
class Posts(models.Model):
    author = models.ForeignKey('auth.user', on_delete=models.CASCADE)
    title = models.TextField(max_length=500)
    text = MDTextField()
    tags = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    update_date = models.DateTimeField(default=timezone.now)

    def update(self):
        self.update_date = timezone.now()
        self.save()

    def tag(self):
        return self.tags.split()

    def __str__(self):
        return self.title
