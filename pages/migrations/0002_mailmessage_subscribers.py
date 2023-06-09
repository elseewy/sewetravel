# Generated by Django 4.1.7 on 2023-04-23 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pages", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="MailMessage",
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
                ("title", models.CharField(max_length=100, null=True)),
                ("message", models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Subscribers",
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
                ("email", models.EmailField(max_length=254, null=True)),
                ("date", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
