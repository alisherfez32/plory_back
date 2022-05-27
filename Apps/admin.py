from django.contrib import admin

from .models import CommonApps, CountryApps, Filters

admin.site.register(CommonApps)
admin.site.register(CountryApps)
admin.site.register(Filters)
