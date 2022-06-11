from adminsortable2.admin import SortableAdminMixin
from django.contrib import admin
from .models import AirStatus, Continents, ListOfCities


# @admin.register(Cities)
# class CitiesAdmin(SortableAdminMixin, admin.ModelAdmin):
#     list_display = ('name', 'country', 'description', 'cost_of_living', 'status', 'date_added')
#     list_display_links = ('name', 'country', 'description', 'cost_of_living', 'status', 'date_added')
#     list_filter = ('name', 'country', 'description', 'cost_of_living', 'status', 'date_added')
#     search_fields = ('name', 'description', 'cost_of_living', 'status', 'date_added')


admin.site.register(AirStatus)
admin.site.register(Continents)
admin.site.register(ListOfCities)
# admin.site.register(Cities, CitiesAdmin)
