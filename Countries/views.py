
from django.shortcuts import render
from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Countries
from .serializers import CountrySerializer, CountryInfoSerializer


class CountyWithCities(APIView):
    def get(self, request, format=None):
        list_countries = Countries.objects.all()
        serializer = CountrySerializer(list_countries, many=True)
        return Response(serializer.data)


class CountryInfo(APIView):
    def get(self, request, format=None):
        list_countries = Countries.objects.all()
        serializer = CountryInfoSerializer(list_countries, many=True)
        return Response(serializer.data)


class CountryDetail(APIView):
    def get_object(self, country_clug):
        try:
            return Countries.objects.get(country_slug=country_clug)
        except Countries.DoesNotExist:
            raise Http404

    def get(self, request, country_slug, format=None):
        country = self.get_object(country_slug)
        serializer = CountryInfoSerializer(country)
        return Response(serializer.data)


