# Generated by Django 4.1 on 2024-01-02 07:51

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Healthapp", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Disease",
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
                ("name", models.CharField(max_length=100)),
            ],
        ),
    ]
