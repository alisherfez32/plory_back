from django.conf import settings
from django.db import models
from django.template.defaultfilters import slugify
from taggit.managers import TaggableManager

# from Countries.models import Countries
# from Countries.models import Countries


class Airports(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        ordering = ['name', ]

    def __str__(self):
        if not self.name:
            return ""
        return self.name


class Districts(models.Model):
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
    citi_main_slug = models.SlugField(null=True, unique=True, blank=True)

    cost_of_living = models.DecimalField(max_digits=6, decimal_places=0)
    free_wi_fi = models.CharField(max_length=200, null=True)
    foreign_friendly = models.CharField(max_length=200, null=True)
    english_speaking = models.CharField(max_length=200, null=True)

    airports = models.ManyToManyField(Airports, blank=True)
    crime_rate = models.CharField(max_length=300, null=True)

    governor = models.CharField(max_length=100, null=True)
    population = models.CharField(max_length=200, null=True)
    area = models.CharField(max_length=200, null=True)
    districts = models.ManyToManyField(Districts, blank=True)

    date_added = models.DateTimeField(auto_now_add=True)
    order = models.PositiveIntegerField(default=0, blank=False, null=False)
    tag = TaggableManager()

    class Meta:
        ordering = ['order', ]

    def __str__(self):
        return str(self.name)

    def save(self, *args, **kwargs):  # new
        if not self.citi_main_slug:
            self.citi_main_slug = slugify(self.name)
        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        return f'/{self.citi_main_slug}'
