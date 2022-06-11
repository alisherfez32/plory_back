from rest_framework import serializers
from .models import Countries, Airports, Seasons
from Cities.selializers import CitySerializer, CityDetailedSerializer


class AirportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Airports
        fields = ("id", "name",)


class SeasonsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seasons
        fields = ("id", "name",)


class CountrySerializer(serializers.ModelSerializer):
    list_cities = CitySerializer(many=True)

    class Meta:
        model = Countries
        fields = (
            "id",
            "name",
            "get_absolute_url",
            "list_cities",
        )


class CountryInfoSerializer(serializers.ModelSerializer):
    list_cities = CitySerializer(many=True)
    capital = serializers.StringRelatedField()
    continent = serializers.StringRelatedField()
    airports = AirportSerializer(many=True)
    seasons = SeasonsSerializer(many=True)

    class Meta:
        model = Countries
        fields = (
            "id",
            "name", "country_slug", "continent", "list_cities",
            "text_near_flag", "get_flag_image",
            "main_language", "population", "popular_foreign_langs", "number_of_foreigners",
            "airports", "climate", "seasons",
            "president", "capital", "independence_day", "number_of_state", "life_expectency", "literacy_rate",
            "foreign_friendly"
        )
