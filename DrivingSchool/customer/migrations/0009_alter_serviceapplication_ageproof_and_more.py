# Generated by Django 4.1 on 2022-10-08 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("customer", "0008_alter_serviceapplication_sslc"),
    ]

    operations = [
        migrations.AlterField(
            model_name="serviceapplication",
            name="AgeProof",
            field=models.ImageField(null=True, upload_to="AgeProof"),
        ),
        migrations.AlterField(
            model_name="serviceapplication",
            name="ApplicationOfPSV",
            field=models.ImageField(null=True, upload_to="PSVapplication"),
        ),
        migrations.AlterField(
            model_name="serviceapplication",
            name="DrivingLicenseOld",
            field=models.ImageField(null=True, upload_to="DrivinLicenseOld"),
        ),
        migrations.AlterField(
            model_name="serviceapplication",
            name="IdProof",
            field=models.ImageField(null=True, upload_to="IdProof"),
        ),
        migrations.AlterField(
            model_name="serviceapplication",
            name="MedicalCirtifict",
            field=models.ImageField(null=True, upload_to="MedicalCirtifict"),
        ),
        migrations.AlterField(
            model_name="serviceapplication",
            name="Photo",
            field=models.ImageField(null=True, upload_to="Photo"),
        ),
        migrations.AlterField(
            model_name="serviceapplication",
            name="PhysicalFitness",
            field=models.ImageField(null=True, upload_to="PhysicalFitness"),
        ),
        migrations.AlterField(
            model_name="serviceapplication",
            name="SchoolCirtifict",
            field=models.ImageField(null=True, upload_to="SchoolCirtifict"),
        ),
        migrations.AlterField(
            model_name="serviceapplication",
            name="Status",
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="serviceapplication",
            name="VehicleRegistration",
            field=models.ImageField(null=True, upload_to="RCbook"),
        ),
    ]
