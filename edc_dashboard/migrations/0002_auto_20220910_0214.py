# Generated by Django 3.2.13 on 2022-09-09 23:14

from django.db import migrations


def delete_old_permissions(apps, schema_editor):
    model_cls = apps.get_model("auth.permission")
    model_cls._default_manager.filter(
        content_type__app_label="edc_dashboard", content_type__model="dashboard"
    ).delete()


class Migration(migrations.Migration):

    dependencies = [
        ("edc_dashboard", "0001_initial"),
    ]

    operations = [migrations.RunPython(delete_old_permissions)]
