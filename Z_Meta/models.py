from django.db import models


class Components(models.Model):
    name = models.CharField(max_length=200, unique=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class MetaTag(models.Model):
    component = models.OneToOneField(Components, on_delete=models.CASCADE)
    title = models.TextField()
    content = models.TextField()
    order = models.PositiveIntegerField(default=0, blank=False, null=False)

    class Meta:
        ordering = ['order', ]
