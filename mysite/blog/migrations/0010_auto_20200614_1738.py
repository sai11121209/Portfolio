# Generated by Django 3.0.7 on 2020-06-14 08:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20200614_1736'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='update_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]