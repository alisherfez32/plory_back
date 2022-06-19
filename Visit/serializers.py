from rest_framework import serializers

from .models import Visit, Filters


class FilterSerializer(serializers.ModelSerializer):

    class Meta:
        model = Filters
        fields = (
            "id",
            "name",
            "used"
        )


class VisitSerializer(serializers.ModelSerializer):
    city = serializers.StringRelatedField()
    district = serializers.StringRelatedField()
    filter_by = FilterSerializer(many=True)

    class Meta:
        model = Visit

        fields = (
            "id",
            "city",
            "district",
            "name",
            "filter_by",
            "url_on_map",
            "entry_fee",
            "description",
            "get_image",
        )