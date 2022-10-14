# Generated by Django 4.1 on 2022-10-08 19:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0006_branch"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("customer", "0006_serviceapplication_ageproof_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="schedule",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("Venue", models.CharField(max_length=100, null=True)),
                ("Date", models.DateField()),
                ("time", models.TimeField(default=django.utils.timezone.now)),
                (
                    "BranchId",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="user.branch"
                    ),
                ),
                (
                    "UserId",
                    models.ForeignKey(
                        db_constraint=False,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
