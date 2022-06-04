from adminsortable2.admin import SortableAdminMixin
from django.contrib import admin
from .models import AirStatus, Continents, ListOfCities, Countries, Cities


@admin.register(Countries)
class CountriesAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('name', 'location', 'capital', )
    list_display_links = ('name', 'location', 'capital', )
    list_filter = ('name', 'location', 'capital', )
    search_fields = ('name', 'population', )
    # list_editable = ('name', 'location', 'capital', )


@admin.register(Cities)
class CitiesAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('name', 'country', 'description', 'cost_of_living', 'status', 'date_added')
    list_display_links = ('name', 'country', 'description', 'cost_of_living', 'status', 'date_added')
    list_filter = ('name', 'country', 'description', 'cost_of_living', 'status', 'date_added')
    search_fields = ('name', 'description', 'cost_of_living', 'status', 'date_added')


admin.site.register(AirStatus)
admin.site.register(Continents)
admin.site.register(ListOfCities)
# admin.site.register(Countries, CountriesAdmin)
# admin.site.register(Cities, CitiesAdmin)
