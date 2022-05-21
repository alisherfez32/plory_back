from rest_framework import serializers

from .models import CostOfLiving


class CostOfLivingsSerializer(serializers.ModelSerializer):
    city = serializers.StringRelatedField()

    class Meta:
        model = CostOfLiving

        fields = (
            "city",
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