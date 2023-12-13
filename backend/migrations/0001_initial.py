# Generated by Django 4.2.5 on 2023-10-06 16:05

import backend.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('event_name', models.CharField(max_length=100, primary_key=True, serialize=False, unique=True)),
                ('starting_date', models.DateField()),
                ('num_of_days', models.IntegerField()),
                ('num_of_sessions', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Attendee',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=254)),
                ('roll_number', models.CharField(blank=True, max_length=150, null=True)),
                ('attendence_log', models.JSONField(default=backend.models.defaultDict)),
                ('misc_log', models.JSONField(default=backend.models.defaultDict)),
                ('event_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.event')),
            ],
        ),
    ]
