# Generated by Django 4.2.1 on 2023-06-03 04:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("resume_app", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="employee", old_name="personal", new_name="designation",
        ),
        migrations.RenameField(
            model_name="employee", old_name="summary", new_name="name",
        ),
        migrations.RenameField(
            model_name="employee",
            old_name="technical",
            new_name="professional_summary",
        ),
        migrations.AddField(
            model_name="employee",
            name="technical_skill_set",
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]