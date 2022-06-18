from django.conf import settings
from django.db import models

from Countries.models import Countries
from taggit.managers import TaggableManager


class Filters(models.Model):
    name = models.CharField(unique=True, max_length=200)
    used = models.BooleanField(default=False)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_added', ]

    def __str__(self):
        return self.name


class Transport(models.Model):
    name = models.CharField(max_length=100)
    country = models.ForeignKey(Countries, default=1, related_name='transport', on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)
    filter_by = models.ManyToManyField(Filters, related_name='transport_filter')
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