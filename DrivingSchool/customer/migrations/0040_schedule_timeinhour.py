# Generated by Django 4.1 on 2022-11-14 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("customer", "0039_remove_payment_driverelated"),
    ]

    operations = [
        migrations.AddField(
            model_name="schedule",
            name="timeInHour",
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
