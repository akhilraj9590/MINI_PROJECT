# Generated by Django 4.1 on 2022-11-16 05:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0018_servicenonlicenceandprice"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="serviceNonLicenceAndPrice", new_name="RcModificationsAndPrice",
        ),
    ]