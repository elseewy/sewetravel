# Generated by Django 4.1.7 on 2023-04-13 00:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("tours", "0002_alter_tour_check_in_date_alter_tour_check_out_date_and_more"),
    ]

    operations = [
        migrations.RemoveField(model_name="tour", name="adv_photo",),
        migrations.RemoveField(model_name="tour", name="adv_title",),
        migrations.RemoveField(model_name="tour", name="description",),
    ]
