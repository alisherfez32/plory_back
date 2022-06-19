from django.shortcuts import render

from django.shortcuts import render
from django.http import Http404


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import EatPlaces, Filters
from .serializers import EatSerializer, FilterSerializer


class ListFilter(APIView):
    def get(self, request, format=None):
        filters = Filters.objects.all()
        serializer = FilterSerializer(filters, many=True)
        return Response(serializer.data)


class ListOfEats(APIView):
    def get(self, request, format=None):
        eats = EatPlaces.objects.all()
        serializer = EatSerializer(eats, many=True)
        return Response(serializer.data)


class CityEats(APIView):
    def get_object(self, city_slug):
        try:
            q = city_slug.capitalize()
            return EatPlaces.objects.filter(city__name=q)
        except EatPlaces.DoesNotExist:
            raise Http404

    def get(self, request, city_slug, format=None):
        eats_in_city = self.get_object(city_slug)
        serializer = EatSerializer(eats_in_city, many=True)
        return Response(serializer.data)


@api_view(['POST'])
def filter_by(request):
    city_slug = request.data.get('city_slug', '')
    filters = request.data.get('filter_by', [])
    q = city_slug.capitalize()
    filtered_eats = EatPlaces.objects.filter(city__name=q)

    for str in filters:
        b = str.capitalize()
        filtered_eats = filtered_eats.filter(filter_by__name=b)

    filter_serializer = EatSerializer(filtered_eats, many=True)

    return Response(filter_serializer.data)