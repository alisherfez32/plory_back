from django.http import Http404
from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import MetaTag
from .serializers import MetaSerializer


class Meta(APIView):
    def get(self, request, format=None):
        metas = MetaTag.objects.all()
        serializer = MetaSerializer(metas, many=True)
        return Response(serializer.data)


class MetaComponent(APIView):
    def get_object(self, component):
        try:
            # q = city_slug.capitalize()
            return MetaTag.objects.filter(component__name=component)
        except MetaTag.DoesNotExist:
            raise Http404

    def get(self, request, component, format=None):
        metas = self.get_object(component)
        serializer = MetaSerializer(metas, many=True)
        return Response(serializer.data)
