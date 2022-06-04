from django.conf import settings
from django.db import models

from Cities.models import ListOfCities
from taggit.managers import TaggableManager


class FilterBy(models.Model):
    tag = models.CharField(unique=True, max_length=60)

    class Meta:
        ordering = ['-tag', ]

    def __str__(self):
        return self.tag


class District(models.Model):
    name = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_added', ]

    def __str__(self):
        return self.name


class Visit(models.Model):
    name = models.CharField(max_length=100)
    city = models.ForeignKey(ListOfCities, related_name='visit', on_delete=models.CASCADE)
    url_on_map = models.URLField()
    district = models.ForeignKey(District, null=True, blank=True, default=1, on_delete=models.CASCADE)
    entry_fee = models.DecimalField(max_digits=20, decimal_places=0)
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(FilterBy, )
    description = models.TextField(null=True)
    order = models.PositiveIntegerField(default=0, blank=False, null=False)

    # best_time_togo = models.TextField(null=True)
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