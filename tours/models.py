from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField


# Create your models here.
class Tour(models.Model):

    meal_choices = (
        ('Breakfast', 'Breakfast'),
        ('Lunch', 'Lunch'),
        ('Dinner', 'Dinner'),
        ('Brunch', 'Brunch'),
        ('Buffet', 'Buffet'),
    )

    year_choice = []
    for r in range(2000, (datetime.now().year + 1)):
        year_choice.append((r, r))

    tour_title = models.CharField(max_length=150)
    destination = models.CharField(max_length=150,blank=True)
    no_nights = models.PositiveIntegerField()
    no_days = models.PositiveIntegerField()
    no_stars = models.PositiveIntegerField()
    meal_one = models.CharField(choices=meal_choices, max_length=100, null=True, blank=True)
    meal_two = models.CharField(choices=meal_choices, max_length=100, null=True, blank=True)
    meal_three = models.CharField(choices=meal_choices, max_length=100, null=True, blank=True)
    meal_four = models.CharField(choices=meal_choices, max_length=100, null=True, blank=True)
    meal_five = models.CharField(choices=meal_choices, max_length=100, null=True, blank=True)
    year = models.IntegerField(('year'), choices=year_choice, blank=True, null=True)
    tour_price = models.IntegerField()
    hightlight = RichTextField(blank=True,null=True)
    highlight_1 = models.CharField(max_length=200, blank=True,null=True)
    highlight_2 = models.CharField(max_length=200, blank=True, null=True)
    highlight_3 = models.CharField(max_length=200, blank=True, null=True)
    highlight_4 = models.CharField(max_length=200, blank=True, null=True)
    highlight_5 = models.CharField(max_length=200, blank=True, null=True)
    tour_photo = models.ImageField(upload_to='photos/%Y/%m/%d')
    tour_photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    tour_photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    tour_photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    tour_photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    tour_photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    tour_photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    tour_photo_7 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    tour_photo_8 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    tour_photo_9 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    tour_photo_10 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    tour_photo_11 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    tour_photo_12 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    tour_photo_13 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    tour_photo_14 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    tour_photo_15 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    tour_photo_16 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    tour_video = models.FileField(upload_to='videos/%Y', blank=True)

    day_1 = RichTextField(blank=True)
    day_1_title = models.CharField(max_length=200, blank=True, null=True)
    day_2 = RichTextField(blank=True)
    day_2_title = models.CharField(max_length=200, blank=True, null=True)
    day_3 = RichTextField(blank=True)
    day_3_title = models.CharField(max_length=200, blank=True, null=True)
    day_4 = RichTextField(blank=True)
    day_4_title = models.CharField(max_length=200, blank=True, null=True)
    day_5 = RichTextField(blank=True)
    day_5_title = models.CharField(max_length=200, blank=True, null=True)
    day_6 = RichTextField(blank=True)
    day_6_title = models.CharField(max_length=200, blank=True, null=True)
    day_7 = RichTextField(blank=True)
    day_8_title = models.CharField(max_length=200, blank=True, null=True)
    day_8 = RichTextField(blank=True)
    day_9_title = models.CharField(max_length=200, blank=True, null=True)
    day_9 = RichTextField(blank=True)
    day_10_title = models.CharField(max_length=200, blank=True, null=True)
    day_10 = RichTextField(blank=True)
    day_11_title = models.CharField(max_length=200, blank=True, null=True)
    day_11 = RichTextField(blank=True)
    day_12_title = models.CharField(max_length=200, blank=True, null=True)
    day_12 = RichTextField(blank=True)
    day_13_title = models.CharField(max_length=200, blank=True, null=True)
    day_13 = RichTextField(blank=True)
    day_14_title = models.CharField(max_length=200, blank=True, null=True)
    day_14 = RichTextField(blank=True)
    day_15_title = models.CharField(max_length=200, blank=True, null=True)
    day_15 = RichTextField(blank=True)
    day_16_title = models.CharField(max_length=200, blank=True, null=True)
    day_16 = RichTextField(blank=True)

    no_people = models.IntegerField(blank=True, null=True)
    check_in_date =models.DateField(blank=True, null=True)
    check_out_date= models.DateField(blank=True, null=True)
    tour_included = RichTextField(blank=True)
    tour_included_2 = RichTextField(blank=True)
    tour_excluded = RichTextField(blank=True)
    tour_details = RichTextField(blank=True)
    is_featured = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.tour_title