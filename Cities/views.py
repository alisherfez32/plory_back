from django.shortcuts import render
from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Countries, Cities, ListOfCities, Continents
from .selializers import CountrySerializer, CitySerializer, CityDetailedSerializer, ContinentSerializer


class ListContinents(APIView):
    def get(self, request, format=None):
        list_cities = Continents.objects.all()
        serializer = ContinentSerializer(list_cities, many=True)
        return Response(serializer.data)


class ListCities(APIView):
    def get(self, request, format=None):
        list_cities = ListOfCities.objects.all()
        serializer = CitySerializer(list_cities, many=True)
        return Response(serializer.data)


class CountyWithCities(APIView):
    def get(self, request, format=None):
        list_countries = Countries.objects.all()
        serializer = CountrySerializer(list_countries, many=True)
        return Response(serializer.data)


class CountryDetail(APIView):
    def get_object(self, country_clug):
        try:
            return Countries.objects.get(country_slug=country_clug)
        except Countries.DoesNotExist:
            raise Http404

    def get(self, request, country_slug, format=None):
        country = self.get_object(country_slug)
        serializer = CountrySerializer(country)
        return Response(serializer.data)


class ListCityDetails(APIView):
    def get(self, request, format=None):
        list_detailed_cities = Cities.objects.all()
        serializer = CityDetailedSerializer(list_detailed_cities, many=True)
        return Response(serializer.data)


class CountryCityDetailed(APIView):
    def get_object(self, country_slug):
        try:
            country_name = Countries.objects.get(country_slug=country_slug)
            return country_name.country.all()
        except Cities.DoesNotExist:
            raise Http404

    def get(self, request, country_slug, format=None):
        city_in_country = self.get_object(country_slug)
        serializer = CityDetailedSerializer(city_in_country, many=True)
        return Response(serializer.data)


class CityDetailed(APIView):
    def get_object(self, city_slug):
        try:
            # q = capitalize.capitalize()
            return Cities.objects.get(citi_main_slug=city_slug)
        except Cities.DoesNotExist:
            raise Http404

    def get(self, request, city_slug, format=None):
        city_detailed_1 = self.get_object(city_slug)
        serializer = CityDetailedSerializer(city_detailed_1)
        return Response(serializer.data)
