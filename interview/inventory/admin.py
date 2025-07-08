from django.contrib import admin
from .models import Inventory, InventoryTag, InventoryLanguage, InventoryType

@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'type', 'language', 'created_at')

@admin.register(InventoryTag)
class InventoryTagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'is_active')

@admin.register(InventoryLanguage)
class InventoryLanguageAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(InventoryType)
class InventoryTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
