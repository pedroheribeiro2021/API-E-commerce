# Generated by Django 4.1 on 2023-03-07 13:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="user",
            name="address",
        ),
    ]
