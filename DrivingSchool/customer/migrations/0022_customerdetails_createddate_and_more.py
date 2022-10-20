# Generated by Django 4.1 on 2022-10-20 01:17

import datetime
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("customer", "0021_customerdetails_drivingpackage"),
    ]

    operations = [
        migrations.AddField(
            model_name="customerdetails",
            name="CreatedDate",
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name="customerdetails",
            name="CreatedTime",
            field=models.TimeField(default=django.utils.timezone.now),
        ),
    ]
