from django.contrib import admin
from .models import Order, OrderTag

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'inventory', 'is_active', 'start_date', 'embargo_date')

@admin.register(OrderTag)
class OrderTagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'is_active')
