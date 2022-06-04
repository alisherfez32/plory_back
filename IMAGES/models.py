from django.conf import settings
from django.db import models

from Cities.models import Countries, ListOfCities
from taggit.managers import TaggableManager


class Images(models.Model):
    name = models.CharField(max_length=200)
    city = models.ForeignKey(ListOfCities, related_name='city_images', blank=True, on_delete=models.CASCADE)
    country = models.ForeignKey(Countries, related_name='country_images', on_delete=models.CASCADE)
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
