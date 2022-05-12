from django.contrib import admin

from .models import Visit, FilterBy

admin.site.register(FilterBy)
admin.site.register(Visit)