from django.db import models
from django.conf import settings
from django.template.defaultfilters import slugify
from taggit.managers import TaggableManager

from Cities.models import Continents, ListOfCities


class Countries(models.Model):
    name = models.CharField(max_length=55)
    country_slug = models.SlugField(null=True, blank=True)
    continent = models.ForeignKey(Continents, on_delete=models.CASCADE, blank=True)
    capital = models.ForeignKey(ListOfCities, related_name='capital', on_delete=models.CASCADE, )
    list_cities = models.ManyToManyField(ListOfCities, )
    order = models.PositiveIntegerField(default=0, blank=False, null=False)
    tag = TaggableManager()

    class Meta:
        ordering = ('order',)

    def save(self, *args, **kwargs):  # new        self.country_slug = self.tag
        if not self.country_slug:
            self.country_slug = slugify(self.name)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/{self.country_slug}'

