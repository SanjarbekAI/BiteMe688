from django.contrib import admin
from staff.models import ChefsModel

@admin.register(ChefsModel)
class ChefsAdmin(admin.ModelAdmin):
    list_display = ['name', 'profession']
    search_fields = ['name']
    list_filter = ['created_at', 'updated_at']