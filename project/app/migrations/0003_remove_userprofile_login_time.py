# Generated by Django 5.0.1 on 2024-01-03 18:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_userprofile_login_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='login_time',
        ),
    ]