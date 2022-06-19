from adminsortable2.admin import SortableAdminMixin
from django.contrib import admin

from .models import Filters, Rent, URL


@admin.register(Rent)
class RentAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('name_of_company', 'date_added',)
    list_display_links = ('name_of_company', 'date_added',)
    list_filter = ('name_of_company', 'date_added',)
    search_fields = ('name_of_company', 'date_added',)


admin.site.register(Filters)
admin.site.register(URL)
# admin.site.register(Rent, RentAdmin)
