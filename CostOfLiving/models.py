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


class Costs(models.Model):
    name = models.CharField(unique=True, max_length=200)
    city = models.ForeignKey(ListOfCities, related_name='cost_of_living', on_delete=models.CASCADE)
    filter_by = models.ManyToManyField(Filters, blank=True, )
    date_added = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(default=0, max_digits=12, decimal_places=0)
    tag = TaggableManager()
    order = models.PositiveIntegerField(default=0, blank=False, null=False)

    class Meta:
        ordering = ['order', ]

    def __str__(self):
        return self.name
