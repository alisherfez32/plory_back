from django.conf import settings
from django.db import models
from django.template.defaultfilters import slugify
from Cities.models import Countries
from taggit.managers import TaggableManager


class Filters(models.Model):
    name = models.CharField(unique=True, max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_added', ]

    def __str__(self):
        return self.name


class Status(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        ordering = ['name', ]

    def __str__(self):
        if not self.name:
            return ""
        return self.name


class CountryFood(models.Model):
    name = models.CharField(max_length=200)
    filter_by = models.ManyToManyField(Filters, blank=True, null=True, )
    slug = models.SlugField(blank=True)
    status = models.ForeignKey(Status, null=True, blank=True, on_delete=models.CASCADE)
    country = models.ForeignKey(Countries, related_name='food', on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)
    # price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    order = models.PositiveIntegerField(default=0, blank=False, null=False)
    tag = TaggableManager()

    class Meta:
        ordering = ['order', ]

    def get_image(self):
        if self.image:
            return settings.MEDIA_HOST + self.image.url
        return ''

    def save(self, *args, **kwargs):  # new
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        g = str(self.country).lower()
        return f'/{g}/{self.slug}'