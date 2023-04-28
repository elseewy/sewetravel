from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField


# Create your models here.
class TourList(models.Model):

    tourlist_title = models.CharField(max_length=155, blank=True)
    description = RichTextField(blank=True)
    tourlist_photo = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    is_featured = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.tourlist_title