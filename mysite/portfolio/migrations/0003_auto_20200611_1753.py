# Generated by Django 3.0.7 on 2020-06-11 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_auto_20200611_1723'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='mail_address',
        ),
        migrations.AddField(
            model_name='contact',
            name='email',
            field=models.TextField(null=True),
        ),
    ]
