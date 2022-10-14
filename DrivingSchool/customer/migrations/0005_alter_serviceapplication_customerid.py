# Generated by Django 4.1 on 2022-10-08 06:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("customer", "0004_alter_drivingapplication_customerid_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="serviceapplication",
            name="CustomerId",
            field=models.ForeignKey(
                db_constraint=False,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
