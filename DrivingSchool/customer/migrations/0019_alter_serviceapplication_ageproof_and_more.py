# Generated by Django 4.1 on 2022-10-14 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("customer", "0018_alter_serviceapplication_ageproof_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="serviceapplication",
            name="AgeProof",
            field=models.ImageField(blank=True, null=True, upload_to="AgeProof"),
        ),
        migrations.AlterField(
            model_name="serviceapplication",
            name="ApplicationOfPSV",
            field=models.ImageField(blank=True, null=True, upload_to="PSVapplication"),
        ),
        migrations.AlterField(
            model_name="serviceapplication",
            name="DrivingLicenseOld",
            field=models.ImageField(
                blank=True, null=True, upload_to="DrivinLicenseOld"
            ),
        ),
        migrations.AlterField(
            model_name="serviceapplication",
            name="IdProof",
            field=models.ImageField(blank=True, null=True, upload_to="IdProof"),
        ),
        migrations.AlterField(
            model_name="serviceapplication",
            name="MedicalCirtifict",
            field=models.ImageField(
                blank=True, null=True, upload_to="MedicalCirtifict"
            ),
        ),
        migrations.AlterField(
            model_name="serviceapplication",
            name="Photo",
            field=models.ImageField(blank=True, null=True, upload_to="Photo"),
        ),
        migrations.AlterField(
            model_name="serviceapplication",
            name="PhysicalFitness",
            field=models.ImageField(blank=True, null=True, upload_to="PhysicalFitness"),
        ),
        migrations.AlterField(
            model_name="serviceapplication",
            name="SSLC",
            field=models.ImageField(blank=True, null=True, upload_to="ssleImages"),
        ),
        migrations.AlterField(
            model_name="serviceapplication",
            name="SchoolCirtifict",
            field=models.ImageField(blank=True, null=True, upload_to="SchoolCirtifict"),
        ),
        migrations.AlterField(
            model_name="serviceapplication",
            name="VehicleRegistration",
            field=models.ImageField(blank=True, null=True, upload_to="RCbook"),
        ),
    ]