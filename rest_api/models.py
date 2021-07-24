from django.db import models
# from rest_framework.fields import JSONField


class Weather(models.Model):
    date = models.DateField()
    lat = models.DecimalField(decimal_places=4, max_digits=12)
    lon = models.DecimalField(decimal_places=4, max_digits=13)
    city = models.CharField(max_length=120)
    state = models.CharField(max_length=120)

    # the best decision for database could be postgres :/
    # temperatures = ArrayField(models.DecimalField(decimal_places=1, max_digits=24))

    temperatures = models.TextField(max_length=256)
