from rest_framework import serializers
from .models import ListOfCities, Continents, Cities


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
    country = serializers.StringRelatedField()
    status = serializers.StringRelatedField()

    class Meta:
        model = Cities
        fields = (
            "id",
            "name",
            "citi_main_slug",
            "country",
            "description",
            "cost_of_living",
            "status",
            "get_image",
            "get_absolute_url"
        )
