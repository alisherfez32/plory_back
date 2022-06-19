from django.conf import settings
from django.db import models

from Cities.models import ListOfCities
from taggit.managers import TaggableManager


class Filters(models.Model):
    name = models.CharField(unique=True, max_length=200)
    used = models.BooleanField(default=False)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_added', ]

    def __str__(self):
        return self.name


class URL(models.Model):
    name_to_recognize = models.CharField(max_length=200)
    name = models.ForeignKey(Filters, on_delete=models.CASCADE)
    url = models.URLField(default='', blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_added', ]

    def __str__(self):
        return self.name_to_recognize


class Rent(models.Model):
    name_of_company = models.CharField(max_length=200)
    city = models.ForeignKey(ListOfCities, related_name='rent', on_delete=models.CASCADE)
    filter_by = models.ManyToManyField(Filters, blank=True, default=1)
    list_urls = models.ManyToManyField(URL, default=1)
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    english_available = models.BooleanField(default=False)
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