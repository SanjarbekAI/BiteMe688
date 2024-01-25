from django.contrib import admin
from foods.models import FoodsModel

@admin.register(FoodsModel)
class FoodsAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'created_at']
    list_filter = ['created_at']
    search_fields = ['name']
