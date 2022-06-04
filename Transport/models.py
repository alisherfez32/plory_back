from django.conf import settings
from django.db import models

from Cities.models import Countries
from taggit.managers import TaggableManager


class TransportStatus(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        ordering = ['name', ]

    def __str__(self):
        if not self.name:
            return ""
        return self.name


class Transport(models.Model):
    name = models.CharField(max_length=100)
    country = models.ForeignKey(Countries, related_name='transport', on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)
    status = models.ForeignKey(TransportStatus, related_name='transport_status', on_delete=models.CASCADE)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    order = models.PositiveIntegerField(default=0, blank=False, null=False)
    # book = models.CharField(max_length=1000, blank=True)

    tag = TaggableManager()

    class Meta:
        ordering = ['order', ]

    def get_image(self):
        if self.image:
            return settings.MEDIA_HOST + self.image.url
        return ''

    def __str__(self):
        return str(self.country)