from django.contrib import admin

from .models import Company, Status, Rent

admin.site.register(Company)
admin.site.register(Status)
admin.site.register(Rent)