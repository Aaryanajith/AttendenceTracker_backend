# Generated by Django 4.2.5 on 2023-09-25 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0015_rename_attandence_log_attendence_attendence_log'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendence',
            name='attendence_log',
            field=models.JSONField(default={'isOUT': False}),
        ),
    ]