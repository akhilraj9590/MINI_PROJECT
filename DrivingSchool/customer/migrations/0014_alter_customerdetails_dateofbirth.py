# Generated by Django 4.1 on 2022-10-12 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("customer", "0013_delete_customerbranch"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customerdetails",
            name="DateOfBirth",
            field=models.DateField(null=True),
        ),
    ]
