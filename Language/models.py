from django.db import models

# from Cities.models import Countries


class Languages(models.Model):
    name = models.CharField(max_length=200, unique=True)

    class Meta:
        ordering = ['name', ]

    def __str__(self):
        if not self.name:
            return ""
        return self.name
