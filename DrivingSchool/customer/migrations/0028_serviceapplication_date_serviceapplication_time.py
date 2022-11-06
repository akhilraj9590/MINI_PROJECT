# Generated by Django 4.1 on 2022-10-31 17:15

import datetime
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("customer", "0027_alter_serviceapplication_status"),
    ]

    operations = [
        migrations.AddField(
            model_name="serviceapplication",
            name="Date",
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name="serviceapplication",
            name="time",
            field=models.TimeField(default=django.utils.timezone.now),
        ),
    ]