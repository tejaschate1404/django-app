# Generated by Django 5.0 on 2023-12-23 11:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_contact_datetime'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='dateTime',
        ),
    ]