from django.shortcuts import render
from django.views import generic
from django.contrib.gis.geos import fromstr, Point
from django.contrib.gis.db.models.functions import Distance
from .models import Shop

longitude = 13.0180847
latitude = 80.1784775
user_location = Point(longitude, latitude, srid=4326)


# Class-based views are an alternative way to implement views as Python classes instead of functions.
# They are used to handle common use cases in web development without re-inventing the wheel.
class Home(generic.ListView):
    model = Shop
    context_object_name = 'shops'
    # To get the nearby shops, you simply use .annotate() to annotate each object on the returned queryset with a
    # distance annotation that’s calculated using Distance(), available from GeoDjango, between the location of each
    # shop and the user’s location.
    queryset = Shop.objects.annotate(distance=Distance('location', user_location)).order_by('distance')[0:6]
    template_name = 'shops/index.html'


