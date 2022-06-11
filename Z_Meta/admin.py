from adminsortable2.admin import SortableAdminMixin
from django.contrib import admin
from .models import Components, MetaTag


@admin.register(MetaTag)
class VisitAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('component', 'title', 'content', )
    list_display_links = ('component', 'title', 'content', )
    list_filter = ('component', 'title', 'content', )
    search_fields = ('component', 'title', 'content', )


admin.site.register(Components)

