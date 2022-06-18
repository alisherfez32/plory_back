from django.shortcuts import render
from django.http import Http404


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

from Countries.models import Countries
from .models import CountryFood, Filters
from .serializers import FoodsSerializer, FilterSerializer


class ListFilter(APIView):
    def get(self, request, format=None):
        filters = Filters.objects.all()
        serializer = FilterSerializer(filters, many=True)
        return Response(serializer.data)


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


@api_view(['POST'])
def filter_by(request):
    country_slug = request.data.get('country_slug', '')
    filters = request.data.get('filter_by', [])
    q = country_slug.capitalize()
    filtered_foods = CountryFood.objects.filter(country__name=q)

    for str in filters:
        b = str.capitalize()
        filtered_foods = filtered_foods.filter(filter_by__name=b)

    filter_serializer = FoodsSerializer(filtered_foods, many=True)

    return Response(filter_serializer.data)



