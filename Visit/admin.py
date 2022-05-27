from django.contrib import admin

from .models import Visit, FilterBy, District

admin.site.register(FilterBy)
admin.site.register(Visit)
admin.site.register(District)
