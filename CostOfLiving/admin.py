from adminsortable2.admin import SortableAdminMixin
from django.contrib import admin

from .models import CostOfLiving, Filters, Costs


@admin.register(CostOfLiving)
class CostOfLivingAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('id', 'date_added', 'water',)
    list_display_links = ('id', 'date_added', 'water',)
    list_filter = ('id', 'date_added', 'water',)
    search_fields = ('id', 'date_added',)


# admin.site.register(CostOfLiving, CostOfLivingAdmin)
admin.site.register(Filters)
admin.site.register(Costs)
