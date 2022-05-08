from rest_framework import serializers
from .models import Countries, ListOfCities, Continents, Cities


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

    # def create(self, validated_data):
    #     tracks_data = validated_data.pop('list_cities')
    #     name = Countries.objects.create(**validated_data)
    #     for track_data in tracks_data:
    #         ListOfCities.objects.create(name=name, **track_data)
    #     return name


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
