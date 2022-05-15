from rest_framework import serializers

from .models import CostOfLiving


class CostOfLivingsSerializer(serializers.ModelSerializer):
    country = serializers.StringRelatedField()

    class Meta:
        model = CostOfLiving

        fields = (
            "country",
            "water",
            "coffee",
            "dinner",
            "lunch",
            "breakfast",
            "taxi",
            "cheapest_meal",
            "coke",
            "bigmac_index",
            "mid_restaurant",
        )