from django.contrib import admin

from .models import CommonApps, CountryApps

admin.site.register(CommonApps)
admin.site.register(CountryApps)