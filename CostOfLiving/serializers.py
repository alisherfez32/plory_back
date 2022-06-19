from rest_framework import serializers

from .models import Costs, Filters


class FilterSerializer(serializers.ModelSerializer):

    class Meta:
        model = Filters
        fields = (
            "id",
            "name",
            "used"
        )


class CostSerializer(serializers.ModelSerializer):
    city = serializers.StringRelatedField()
    filter_by = FilterSerializer(many=True)

    class Meta:
        model = Costs
        fields = (
            "id",
            "price",
            "name",
            "filter_by",
            "city",

        )