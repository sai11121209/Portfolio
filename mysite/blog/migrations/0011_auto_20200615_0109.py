# Generated by Django 3.0.7 on 2020-06-14 16:09

from django.db import migrations
import markdownx.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20200614_1738'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='text',
            field=markdownx.models.MarkdownxField(help_text='To Write with Markdown', verbose_name='text'),
        ),
    ]
