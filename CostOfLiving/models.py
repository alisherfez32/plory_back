from django.db import models

from Cities.models import ListOfCities
from taggit.managers import TaggableManager


class Filters(models.Model):
    name = models.CharField(unique=True, max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_added', ]

    def __str__(self):
        return self.name


class Costs(models.Model):
    name = models.CharField(unique=True, max_length=200)
    city = models.OneToOneField(ListOfCities, related_name='cost_of_living_2', on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_added', ]

    def __str__(self):
        return self.name


class CostOfLiving(models.Model):
    city = models.OneToOneField(ListOfCities, unique=True, related_name='cost_of_living', on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)
    water = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    coffee = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    dinner = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    lunch = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    breakfast = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    taxi = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    cheapest_meal = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    coke = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    bigmac_index = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    mid_restaurant = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    # Eating Out
    rice = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    eggs = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    milk = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    chicken = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    bread = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    potatoes = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    tomatoes = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    onions = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    carrots = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    apples = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    beef = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    cheese = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    flour = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    sugar = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    oranges = models.DecimalField(default=0, max_digits=12, decimal_places=2)

    # Utilities
    shorts = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    t_shirt = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    doctor_check = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    haircut = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    shampoo = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    deodorant = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    toothpaste = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    toilet = models.DecimalField(default=0, max_digits=12, decimal_places=2)

    tag = TaggableManager()

    class Meta:
        ordering = ['-date_added', ]

    def __str__(self):
        q = str(self.city)
        return q