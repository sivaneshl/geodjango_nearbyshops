from django.contrib.gis.db import models


class Shop(models.Model):
    name = models.CharField(max_length=100)
    location = models.PointField()
    #  PointField, a GeoDjango-specific geometric field for storing a GEOS Point object
    #  that represents a pair of longitude and latitude coordinates.
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)

