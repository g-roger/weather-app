from django.db import models


class Weather(models.Model):
    date = models.DateField()
    lat = models.DecimalField(decimal_places=4, max_digits=12)
    lon = models.DecimalField(decimal_places=4, max_digits=13)
    city = models.CharField(max_length=120)
    state = models.CharField(max_length=120)
