from decimal import Decimal

from django.db import models

from django.core.validators import MinValueValidator, MaxValueValidator
from taggit.managers import TaggableManager

PERCENTAGE_VALIDATOR = [MinValueValidator(0), MaxValueValidator(100)]

from Cities.models import ListOfCities


class ScoreStatus(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        ordering = ['name', ]

    def __str__(self):
        if not self.name:
            return ""
        return self.name


class Score(models.Model):
    city = models.OneToOneField(ListOfCities, related_name='score', on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)
    quality_of_life = models.DecimalField(max_digits=3, decimal_places=0, default=Decimal(0),
                                         validators=PERCENTAGE_VALIDATOR)
    cost = models.DecimalField(max_digits=3, decimal_places=0, default=Decimal(0),
                                         validators=PERCENTAGE_VALIDATOR)
    family_score = models.DecimalField(max_digits=3, decimal_places=0, default=Decimal(0),
                                         validators=PERCENTAGE_VALIDATOR)
    internet = models.DecimalField(max_digits=3, decimal_places=0, default=Decimal(0),
                                         validators=PERCENTAGE_VALIDATOR)
    fun = models.DecimalField(max_digits=3, decimal_places=0, default=Decimal(0),
                                         validators=PERCENTAGE_VALIDATOR)
    temperature = models.DecimalField(max_digits=3, decimal_places=0, default=Decimal(0),
                                         validators=PERCENTAGE_VALIDATOR)
    humidity = models.DecimalField(max_digits=3, decimal_places=0, default=Decimal(0),
                                         validators=PERCENTAGE_VALIDATOR)
    air_quality = models.DecimalField(max_digits=3, decimal_places=0, default=Decimal(0),
                                         validators=PERCENTAGE_VALIDATOR)
    safety = models.DecimalField(max_digits=3, decimal_places=0, default=Decimal(0),
                                         validators=PERCENTAGE_VALIDATOR)
    lack_of_racism = models.DecimalField(max_digits=3, decimal_places=0, default=Decimal(0),
                                         validators=PERCENTAGE_VALIDATOR)
    education_level = models.DecimalField(max_digits=3, decimal_places=0, default=Decimal(0),
                                         validators=PERCENTAGE_VALIDATOR)
    free_wifi = models.DecimalField(max_digits=3, decimal_places=0, default=Decimal(0),
                                         validators=PERCENTAGE_VALIDATOR)
    income_level = models.DecimalField(max_digits=3, decimal_places=0, default=Decimal(0),
                                         validators=PERCENTAGE_VALIDATOR)
    english_speaking = models.DecimalField(max_digits=3, decimal_places=0, default=Decimal(0),
                                         validators=PERCENTAGE_VALIDATOR)
    people_density = models.DecimalField(max_digits=3, decimal_places=0, default=Decimal(0),
                                         validators=PERCENTAGE_VALIDATOR)
    walk_ability = models.DecimalField(max_digits=3, decimal_places=0, default=Decimal(0),
                                         validators=PERCENTAGE_VALIDATOR)
    peace = models.DecimalField(max_digits=3, decimal_places=0, default=Decimal(0),
                                         validators=PERCENTAGE_VALIDATOR)
    traffic_safety = models.DecimalField(max_digits=3, decimal_places=0, default=Decimal(0),
                                         validators=PERCENTAGE_VALIDATOR)
    hospitals = models.DecimalField(max_digits=3, decimal_places=0, default=Decimal(0),
                                         validators=PERCENTAGE_VALIDATOR)
    happiness = models.DecimalField(max_digits=3, decimal_places=0, default=Decimal(0),
                                         validators=PERCENTAGE_VALIDATOR)
    places_towork_from = models.DecimalField(max_digits=3, decimal_places=0, default=Decimal(0),
                                         validators=PERCENTAGE_VALIDATOR)
    heating = models.DecimalField(max_digits=3, decimal_places=0, default=Decimal(0),
                                         validators=PERCENTAGE_VALIDATOR)
    friendly_to_foreigners = models.DecimalField(max_digits=3, decimal_places=0, default=Decimal(0),
                                         validators=PERCENTAGE_VALIDATOR)
    freedom_of_speech = models.DecimalField(max_digits=3, decimal_places=0, default=Decimal(0),
                                         validators=PERCENTAGE_VALIDATOR)
    female_frinedly = models.DecimalField(max_digits=3, decimal_places=0, default=Decimal(0),
                                         validators=PERCENTAGE_VALIDATOR)
    startup_score = models.DecimalField(max_digits=3, decimal_places=0, default=Decimal(0),
                                         validators=PERCENTAGE_VALIDATOR)
    status = models.ForeignKey(ScoreStatus, related_name='score_status', on_delete=models.CASCADE)
    note = models.TextField(null=True)

    tag = TaggableManager()

    class Meta:
        ordering = ['-date_added', ]

    def __str__(self):
        return str(self.city)
