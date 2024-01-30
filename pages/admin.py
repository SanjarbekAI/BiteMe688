from django.contrib import admin
from pages.models import EventsModel, FeedbacksModel, EmailModel, OrderModel


@admin.register(EventsModel)
class EventsModelAdmin(admin.ModelAdmin):
    list_display = ['location_name', 'start_time', 'end_time']
    search_fields = ['location_name']
    list_filter = ['start_time', 'end_time']


@admin.register(FeedbacksModel)
class EventsModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'job']
    search_fields = ['name']
    list_filter = ['name']


@admin.register(EmailModel)
class EmailModelAdmin(admin.ModelAdmin):
    list_display = ['email']
    search_fields = ['email']
    list_filter = ['created_at']


@admin.register(OrderModel)
class OrderModelAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
    list_filter = ['created_at']