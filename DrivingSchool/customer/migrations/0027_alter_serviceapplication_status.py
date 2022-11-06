# Generated by Django 4.1 on 2022-10-27 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("customer", "0026_customerdetails_address"),
    ]

    operations = [
        migrations.AlterField(
            model_name="serviceapplication",
            name="Status",
            field=models.CharField(
                choices=[
                    ("Pending", "Pending"),
                    ("Processing", "Processing"),
                    ("Forwarded to RTO", "Forwarded to RTO"),
                    ("Complete", "Complete"),
                ],
                default="Pending",
                max_length=100,
                null=True,
            ),
        ),
    ]
