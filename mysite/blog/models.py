from django.db import models
from django.utils import timezone
from markdownx.models import MarkdownxField
from markdownx.utils import markdownify
from django.utils.safestring import mark_safe

# Create your models here.
class Posts(models.Model):
    author = models.ForeignKey('auth.user', on_delete=models.CASCADE)
    title = models.TextField(max_length=500)
    text = MarkdownxField('text', help_text='To Write with Markdown')
    tag = models.TextField()
    comment = models.TextField(null=True)
    created_date = models.DateTimeField(default=timezone.now)
    update_date = models.DateTimeField(default=timezone.now)

    def update(self):
        self.update_date = timezone.now()
        self.save()

    def markdown(self): #テンプレートでmarkdownを適応するため
        return mark_safe(markdownify(self.text))

    def __str__(self):
        return self.title
