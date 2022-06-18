from rest_framework import serializers

from .models import Transport, Filters


class FilterSerializer(serializers.ModelSerializer):

    class Meta:
        model = Filters
        fields = (
            "id",
            "name",
            "used"
        )


class TransportsSerializer(serializers.ModelSerializer):
    country = serializers.StringRelatedField()
    status = serializers.StringRelatedField()
    filter_by = FilterSerializer(many=True)

    class Meta:
        model = Transport

        fields = (
            "id",
            "country",
            "name",
            "status",
            "description",
            "get_image",
            "filter_by",
            # "book"
        )