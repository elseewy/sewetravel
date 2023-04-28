from django.contrib import admin
from .models import Tour
from django.utils.html import format_html
# Register your models here.

class TourAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="40" style="border-radius: 50px;" />'.format(object.tour_photo.url))

    thumbnail.short_description = 'Tour Image'
    list_display = ('id','thumbnail','tour_title', 'destination', 'is_featured')
    list_display_links = ('id', 'thumbnail', 'tour_title')
    list_editable = ('is_featured',)
    search_fields = ('id', 'tour_title', 'destination',)

admin.site.register(Tour, TourAdmin)