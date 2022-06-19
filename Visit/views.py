from django.http import Http404
from django.shortcuts import render
from rest_framework.decorators import api_view

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Visit, Filters
from .serializers import VisitSerializer, FilterSerializer


class ListVisits(APIView):
    def get(self, request, format=None):
        visits = Visit.objects.all()
        serializer = VisitSerializer(visits, many=True)
        return Response(serializer.data)


class ListFilter(APIView):
    def get(self, request, format=None):
        filters = Filters.objects.all()
        serializer = FilterSerializer(filters, many=True)
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


@api_view(['POST'])
def filter_by(request):
    city_slug = request.data.get('city_slug', '')
    filters = request.data.get('filter_by', [])
    q = city_slug.capitalize()
    filtered_visits = Visit.objects.filter(city__name=q)

    for str in filters:
        b = str.capitalize()
        filtered_visits = filtered_visits.filter(filter_by__name=b)

    filter_serializer = VisitSerializer(filtered_visits, many=True)

    return Response(filter_serializer.data)