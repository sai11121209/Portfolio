# Generated by Django 3.0.7 on 2020-06-15 15:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0006_auto_20200614_1736'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='create_date',
            new_name='created_date',
        ),
    ]