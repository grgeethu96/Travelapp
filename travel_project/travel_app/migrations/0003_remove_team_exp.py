# Generated by Django 3.2.15 on 2022-09-29 09:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travel_app', '0002_team'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='exp',
        ),
    ]