from django.contrib import admin

from .models import CostOfLiving, Filters, Costs

admin.site.register(CostOfLiving)
admin.site.register(Filters)
admin.site.register(Costs)
