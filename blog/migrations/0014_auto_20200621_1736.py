# Generated by Django 3.0.7 on 2020-06-21 08:36

from django.db import migrations
import mdeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_auto_20200618_2101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='text',
            field=mdeditor.fields.MDTextField(help_text='To Write with Markdown', verbose_name='text'),
        ),
    ]