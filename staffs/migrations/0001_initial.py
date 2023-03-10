# Generated by Django 4.1.4 on 2022-12-30 21:11

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Staff",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("name", models.TextField()),
                ("startDate", models.DateField()),
                ("quantity", models.PositiveIntegerField()),
                ("area", models.TextField()),
                ("role", models.TextField()),
                ("salary", models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]
