from django.urls import path
from rest_api.views import WeatherViewSet, WeatherDetail


urlpatterns = [
    path('weather/', WeatherViewSet.as_view()),
    path('weather/<int:pk>/', WeatherDetail.as_view())
]
