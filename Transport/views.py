from django.shortcuts import render
from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Transport, Filters
from .serializers import TransportsSerializer, FilterSerializer


class ListTransports(APIView):
    def get(self, request, format=None):
        transports = Transport.objects.all()
        serializer = TransportsSerializer(transports, many=True)
        return Response(serializer.data)


class ListFilter(APIView):
    def get(self, request, format=None):
        filters = Filters.objects.all()
        serializer = FilterSerializer(filters, many=True)
        return Response(serializer.data)


class CountryTransports(APIView):
    def get_object(self, country_slug):
        try:
            q = country_slug.capitalize()
            return Transport.objects.filter(country__name=q)
        except Transport.DoesNotExist:
            raise Http404

    def get(self, request, country_slug, format=None):
        transports_in_country = self.get_object(country_slug)
        serializer = TransportsSerializer(transports_in_country, many=True)
        return Response(serializer.data)


@api_view(['POST'])
def filter_by(request):
    country_slug = request.data.get('country_slug', '')
    filters = request.data.get('filter_by', [])
    q = country_slug.capitalize()
    filtered_foods = Transport.objects.filter(country__name=q)

    for str in filters:
        b = str.capitalize()
        filtered_foods = filtered_foods.filter(filter_by__name=b)

    filter_serializer = TransportsSerializer(filtered_foods, many=True)

    return Response(filter_serializer.data)
