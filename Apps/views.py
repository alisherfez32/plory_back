from django.http import Http404
from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import CommonApps, CountryApps
from .serializers import CommonAppSerializer, CountryAppSerializer


class ListApps(APIView):
    def get(self, request, format=None):
        list_apps = CommonApps.objects.all()
        serializer = CommonAppSerializer(list_apps, many=True)
        return Response(serializer.data)


class Apps(APIView):
    def get(self, request, format=None):
        countries_apps = CountryApps.objects.all()
        serializer = CountryAppSerializer(countries_apps, many=True)
        return Response(serializer.data)


class CountryWithApps(APIView):
    def get_object(self, country_slug):
        try:
            # q = country_slug.capitalize()
            return CountryApps.objects.filter(slug=country_slug)[:1]
        except CountryApps.DoesNotExist:
            raise Http404

    def get(self, request, country_slug, format=None):
        countries_with_apps = self.get_object(country_slug)
        serializer = CountryAppSerializer(countries_with_apps, many=True)
        return Response(serializer.data)
