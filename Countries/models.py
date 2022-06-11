from django.db import models
from django.conf import settings
from django.template.defaultfilters import slugify
from taggit.managers import TaggableManager

from Cities.models import Continents, ListOfCities


class Airports(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Seasons(models.Model):
    name = models.CharField(max_length=201)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Countries(models.Model):
    name = models.CharField(max_length=55, unique=True)
    country_slug = models.SlugField(null=True, blank=True, unique=True)
    continent = models.ForeignKey(Continents, on_delete=models.CASCADE, blank=True)
    list_cities = models.ManyToManyField(ListOfCities, )

    #Text
    text_near_flag = models.CharField(max_length=100, null=True)
    flag_image = models.ImageField(upload_to='uploads/flags/', blank=True, null=True, )
    # Main
    main_language = models.CharField(max_length=400, null=True)
    population = models.CharField(max_length=200, null=True)
    popular_foreign_langs = models.CharField(max_length=400, null=True)
    number_of_foreigners = models.CharField(max_length=200, null=True)

    # Airports
    airports = models.ManyToManyField(Airports, blank=True)
    climate = models.CharField(max_length=600, null=True)
    seasons = models.ManyToManyField(Seasons, blank=True, )

    # Political
    president = models.CharField(max_length=200, null=True)
    capital = models.ForeignKey(ListOfCities, related_name='capital', on_delete=models.CASCADE, )
    independence_day = models.CharField(max_length=200, null=True)
    number_of_state = models.CharField(max_length=100, null=True)
    life_expectency = models.DecimalField(max_digits=4, decimal_places=0, null=True)
    literacy_rate = models.DecimalField(max_digits=2, decimal_places=0, null=True)

    # FriendLy
    foreign_friendly = models.CharField(max_length=100, null=True)

    order = models.PositiveIntegerField(default=0, blank=False, null=False)
    tag = TaggableManager()

    class Meta:
        ordering = ('order',)

    def get_flag_image(self):
        if self.flag_image:
            return settings.MEDIA_HOST + self.flag_image.url
        return ''

    def save(self, *args, **kwargs):  # new        self.country_slug = self.tag
        if not self.country_slug:
            self.country_slug = slugify(self.name)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/{self.country_slug}'

