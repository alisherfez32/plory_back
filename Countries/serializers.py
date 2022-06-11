from rest_framework import serializers
from .models import Countries
from Cities.selializers import CitySerializer


class CountrySerializer(serializers.ModelSerializer):
    list_cities = CitySerializer(many=True)
    capital = serializers.StringRelatedField()
    location = serializers.StringRelatedField()

    class Meta:
        model = Countries
        fields = (
            "id",
            "name",
            "population",
            "get_absolute_url",
            "list_cities",
            "location",
            "capital",
        )
