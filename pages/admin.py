from django.contrib import admin
from pages.models import EventsModel


@admin.register(EventsModel)
class EventsModelAdmin(admin.ModelAdmin):
    list_display = ['location_name', 'start_time', 'end_time']
    search_fields = ['location_name']
    list_filter = ['start_time', 'end_time']


