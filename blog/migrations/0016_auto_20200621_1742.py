# Generated by Django 3.0.7 on 2020-06-21 08:42

from django.db import migrations
import mdeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_auto_20200621_1741'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='text',
            field=mdeditor.fields.MDTextField(help_text='To Write with Markdown', verbose_name='text'),
        ),
    ]
