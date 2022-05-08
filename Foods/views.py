from django.shortcuts import render
from django.http import Http404


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

from Cities.models import Countries
from .models import CountryFood
from .serializers import FoodsSerializer


class ListOfFoods(APIView):
    def get(self, request, format=None):
        foods = CountryFood.objects.all()
        serializer = FoodsSerializer(foods, many=True)
        return Response(serializer.data)


class CountryListFood(APIView):
    def get_object(self, country_slug):
        try:
            q = country_slug.capitalize()
            return CountryFood.objects.filter(country__name=q)
        except CountryFood.DoesNotExist:
            raise Http404

    def get(self, request, country_slug, format=None):
        foods_in_country = self.get_object(country_slug)
        serializer = FoodsSerializer(foods_in_country, many=True)
        return Response(serializer.data)


