from django.conf import settings
from django.db import models

from Cities.models import ListOfCities
from taggit.managers import TaggableManager


class Status(models.Model):
    name = models.CharField(unique=True, max_length=200)

    class Meta:
        ordering = ['-name', ]

    def __str__(self):
        return self.name


class Rent(models.Model):
    name_of_company = models.CharField(max_length=200)
    city = models.ForeignKey(ListOfCities, related_name='rent', on_delete=models.CASCADE)
    status = models.ForeignKey(Status, related_name='rent_status', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    hotel = models.URLField(default='', blank=True)
    guest_house = models.URLField(default='', blank=True)
    apartment = models.URLField(default='', blank=True)
    house = models.URLField(default='', blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    order = models.PositiveIntegerField(default=0, blank=False, null=False)
    tag = TaggableManager()

    class Meta:
        ordering = ['order', ]

    def get_image(self):
        if self.image:
            return settings.MEDIA_HOST + self.image.url
        return ''

    def __str__(self):
        q = self.name_of_company + ' / ' + str(self.city)
        return q