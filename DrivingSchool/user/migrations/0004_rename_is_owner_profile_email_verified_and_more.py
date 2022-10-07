# Generated by Django 4.1 on 2022-10-06 02:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0003_profile_delete_userextend"),
    ]

    operations = [
        migrations.RenameField(
            model_name="profile", old_name="is_owner", new_name="email_verified",
        ),
        migrations.RemoveField(model_name="profile", name="is_customer",),
        migrations.RemoveField(model_name="profile", name="is_staff",),
    ]