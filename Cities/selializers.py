from rest_framework import serializers
from .models import ListOfCities, Continents, Cities, Airports, Districts


class AirportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Airports
        fields = ("id", "name",)


class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = Districts
        fields = ("id", "name",)


class ContinentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Continents
        fields = (
            "id",
            "name",
            "get_absolute_url",
        )


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = ListOfCities
        fields = (
            "id",
            "name",
            "get_absolute_url",
        )


class CityDetailedSerializer(serializers.ModelSerializer):
    name = serializers.StringRelatedField()
    airports = AirportSerializer(many=True)
    districts = DistrictSerializer(many=True)

    class Meta:
        model = Cities
        fields = (
            "id",
            "name",
            "citi_main_slug",
            "cost_of_living", "free_wi_fi", "foreign_friendly", "english_speaking",
            "airports", "crime_rate",
            "governor", "population", "area", "districts",
            "get_absolute_url"
        )
