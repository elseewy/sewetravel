# Generated by Django 4.1.7 on 2023-04-12 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tours", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="tour",
            name="check_in_date",
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="tour",
            name="check_out_date",
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="tour",
            name="no_people",
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
