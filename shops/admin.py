from django.contrib.gis import admin
from django.contrib.gis.admin import OSMGeoAdmin
from .models import Shop


# Use @admin.register decorator to register the Shop model in the admin application.
@admin.register(Shop)
class ShopAdmin(OSMGeoAdmin):
    # Since Shop model includes a GeoDjango field, we need to use the special OSMGeoAdmin class.
    list_display = ('name', 'location')
