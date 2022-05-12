from django.shortcuts import render
from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Score
from .serializers import ScoreSerializer


class ListScores(APIView):
    def get(self, request, format=None):
        transports = Score.objects.all()
        serializer = ScoreSerializer(transports, many=True)
        return Response(serializer.data)


class CityScores(APIView):
    def get_object(self, city_slug):
        try:
            q = city_slug.capitalize()
            return Score.objects.filter(city__name=q)[:1]
        except Score.DoesNotExist:
            raise Http404

    def get(self, request, city_slug, format=None):
        transports_in_country = self.get_object(city_slug)
        serializer = ScoreSerializer(transports_in_country, many=True)
        return Response(serializer.data)
