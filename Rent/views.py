from django.shortcuts import render
from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Rent, Filters
from .serializers import RentSerializer, FilterSerializer


class ListRents(APIView):
    def get(self, request, format=None):
        rents = Rent.objects.all()
        serializer = RentSerializer(rents, many=True)
        return Response(serializer.data)


class ListFilter(APIView):
    def get(self, request, format=None):
        filters = Filters.objects.all()
        serializer = FilterSerializer(filters, many=True)
        return Response(serializer.data)


class CityRents(APIView):
    def get_object(self, city_slug):
        try:
            q = city_slug.capitalize()
            return Rent.objects.filter(city__name=q)
        except Rent.DoesNotExist:
            raise Http404

    def get(self, request, city_slug, format=None):
        rents_in_city = self.get_object(city_slug)
        serializer = RentSerializer(rents_in_city, many=True)
        return Response(serializer.data)


@api_view(['POST'])
def filter_by(request):
    city_slug = request.data.get('city_slug', '')
    filters = request.data.get('filter_by', [])
    q = city_slug.capitalize()
    filtered_rents = Rent.objects.filter(city__name=q)

    for str in filters:
        b = str.capitalize()
        filtered_rents = filtered_rents.filter(filter_by__name=b)

    filter_serializer = RentSerializer(filtered_rents, many=True)

    return Response(filter_serializer.data)