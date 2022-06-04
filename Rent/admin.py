from adminsortable2.admin import SortableAdminMixin
from django.contrib import admin

from .models import Status, Rent


@admin.register(Rent)
class RentAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('name_of_company', 'date_added',)
    list_display_links = ('name_of_company', 'date_added',)
    list_filter = ('name_of_company', 'date_added',)
    search_fields = ('name_of_company', 'date_added',)


admin.site.register(Status)
# admin.site.register(Rent, RentAdmin)
