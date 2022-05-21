from rest_framework import serializers

from .models import EatPlaces


class EatSerializer(serializers.ModelSerializer):
    city = serializers.StringRelatedField()
    district = serializers.StringRelatedField()

    class Meta:
        model = EatPlaces

        fields = (
            "id",
            "name",
            "city",
            "district",
            "price",
            "get_image",
            "url",
        )