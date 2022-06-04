from adminsortable2.admin import SortableAdminMixin
from django.contrib import admin

from .models import District, EatPlaces, Filters


@admin.register(EatPlaces)
class EatPlacesAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('name', 'price', 'date_added')
    list_display_links = ('name', 'price', 'date_added')
    list_filter = ('name', 'price', 'url', 'date_added')
    search_fields = ('name', 'price', 'date_added')


admin.site.register(District)
# admin.site.register(EatPlaces, EatPlacesAdmin)
admin.site.register(Filters)
