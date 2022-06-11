from django.conf import settings
from django.db import models
from django.template.defaultfilters import slugify
from taggit.managers import TaggableManager

from Countries.models import Countries


class AirStatus(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        ordering = ['name', ]

    def __str__(self):
        if not self.name:
            return ""
        return self.name


class Continents(models.Model):
    name = models.CharField(max_length=50)
    area = models.DecimalField(max_digits=6, decimal_places=2)

    class Meta:
        ordering = ['name', ]

    def __str__(self):
        if not self.name:
            return ""
        return self.name

    def get_absolute_url(self):
        return f'/{self.name.lower()}'


class ListOfCities(models.Model):
    name = models.CharField(max_length=85, )
    city_slug = models.SlugField(max_length=50, blank=True, null=True)

    class Meta:
        ordering = ['name', ]

    def save(self, *args, **kwargs):  # new
        if not self.city_slug:
            self.city_slug = slugify(self.name)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/{self.city_slug}'


class Cities(models.Model):
    name = models.ForeignKey(ListOfCities, related_name='name_of_city', on_delete=models.CASCADE)
    citi_main_slug = models.SlugField(null=True, blank=True)
    country = models.ForeignKey(Countries, related_name='country', on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)
    cost_of_living = models.DecimalField(max_digits=6, decimal_places=2)
    status = models.ForeignKey(AirStatus, related_name='status_of_air', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    order = models.PositiveIntegerField(default=0, blank=False, null=False)
    tag = TaggableManager()

    class Meta:
        ordering = ['order', ]

    def __str__(self):
        return str(self.name)

    def get_image(self):
        if self.image:
            return settings.MEDIA_HOST + self.image.url
        return ''

    def save(self, *args, **kwargs):  # new
        if not self.citi_main_slug:
            self.citi_main_slug = slugify(self.name)
        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        g = str(self.country).lower()
        return f'/{g}/{self.citi_main_slug}'
