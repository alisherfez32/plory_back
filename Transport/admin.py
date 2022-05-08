from django.contrib import admin

from .models import Transport, TransportStatus

admin.site.register(Transport)
admin.site.register(TransportStatus)