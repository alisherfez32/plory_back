from django.db import models
from django.template.defaultfilters import slugify
from Cities.models import Countries
from taggit.managers import TaggableManager


class CountryFood(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(blank=True)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    country = models.ForeignKey(Countries, related_name='food', on_delete=models.CASCADE)
    tag = TaggableManager()


    class Meta:
        ordering = ['-date_added', ]

    def get_image(self):
        if self.image:
            return 'http://127.0.0.1:8000' + self.image.url
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