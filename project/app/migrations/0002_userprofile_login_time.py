# Generated by Django 5.0.1 on 2024-01-03 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='login_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]