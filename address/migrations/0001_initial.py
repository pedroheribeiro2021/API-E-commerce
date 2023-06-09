# Generated by Django 4.0 on 2023-03-15 18:07

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('state', models.CharField(max_length=150)),
                ('city', models.CharField(max_length=150)),
                ('zip_code', models.CharField(max_length=8)),
                ('street', models.CharField(max_length=150)),
                ('number', models.PositiveSmallIntegerField()),
            ],
        ),
    ]
