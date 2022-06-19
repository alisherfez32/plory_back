from rest_framework import serializers

from .models import Rent, Filters, URL


class FilterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Filters
        fields = (
            "id",
            "name",
            "used"
        )


class URLSerializer(serializers.ModelSerializer):
    name = serializers.StringRelatedField()

    class Meta:
        model = URL
        fields = (
            "id",
            "name",
            "url"
        )


class RentSerializer(serializers.ModelSerializer):
    city = serializers.StringRelatedField()
    status = serializers.StringRelatedField()
    filter_by = FilterSerializer(many=True)
    list_urls = URLSerializer(many=True)

    class Meta:
        model = Rent

        fields = (
            "id",
            "city",
            "status",
            "name_of_company",
            "get_image",
            "filter_by",
            "list_urls",
            "english_available",
        )
