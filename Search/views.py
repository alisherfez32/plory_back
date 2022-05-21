from django.db.models import Q
from django.http import Http404
from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Citeis and Countries
from Cities.models import Countries, Cities
from Cities.selializers import CountrySerializer, CityDetailedSerializer

# Apps
from Apps.models import CountryApps
from Apps.serializers import CountryAppSerializer

# Cost Of Living
from CostOfLiving.models import CostOfLiving
from CostOfLiving.serializers import CostOfLivingsSerializer

# Foods
from Foods.models import CountryFood
from Foods.serializers import FoodsSerializer

# IMAGES
# from IMAGES.models import Images(models.Model):

# Languages
from Language.models import Languages
from Language.serializers import LanguageSerializer

# Rent
from Rent.models import Rent
from Rent.serializers import RentSerializer

# Score
from Score.models import Score
from Score.serializers import ScoreSerializer

# Transport
from Transport.models import Transport
from Transport.serializers import TransportsSerializer

# Visit
from Visit.models import Visit
from Visit.serializers import VisitSerializer


@api_view(['POST'])
def search(request):
    query = request.data.get('query', '')
    query = query.lower()

    if query:
        countries = Countries.objects.filter(Q(tag__name=query))
        cities = Cities.objects.filter(Q(tag__name=query))
        # apps = CountryApps.objects.filter(Q(tag__name=query))
        costs = CostOfLiving.objects.filter(Q(tag__name=query))
        foods = CountryFood.objects.filter(Q(tag__name=query))
        # languages = Languages.objects.filter(Q(tag__name=query))
        rents = Rent.objects.filter(Q(tag__name=query))
        scores = Score.objects.filter(Q(tag__name=query))
        transports = Transport.objects.filter(Q(tag__name=query))
        visits = Visit.objects.filter(Q(tag__name=query))

        ct_serializer = CountrySerializer(countries, many=True)
        city_serializer = CityDetailedSerializer(cities, many=True)
        # app_serializer = CountryAppSerializer(apps, many=True)
        cost_serializer = CostOfLivingsSerializer(costs, many=True)
        food_serializer = FoodsSerializer(foods, many=True)
        # lang_srz = LanguageSerializer(languages, many=True)
        rent_srz = RentSerializer(rents, many=True)
        score_srz = ScoreSerializer(scores, many=True)
        trans_srz = TransportsSerializer(transports, many=True)
        visit_srz = VisitSerializer(visits, many=True)

        context = {
            "countries": ct_serializer.data,
            "cities": city_serializer.data,
            # "apps": app_serializer.data,
            "costs": cost_serializer.data,
            "foods": food_serializer.data,
            # "langs": lang_srz.data,
            "rents": rent_srz.data,
            "scores": score_srz.data,
            "transports": trans_srz.data,
            "visits": visit_srz.data
        }
        return Response(context)
    else:
        return Response({"search_info": []})
