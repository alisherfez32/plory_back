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
    water = models.DecimalField(default=0, max_digits=12, decimal_places=0)
    coffee = models.DecimalField(default=0, max_digits=12, decimal_places=0)
    dinner = models.DecimalField(default=0, max_digits=12, decimal_places=0)
    lunch = models.DecimalField(default=0, max_digits=12, decimal_places=0)
    breakfast = models.DecimalField(default=0, max_digits=12, decimal_places=0)
    taxi = models.DecimalField(default=0, max_digits=12, decimal_places=0)
    cheapest_meal = models.DecimalField(default=0, max_digits=12, decimal_places=0)
    coke = models.DecimalField(default=0, max_digits=12, decimal_places=0)
    bigmac_index = models.DecimalField(default=0, max_digits=12, decimal_places=0)
    mid_restaurant = models.DecimalField(default=0, max_digits=12, decimal_places=0)
    # Eating Out
    rice = models.DecimalField(default=0, max_digits=12, decimal_places=0)
    eggs = models.DecimalField(default=0, max_digits=12, decimal_places=0)
    milk = models.DecimalField(default=0, max_digits=12, decimal_places=0)
    chicken = models.DecimalField(default=0, max_digits=12, decimal_places=0)
    bread = models.DecimalField(default=0, max_digits=12, decimal_places=0)
    potatoes = models.DecimalField(default=0, max_digits=12, decimal_places=0)
    tomatoes = models.DecimalField(default=0, max_digits=12, decimal_places=0)
    onions = models.DecimalField(default=0, max_digits=12, decimal_places=0)
    carrots = models.DecimalField(default=0, max_digits=12, decimal_places=0)
    apples = models.DecimalField(default=0, max_digits=12, decimal_places=0)
    beef = models.DecimalField(default=0, max_digits=12, decimal_places=0)
    cheese = models.DecimalField(default=0, max_digits=12, decimal_places=0)
    flour = models.DecimalField(default=0, max_digits=12, decimal_places=0)
    sugar = models.DecimalField(default=0, max_digits=12, decimal_places=0)
    oranges = models.DecimalField(default=0, max_digits=12, decimal_places=0)

    # Utilities
    shorts = models.DecimalField(default=0, max_digits=12, decimal_places=0)
    t_shirt = models.DecimalField(default=0, max_digits=12, decimal_places=0)
    doctor_check = models.DecimalField(default=0, max_digits=12, decimal_places=0)
    haircut = models.DecimalField(default=0, max_digits=12, decimal_places=0)
    shampoo = models.DecimalField(default=0, max_digits=12, decimal_places=0)
    deodorant = models.DecimalField(default=0, max_digits=12, decimal_places=0)
    toothpaste = models.DecimalField(default=0, max_digits=12, decimal_places=0)
    toilet = models.DecimalField(default=0, max_digits=12, decimal_places=0)
    order = models.PositiveIntegerField(default=0, blank=False, null=False)

    tag = TaggableManager()

    class Meta:
        ordering = ['order', ]

    def __str__(self):
        q = str(self.city)
        return q