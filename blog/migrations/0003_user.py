# Generated by Django 3.0.7 on 2020-06-11 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200611_2147'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.TextField(max_length=150)),
                ('email', models.TextField(max_length=254)),
                ('password', models.TextField(max_length=128)),
            ],
        ),
    ]
