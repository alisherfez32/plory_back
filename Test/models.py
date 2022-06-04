from django.db import models


class Test(models.Model):
    name = models.CharField(max_length=200)
    comments = models.IntegerField(default=0)
    time = models.TimeField(blank=True, null=True)

    class Meta:
        ordering = ['comments']

    def __str__(self):
        return self.name
