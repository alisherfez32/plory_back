from django.shortcuts import render
from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Visit, FilterBy
from .serializers import VisitSerializer


class ListVisits(APIView):
    def get(self, request, format=None):
        visits = Visit.objects.all()
        serializer = VisitSerializer(visits, many=True)
        return Response(serializer.data)


class CityVisits(APIView):
    def get_object(self, city_slug):
        try:
            q = city_slug.capitalize()
            return Visit.objects.filter(city__name=q)
        except Visit.DoesNotExist:
            raise Http404

    def get(self, request, city_slug, format=None):
        visits_in_city = self.get_object(city_slug)
        serializer = VisitSerializer(visits_in_city, many=True)
        return Response(serializer.data)