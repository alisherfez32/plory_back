from django.db import models

from Cities.models import ListOfCities


class FilterBy(models.Model):
    tag = models.CharField(unique=True, max_length=60)

    class Meta:
        ordering = ['-tag', ]

    def __str__(self):
        return self.tag


class Visit(models.Model):
    name = models.CharField(max_length=100)
    city = models.ForeignKey(ListOfCities, related_name='visit', on_delete=models.CASCADE)
    url_on_map = models.URLField()
    entry_fee = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(FilterBy, )
    description = models.TextField(null=True)
    best_time_togo = models.TextField(null=True)

    class Meta:
        ordering = ['-date_added', ]

    def get_image(self):
        if self.image:
            return 'http://127.0.0.1:8000' + self.image.url
        return ''

    def __str__(self):
        q = self.name + ' / ' + str(self.city)
        return q