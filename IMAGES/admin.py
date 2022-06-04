from adminsortable2.admin import SortableAdminMixin
from django.contrib import admin

from .models import Images


@admin.register(Images)
class ImagesAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('name', 'notes', 'date_added')
    list_display_links = ('name', 'notes', 'date_added')
    list_filter = ('name', 'notes', 'date_added')
    search_fields = ('name', 'notes', 'date_added')


# admin.site.register(Images, ImagesAdmin)
