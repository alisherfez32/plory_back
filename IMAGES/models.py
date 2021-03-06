from django.conf import settings
from django.db import models

from Cities.models import ListOfCities
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


class Images(models.Model):
    name = models.CharField(max_length=200)
    city = models.ForeignKey(ListOfCities, related_name='city_images', blank=True, on_delete=models.CASCADE)
    country = models.ForeignKey(Countries, default=1, related_name='country_images', on_delete=models.CASCADE)
    filter_by = models.ManyToManyField(Filters, related_name='filter_foods', default=1)
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    notes = models.TextField(null=True)
    order = models.PositiveIntegerField(default=0, blank=False, null=False)
    tag = TaggableManager()

    class Meta:
        ordering = ['order', ]

    def get_image(self):
        if self.image:
            return settings.MEDIA_HOST + self.image.url
        return ''

    def __str__(self):
        q = self.name + ' / ' + str(self.city)
        return q
