# Generated by Django 4.1 on 2022-11-13 02:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("customer", "0036_serviceapplication_learnigdate_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="serviceapplication",
            name="leanigStatus",
            field=models.CharField(
                blank=True,
                choices=[("Not complete", "Not complete"), ("Complete", "Complete")],
                max_length=100,
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="serviceapplication",
            name="testStatus",
            field=models.CharField(
                blank=True,
                choices=[("Not complete", "Not complete"), ("Complete", "Complete")],
                max_length=100,
                null=True,
            ),
        ),
    ]
