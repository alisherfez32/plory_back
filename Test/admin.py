from adminsortable2.admin import SortableAdminMixin
from django.contrib import admin

from .models import Test


@admin.register(Test)
class TestAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('name', 'comments', )
    list_display_links = ('name', 'comments', )
    list_filter = ('name', 'comments',)
    search_fields = ('name', 'comments',)