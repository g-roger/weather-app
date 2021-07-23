from django.urls import path
from rest_api.views import WeatherViewSet


urlpatterns = [
    path('weather/', WeatherViewSet.as_view())
]
