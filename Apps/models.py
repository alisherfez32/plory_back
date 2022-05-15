from django.db import models
from django.conf import settings

from Cities.models import Countries
from django.template.defaultfilters import slugify
from taggit.managers import TaggableManager


class CommonApps(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(blank=True)
    description = models.TextField()
    url = models.URLField()
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_added', ]

    def get_image(self):
        if self.image:
            return settings.MEDIA_HOST + self.image.url
        return ''

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):  # new
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)


class CountryApps(models.Model):
    country = models.OneToOneField(Countries, on_delete=models.CASCADE)
    slug = models.SlugField(blank=True, default=country)
    date_added = models.DateTimeField(auto_now_add=True)
    apps_for_what = models.TextField(blank=True, null=True)
    apps_and_websites = models.ManyToManyField(CommonApps, )
    tag = TaggableManager()

    class Meta:
        ordering = ['-date_added', ]

    def save(self, *args, **kwargs):  # new
        if not self.slug:
            self.slug = slugify(self.country)
        return super().save(*args, **kwargs)

    def __str__(self):
        return str(self.country)

