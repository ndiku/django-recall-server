# Generated by Django 5.0.6 on 2024-06-26 16:33

import uuid

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("polling_station", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="pollingstation",
            options={"ordering": ("-updated_at", "-created_at")},
        ),
        migrations.RemoveField(
            model_name="pollingstation",
            name="id",
        ),
        migrations.AddField(
            model_name="pollingstation",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="pollingstation",
            name="is_active",
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name="pollingstation",
            name="tokenized_id",
            field=models.UUIDField(
                default=uuid.uuid4, editable=False, primary_key=True, serialize=False
            ),
        ),
        migrations.AddField(
            model_name="pollingstation",
            name="updated_at",
            field=models.DateTimeField(auto_now=True),
        ),
    ]