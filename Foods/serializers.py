from rest_framework import serializers

from .models import CountryFood


class FoodsSerializer(serializers.ModelSerializer):
    country = serializers.StringRelatedField()
    class Meta:
        model = CountryFood
        fields = (
            "id",
            "name",
            "country",
            "get_absolute_url",
            "description",
            "get_image",
            "price",
        )