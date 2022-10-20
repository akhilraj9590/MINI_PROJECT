# Generated by Django 4.1 on 2022-10-20 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0012_instructor"),
    ]

    operations = [
        migrations.AddField(
            model_name="instructor",
            name="Age",
            field=models.PositiveBigIntegerField(null=True),
        ),
        migrations.AddField(
            model_name="instructor",
            name="Experience",
            field=models.PositiveBigIntegerField(null=True),
        ),
        migrations.AddField(
            model_name="instructor",
            name="Gender",
            field=models.CharField(max_length=100, null=True),
        ),
    ]
