from django.contrib import admin
from .models import StockItem

# Register your models here.
@admin.register(StockItem)
class StockItemAdmin(admin.ModelAdmin):
    list_display = ('item_name','category','stock','price')
    search_fields = ('item_name','category')
    list_filter = ('category',)
    ordering = ('item_name',)
    