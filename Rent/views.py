from django.shortcuts import render
from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Rent
from .serializers import RentSerializer


class ListRents(APIView):
    def get(self, request, format=None):
        rents = Rent.objects.all()
        serializer = RentSerializer(rents, many=True)
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
