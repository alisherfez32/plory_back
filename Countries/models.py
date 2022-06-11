from django.db import models
from django.conf import settings
from django.template.defaultfilters import slugify
from taggit.managers import TaggableManager

from Cities.models import Continents, ListOfCities


class Countries(models.Model):
    name = models.CharField(max_length=55)
    population = models.DecimalField(max_digits=6, decimal_places=2)
    country_slug = models.SlugField(null=True, blank=True)
    location = models.ForeignKey(Continents, on_delete=models.CASCADE, default='Asia', blank=True)
    capital = models.ForeignKey(ListOfCities, related_name='capital', on_delete=models.CASCADE, )
    list_cities = models.ManyToManyField(ListOfCities, )
    order = models.PositiveIntegerField(default=0, blank=False, null=False)
    tag = TaggableManager()

    class Meta:
        ordering = ('order',)

    def save(self, *args, **kwargs):  # new
        self.search = self.tag
        if not self.country_slug:
            self.country_slug = slugify(self.name)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/{self.country_slug}'

