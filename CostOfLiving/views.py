from django.shortcuts import render
from django.http import Http404
from rest_framework.decorators import api_view

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Filters, Costs
from .serializers import CostSerializer, FilterSerializer


class ListCostOfLiving(APIView):
    def get(self, request, format=None):
        cost_of_living = Costs.objects.all()
        serializer = CostSerializer(cost_of_living, many=True)
        return Response(serializer.data)


class ListFilter(APIView):
    def get(self, request, format=None):
        filters = Filters.objects.all()
        serializer = FilterSerializer(filters, many=True)
        return Response(serializer.data)


class CityCosts(APIView):
    def get_object(self, city_slug):
        try:
            q = city_slug.capitalize()
            return Costs.objects.filter(city__name=q)
        except Costs.DoesNotExist:
            raise Http404

    def get(self, request, city_slug, format=None):
        rents_in_city = self.get_object(city_slug)
        serializer = CostSerializer(rents_in_city, many=True)
        return Response(serializer.data)




@api_view(['POST'])
def filter_by(request):
    city_slug = request.data.get('city_slug', '')
    filters = request.data.get('filter_by', [])
    q = city_slug.capitalize()
    filtered_costs = Costs.objects.filter(city__name=q)

    for str in filters:
        b = str.capitalize()
        filtered_costs = filtered_costs.filter(filter_by__name=b)

    filter_serializer = CostSerializer(filtered_costs, many=True)

    return Response(filter_serializer.data)
