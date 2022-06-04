from adminsortable2.admin import SortableAdminMixin
from django.contrib import admin

from .models import CountryFood, Status, Filters


@admin.register(CountryFood)
class CountryFoodAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('name', 'description', 'date_added')
    list_display_links = ('name', 'description', 'date_added')
    list_filter = ('name', 'description', 'date_added')
    search_fields = ('name', 'description', 'date_added')


# admin.site.register(CountryFood, CountryFoodAdmin)
admin.site.register(Status)
admin.site.register(Filters)
