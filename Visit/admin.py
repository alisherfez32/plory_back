from adminsortable2.admin import SortableAdminMixin
from django.contrib import admin

from .models import Visit, Filters, District


@admin.register(Visit)
class VisitAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('name', 'entry_fee', 'description', )
    list_display_links = ('name', 'entry_fee', 'description', )
    list_filter = ('name', 'entry_fee', 'description', )
    search_fields = ('name', 'entry_fee', 'description')


admin.site.register(Filters)
# admin.site.register(Visit, VisitAdmin)
admin.site.register(District)
