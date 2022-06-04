from adminsortable2.admin import SortableAdminMixin
from django.contrib import admin

from .models import Transport, TransportStatus


@admin.register(Transport)
class TransportAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('name', 'description', 'date_added',)
    list_display_links = ('name', 'description', 'date_added',)
    list_filter = ('name', 'description', 'date_added',)
    search_fields = ('name', 'description',)


# admin.site.register(Transport, TransportAdmin)
admin.site.register(TransportStatus)