from django.db import models
from django.conf import settings

from Countries.models import Countries
from django.template.defaultfilters import slugify
from taggit.managers import TaggableManager


class Filters(models.Model):
    name = models.CharField(unique=True, max_length=200)
    used = models.BooleanField(default=False)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_added', ]

    def __str__(self):
        return self.name


class CommonApps(models.Model):
    name = models.CharField(max_length=100, unique=True)
    country = models.ForeignKey(Countries, related_name='apps_in_ct', on_delete=models.CASCADE)
    slug = models.SlugField(blank=True)
    description = models.TextField(max_length=50)
    url = models.URLField(blank=True)
    ios_url = models.URLField(blank=True, null=True)
    android_url = models.URLField(blank=True, null=True)
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    order = models.PositiveIntegerField(default=0, blank=False, null=False)
    filter_by = models.ManyToManyField(Filters, blank=True, )
    tag = TaggableManager()

    class Meta:
        ordering = ['order', ]

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
