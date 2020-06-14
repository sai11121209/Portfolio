from django.contrib import admin
from .models import Posts
from markdownx.admin import MarkdownxModelAdmin

# Register your models here.
#admin.site.register(Posts)
admin.site.register(Posts, MarkdownxModelAdmin)