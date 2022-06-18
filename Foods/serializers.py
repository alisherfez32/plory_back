from rest_framework import serializers

from .models import CountryFood, Filters


class FilterSerializer(serializers.ModelSerializer):

    class Meta:
        model = Filters
        fields = (
            "id",
            "name",
            "used"
        )


class FoodsSerializer(serializers.ModelSerializer):
    country = serializers.StringRelatedField()
    filter_by = FilterSerializer(many=True)

    class Meta:
        model = CountryFood
        fields = (
            "id",
            "name",
            "filter_by",
            "country",
            "get_absolute_url",
            "description",
            "get_image",
            # "price",
        )