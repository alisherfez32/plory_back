from django.shortcuts import render
from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Images
from .serializers import ImageSerializer


class AllImages(APIView):
    def get(self, request, format=None):
        images = Images.objects.all()
        serializer = ImageSerializer(images, many=True)
        return Response(serializer.data)


class CountryImages(APIView):
    def get_object(self, country_slug):
        try:
            q = country_slug.capitalize()
            return Images.objects.filter(country__name=q)
        except Images.DoesNotExist:
            raise Http404

    def get(self, request, country_slug, format=None):
        images_in_country = self.get_object(country_slug)
        serializer = ImageSerializer(images_in_country, many=True)
        return Response(serializer.data)


class CityImages(APIView):
    def get_object(self, city_slug):
        try:
            # q = country_slug.capitalize()
            c = city_slug.capitalize()
            return Images.objects.filter(city__name=c)
        except Images.DoesNotExist:
            raise Http404

    def get(self, request, city_slug, format=None):
        images_in_country = self.get_object(city_slug)
        serializer = ImageSerializer(images_in_country, many=True)
        return Response(serializer.data)

