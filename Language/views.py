from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Languages
from .serializers import LanguageSerializer

class ListLanguages(APIView):
    def get(self, request, format=None):
        languages = Languages.objects.all()
        serializer = LanguageSerializer(languages, many=True)
        return Response(serializer.data)