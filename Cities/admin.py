from adminsortable2.admin import SortableAdminMixin
from django.contrib import admin
from .models import Continents, ListOfCities, Cities, Airports, Districts


@admin.register(Cities)
class CitiesAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('name', 'cost_of_living', 'population', 'date_added')
    list_display_links = ('name', 'cost_of_living', 'population', 'date_added')
    list_filter = ('name', 'cost_of_living', 'population', 'date_added')
    search_fields = ('name', 'cost_of_living', 'population', 'date_added')


admin.site.register(Districts)
admin.site.register(Airports)
admin.site.register(Continents)
admin.site.register(ListOfCities)
# admin.site.register(Cities, CitiesAdmin)
