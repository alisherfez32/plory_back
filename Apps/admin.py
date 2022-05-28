from django.contrib import admin

from .models import CommonApps, CountryApps, Filters


class CountryAppsAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'date_added',)
    list_display_links = ('name', 'description', 'date_added',)
    list_filter = ('name', 'date_added', )
    search_fields = ('name', 'description',)


admin.site.register(CommonApps, CountryAppsAdmin)
admin.site.register(CountryApps)
admin.site.register(Filters)
