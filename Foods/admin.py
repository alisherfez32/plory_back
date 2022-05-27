from django.contrib import admin

from .models import CountryFood, Status, Filters

admin.site.register(CountryFood)
admin.site.register(Status)
admin.site.register(Filters)
