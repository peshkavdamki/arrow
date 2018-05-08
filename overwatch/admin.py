from django.contrib import admin
from . import models

# Register your models here.

class OrderAdmin(admin.ModelAdmin):
    list_display = ['created', 'type', 'pack', 'oldScore', 'newScore', 'contact', 'price', 'paid', 'booster', 'done']
    search_fields = ['created', 'booster']


class BoostersAdmin(admin.ModelAdmin):
    list_display = ['name']


class PackAdmin(admin.ModelAdmin):
    list_display = ['name', 'type', 'price', 'is_active', 'description']

admin.site.register(models.Order, OrderAdmin)
admin.site.register(models.Booster, BoostersAdmin)
admin.site.register(models.Pack, PackAdmin)
