from django.shortcuts import render
from django.http import Http404


from rest_framework.views import APIView
from rest_framework.response import Response

from .models import CostOfLiving
from .serializers import CostOfLivingsSerializer


class ListCostOfLiving(APIView):
    def get(self, request, format=None):
        cost_of_living = CostOfLiving.objects.all()
        serializer = CostOfLivingsSerializer(cost_of_living, many=True)
        return Response(serializer.data)


class CountryCostOfLiving(APIView):
    def get_object(self, country_slug):
        try:
            q = country_slug.capitalize()
            return CostOfLiving.objects.get(country__name=q)
        except CostOfLiving.DoesNotExist:
            raise Http404

    def get(self, request, country_slug, format=None):
        costs_in_country = self.get_object(country_slug)
        serializer = CostOfLivingsSerializer(costs_in_country)
        return Response(serializer.data)