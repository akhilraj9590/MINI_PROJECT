# Generated by Django 4.1 on 2022-10-12 19:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("customer", "0012_customerbranch"),
    ]

    operations = [
        migrations.DeleteModel(name="CustomerBranch",),
    ]
