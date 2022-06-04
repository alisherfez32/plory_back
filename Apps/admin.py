from django.contrib import admin
from adminsortable2.admin import SortableAdminMixin

from .models import CommonApps, CountryApps, Filters


# class FiltersInline(admin.TabularInline):
#     model = Filters


@admin.register(CommonApps)
class CountryAppsAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'date_added',)
    list_display_links = ('name', 'description', 'date_added',)
    list_filter = ('name', 'date_added',)
    search_fields = ('name', 'description',)
    # inlines = [FiltersInline, ]


# admin.site.register(SortableAdminMixin, CommonApps, CountryAppsAdmin)
admin.site.register(CountryApps)
admin.site.register(Filters)
