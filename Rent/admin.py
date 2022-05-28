from django.contrib import admin

from .models import Status, Rent


class RentAdmin(admin.ModelAdmin):
    list_display = ('name_of_company', 'date_added', )
    list_display_links = ('name_of_company', 'date_added', )
    list_filter = ('name_of_company', 'date_added', )
    search_fields = ('name_of_company', 'date_added',)


admin.site.register(Status)
admin.site.register(Rent, RentAdmin)