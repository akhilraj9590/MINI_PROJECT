# Generated by Django 4.1 on 2022-10-12 20:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0008_rename_servicesnameandprrice_servicesnameandprice"),
        ("customer", "0015_serviceapplication_servicename"),
    ]

    operations = [
        migrations.AlterField(
            model_name="serviceapplication",
            name="ServiceName",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="user.servicesnameandprice",
            ),
        ),
    ]
