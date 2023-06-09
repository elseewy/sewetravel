# Generated by Django 4.1.7 on 2023-04-12 20:33

import ckeditor.fields
import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Tour",
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
                ("tour_title", models.CharField(max_length=150)),
                ("destination", models.CharField(blank=True, max_length=150)),
                ("adv_title", models.CharField(blank=True, max_length=155)),
                ("description", ckeditor.fields.RichTextField(blank=True)),
                (
                    "adv_photo",
                    models.ImageField(blank=True, upload_to="photos/%Y/%m/%d"),
                ),
                ("no_nights", models.PositiveIntegerField()),
                ("no_days", models.PositiveIntegerField()),
                ("no_stars", models.PositiveIntegerField()),
                (
                    "meal_one",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("Breakfast", "Breakfast"),
                            ("Lunch", "Lunch"),
                            ("Dinner", "Dinner"),
                            ("Brunch", "Brunch"),
                            ("Buffet", "Buffet"),
                        ],
                        max_length=100,
                        null=True,
                    ),
                ),
                (
                    "meal_two",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("Breakfast", "Breakfast"),
                            ("Lunch", "Lunch"),
                            ("Dinner", "Dinner"),
                            ("Brunch", "Brunch"),
                            ("Buffet", "Buffet"),
                        ],
                        max_length=100,
                        null=True,
                    ),
                ),
                (
                    "meal_three",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("Breakfast", "Breakfast"),
                            ("Lunch", "Lunch"),
                            ("Dinner", "Dinner"),
                            ("Brunch", "Brunch"),
                            ("Buffet", "Buffet"),
                        ],
                        max_length=100,
                        null=True,
                    ),
                ),
                (
                    "meal_four",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("Breakfast", "Breakfast"),
                            ("Lunch", "Lunch"),
                            ("Dinner", "Dinner"),
                            ("Brunch", "Brunch"),
                            ("Buffet", "Buffet"),
                        ],
                        max_length=100,
                        null=True,
                    ),
                ),
                (
                    "meal_five",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("Breakfast", "Breakfast"),
                            ("Lunch", "Lunch"),
                            ("Dinner", "Dinner"),
                            ("Brunch", "Brunch"),
                            ("Buffet", "Buffet"),
                        ],
                        max_length=100,
                        null=True,
                    ),
                ),
                (
                    "year",
                    models.IntegerField(
                        blank=True,
                        choices=[
                            (2000, 2000),
                            (2001, 2001),
                            (2002, 2002),
                            (2003, 2003),
                            (2004, 2004),
                            (2005, 2005),
                            (2006, 2006),
                            (2007, 2007),
                            (2008, 2008),
                            (2009, 2009),
                            (2010, 2010),
                            (2011, 2011),
                            (2012, 2012),
                            (2013, 2013),
                            (2014, 2014),
                            (2015, 2015),
                            (2016, 2016),
                            (2017, 2017),
                            (2018, 2018),
                            (2019, 2019),
                            (2020, 2020),
                            (2021, 2021),
                            (2022, 2022),
                            (2023, 2023),
                        ],
                        null=True,
                        verbose_name="year",
                    ),
                ),
                ("tour_price", models.IntegerField()),
                (
                    "highlight_1",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
                (
                    "highlight_2",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
                (
                    "highlight_3",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
                (
                    "highlight_4",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
                (
                    "highlight_5",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
                ("tour_photo", models.ImageField(upload_to="photos/%Y/%m/%d")),
                (
                    "tour_photo_1",
                    models.ImageField(blank=True, upload_to="photos/%Y/%m/%d"),
                ),
                (
                    "tour_photo_2",
                    models.ImageField(blank=True, upload_to="photos/%Y/%m/%d"),
                ),
                (
                    "tour_photo_3",
                    models.ImageField(blank=True, upload_to="photos/%Y/%m/%d"),
                ),
                (
                    "tour_photo_4",
                    models.ImageField(blank=True, upload_to="photos/%Y/%m/%d"),
                ),
                (
                    "tour_photo_5",
                    models.ImageField(blank=True, upload_to="photos/%Y/%m/%d"),
                ),
                (
                    "tour_photo_6",
                    models.ImageField(blank=True, upload_to="photos/%Y/%m/%d"),
                ),
                (
                    "tour_photo_7",
                    models.ImageField(blank=True, upload_to="photos/%Y/%m/%d"),
                ),
                (
                    "tour_photo_8",
                    models.ImageField(blank=True, upload_to="photos/%Y/%m/%d"),
                ),
                (
                    "tour_photo_9",
                    models.ImageField(blank=True, upload_to="photos/%Y/%m/%d"),
                ),
                (
                    "tour_photo_10",
                    models.ImageField(blank=True, upload_to="photos/%Y/%m/%d"),
                ),
                (
                    "tour_photo_11",
                    models.ImageField(blank=True, upload_to="photos/%Y/%m/%d"),
                ),
                (
                    "tour_photo_12",
                    models.ImageField(blank=True, upload_to="photos/%Y/%m/%d"),
                ),
                (
                    "tour_photo_13",
                    models.ImageField(blank=True, upload_to="photos/%Y/%m/%d"),
                ),
                (
                    "tour_photo_14",
                    models.ImageField(blank=True, upload_to="photos/%Y/%m/%d"),
                ),
                (
                    "tour_photo_15",
                    models.ImageField(blank=True, upload_to="photos/%Y/%m/%d"),
                ),
                (
                    "tour_photo_16",
                    models.ImageField(blank=True, upload_to="photos/%Y/%m/%d"),
                ),
                ("tour_video", models.FileField(blank=True, upload_to="videos/%Y")),
                ("day_1", ckeditor.fields.RichTextField(blank=True)),
                ("day_2", ckeditor.fields.RichTextField(blank=True)),
                ("day_3", ckeditor.fields.RichTextField(blank=True)),
                ("day_4", ckeditor.fields.RichTextField(blank=True)),
                ("day_5", ckeditor.fields.RichTextField(blank=True)),
                ("day_6", ckeditor.fields.RichTextField(blank=True)),
                ("day_7", ckeditor.fields.RichTextField(blank=True)),
                ("day_8", ckeditor.fields.RichTextField(blank=True)),
                ("day_9", ckeditor.fields.RichTextField(blank=True)),
                ("day_10", ckeditor.fields.RichTextField(blank=True)),
                ("day_11", ckeditor.fields.RichTextField(blank=True)),
                ("day_12", ckeditor.fields.RichTextField(blank=True)),
                ("day_13", ckeditor.fields.RichTextField(blank=True)),
                ("day_14", ckeditor.fields.RichTextField(blank=True)),
                ("day_15", ckeditor.fields.RichTextField(blank=True)),
                ("day_16", ckeditor.fields.RichTextField(blank=True)),
                ("no_people", models.IntegerField(blank=True)),
                ("check_in_date", models.DateField(blank=True)),
                ("check_out_date", models.DateField(blank=True)),
                ("tour_included", ckeditor.fields.RichTextField(blank=True)),
                ("tour_excluded", ckeditor.fields.RichTextField(blank=True)),
                ("tour_details", ckeditor.fields.RichTextField(blank=True)),
                ("is_featured", models.BooleanField(default=False)),
                (
                    "created_date",
                    models.DateTimeField(blank=True, default=datetime.datetime.now),
                ),
            ],
        ),
    ]
