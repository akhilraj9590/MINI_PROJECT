# Generated by Django 4.1 on 2022-11-16 05:27

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0019_rename_servicenonlicenceandprice_rcmodificationsandprice"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("customer", "0040_schedule_timeinhour"),
    ]

    operations = [
        migrations.CreateModel(
            name="ServiceApplicationOfNonLicence",
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
                (
                    "SSLC",
                    models.ImageField(blank=True, null=True, upload_to="ssleImages"),
                ),
                (
                    "IdProof",
                    models.ImageField(blank=True, null=True, upload_to="IdProof"),
                ),
                ("Photo", models.ImageField(blank=True, null=True, upload_to="Photo")),
                (
                    "PhysicalFitness",
                    models.ImageField(
                        blank=True, null=True, upload_to="PhysicalFitness"
                    ),
                ),
                (
                    "AgeProof",
                    models.ImageField(blank=True, null=True, upload_to="AgeProof"),
                ),
                (
                    "VehicleRegistration",
                    models.ImageField(blank=True, null=True, upload_to="RCbook"),
                ),
                (
                    "ApplicationOfPSV",
                    models.ImageField(
                        blank=True, null=True, upload_to="PSVapplication"
                    ),
                ),
                (
                    "MedicalCirtifict",
                    models.ImageField(
                        blank=True, null=True, upload_to="MedicalCirtifict"
                    ),
                ),
                (
                    "SchoolCirtifict",
                    models.ImageField(
                        blank=True, null=True, upload_to="SchoolCirtifict"
                    ),
                ),
                (
                    "DrivingLicenseOld",
                    models.ImageField(
                        blank=True, null=True, upload_to="DrivinLicenseOld"
                    ),
                ),
                (
                    "Status",
                    models.CharField(
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
                (
                    "time",
                    models.TimeField(default=django.utils.timezone.now, null=True),
                ),
                ("Date", models.DateField(default=datetime.date.today, null=True)),
                (
                    "BranchId",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="user.branch"
                    ),
                ),
                (
                    "CustomerId",
                    models.ForeignKey(
                        db_constraint=False,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "ServiceName",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="user.rcmodificationsandprice",
                    ),
                ),
            ],
        ),
    ]