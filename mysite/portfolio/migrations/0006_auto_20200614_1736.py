# Generated by Django 3.0.7 on 2020-06-14 08:36

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0005_auto_20200613_0104'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='timestamp',
            new_name='create_date',
        ),
        migrations.AddField(
            model_name='contact',
            name='update_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
