from rest_framework import serializers

from .models import EatPlaces, Filters


class FilterSerializer(serializers.ModelSerializer):

    class Meta:
        model = Filters
        fields = (
            "id",
            "name",
            "used"
        )


class EatSerializer(serializers.ModelSerializer):
    city = serializers.StringRelatedField()
    district = serializers.StringRelatedField()
    filter_by = FilterSerializer(many=True)

    class Meta:
        model = EatPlaces

        fields = (
            "id",
            "name",
            "city",
            "district",
            "filter_by",
            "price",
            "get_image",
            "url",
        )