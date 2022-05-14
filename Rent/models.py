from django.db import models

from Cities.models import ListOfCities
from taggit.managers import TaggableManager


class Status(models.Model):
    name = models.CharField(unique=True, max_length=200)

    class Meta:
        ordering = ['-name', ]

    def __str__(self):
        return self.name


class Company(models.Model):
    name = models.CharField(unique=True, max_length=200)
    url_cp = models.URLField()

    class Meta:
        ordering = ['-name', ]

    def __str__(self):
        return self.name


class Rent(models.Model):
    name = models.CharField(max_length=200)
    city = models.ForeignKey(ListOfCities, related_name='rent', on_delete=models.CASCADE)
    url_of_rent = models.URLField()
    status = models.ForeignKey(Status, related_name='rent_status', on_delete=models.CASCADE)
    company = models.ForeignKey(Company, related_name='rent_company', on_delete=models.CASCADE)
    notes = models.TextField(null=True)
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    tag = TaggableManager()

    class Meta:
        ordering = ['-date_added', ]

    def get_image(self):
        if self.image:
            return 'http://127.0.0.1:8000' + self.image.url
        return ''

    def __str__(self):
        q = self.name + ' / ' + str(self.city)
        return q