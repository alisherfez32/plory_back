from adminsortable2.admin import SortableAdminMixin
from django.contrib import admin
from .models import Countries, Airports, Seasons


@admin.register(Countries)
class CountriesAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('name', 'continent', 'capital', )
    list_display_links = ('name', 'continent', 'capital', )
    list_filter = ('name', 'continent', 'capital', )
    search_fields = ('name', )
    # list_editable = ('name', 'location', 'capital', )


admin.site.register(Airports)
admin.site.register(Seasons)