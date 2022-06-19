from adminsortable2.admin import SortableAdminMixin
from django.contrib import admin

from .models import Filters, Costs


@admin.register(Costs)
class CostOfLivingAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('id', 'date_added', 'name',)
    list_display_links = ('id', 'date_added', 'name',)
    list_filter = ('id', 'date_added', 'name',)
    search_fields = ('id', 'date_added',)

admin.site.register(Filters)
# admin.site.register(Costs)
