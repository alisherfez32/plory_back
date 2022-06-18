from django.http import Http404
from django.shortcuts import render
from rest_framework.decorators import api_view

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import CommonApps, Filters
from .serializers import AppSerializer, FilterSerializer


class ListApps(APIView):
    def get(self, request, format=None):
        list_apps = CommonApps.objects.all()
        serializer = AppSerializer(list_apps, many=True)
        return Response(serializer.data)


class ListFilter(APIView):
    def get(self, request, format=None):
        filters = Filters.objects.all()
        serializer = FilterSerializer(filters, many=True)
        return Response(serializer.data)


class CountryWithApps(APIView):
    def get_object(self, country_slug):
        try:
            q = country_slug.capitalize()
            return CommonApps.objects.filter(country__name=q)
        except CommonApps.DoesNotExist:
            raise Http404

    def get(self, request, country_slug, format=None):
        countries_with_apps = self.get_object(country_slug)
        serializer = AppSerializer(countries_with_apps, many=True)
        return Response(serializer.data)


@api_view(['POST'])
def filter_by(request):
    country_slug = request.data.get('country_slug', '')
    filters = request.data.get('filter_by', [])
    q = country_slug.capitalize()
    filtered_apps = CommonApps.objects.filter(country__name=q)

    for str in filters:
        b = str.capitalize()
        filtered_apps = filtered_apps.filter(filter_by__name=b)

    filter_serializer = AppSerializer(filtered_apps, many=True)

    return Response(filter_serializer.data)

