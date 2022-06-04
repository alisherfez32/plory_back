from django.db import models

from django.conf import settings
from django.db import models
from django.template.defaultfilters import slugify
from Cities.models import ListOfCities
from taggit.managers import TaggableManager


class Filters(models.Model):
    name = models.CharField(unique=True, max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_added', ]

    def __str__(self):
        return self.name


class District(models.Model):
    name = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_added', ]

    def __str__(self):
        return self.name


class EatPlaces(models.Model):
    name = models.CharField(max_length=200)
    city = models.ForeignKey(ListOfCities, related_name='eat_places', on_delete=models.CASCADE)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    filter_by = models.ManyToManyField(Filters, blank=True, null=True, )
    price = models.DecimalField(max_digits=20, decimal_places=0)
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    url = models.URLField()
    date_added = models.DateTimeField(auto_now_add=True)
    tag = TaggableManager()
    order = models.PositiveIntegerField(default=0, blank=False, null=False)

    class Meta:
        ordering = ['order', ]

    def get_image(self):
        if self.image:
            return settings.MEDIA_HOST + self.image.url
        return ''

    def __str__(self):
        return self.name