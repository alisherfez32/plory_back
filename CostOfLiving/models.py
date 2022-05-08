from django.db import models

from Cities.models import Countries


class CostOfLiving(models.Model):
    country = models.OneToOneField(Countries, unique=True, related_name='cost_of_living', on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)
    water = models.DecimalField(max_digits=12, decimal_places=2)
    coffee = models.DecimalField(max_digits=12, decimal_places=2)
    dinner = models.DecimalField(max_digits=12, decimal_places=2)
    lunch = models.DecimalField(max_digits=12, decimal_places=2)
    breakfast = models.DecimalField(max_digits=12, decimal_places=2)
    taxi = models.DecimalField(max_digits=12, decimal_places=2)
    cheapest_meal = models.DecimalField(max_digits=12, decimal_places=2)
    coke = models.DecimalField(max_digits=12, decimal_places=2)
    bigmac_index = models.DecimalField(max_digits=12, decimal_places=2)
    mid_restaurant = models.DecimalField(max_digits=12, decimal_places=2)

    class Meta:
        ordering = ['-date_added', ]

    def __str__(self):
        q = str(self.country)
        return q