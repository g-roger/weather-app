import json

from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_api.models import Weather
from rest_api.serializers import WeatherSerializer


class WeatherViewSet(APIView):
    def post(self, request):
        serializer = WeatherSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        sort = request.query_params.get('sort', None)
        city = request.query_params.getlist('city', None)
        date = request.query_params.get('date', None)

        query = Weather.objects

        if date:
            query = query.filter(date=date)

        if city:
            # iexact and icontains have problem with SQLITE
            query = query.filter(city__iregex=r'^(' + '?|'.join(city) + ')+')

        if sort:
            if sort == '-date':
                sort = '-date'
            else:
                sort = 'date'
            query = query.order_by(sort, 'id')
        else:
            query = query.order_by('id')

        serializer = WeatherSerializer(query.all(), many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class WeatherDetail(APIView):
    def get(self, request, pk):
        try:
            weather = Weather.objects.get(pk=pk)
            serializer = WeatherSerializer(weather)
            return Response(serializer.data)
        except Weather.DoesNotExist:
            raise Http404
