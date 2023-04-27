from django.contrib import admin
from .models import Team,MailMessage,Subscribers
from django.utils.html import format_html

# Register your models here.

class TeamAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="40" />'.format(object.photo.url))

    thumbnail.short_description = "Photo"
    list_display = ('id','thumbnail', 'first_name', 'last_name', 'created_date')
    list_display_links = ('id', 'thumbnail', 'first_name')
    search_fields = ('id', 'first_name', 'last_name', 'created_date', 'position')
    list_filter = ('position',)

admin.site.register(Team, TeamAdmin)
admin.site.register(MailMessage)
admin.site.register(Subscribers)
