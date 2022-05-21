from django.shortcuts import render

from django.shortcuts import render
from django.http import Http404


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import EatPlaces
from .serializers import EatSerializer


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
