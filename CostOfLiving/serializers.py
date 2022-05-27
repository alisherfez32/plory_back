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
        #    Eating out
            "rice",
            "eggs",
            "milk",
            "chicken",
            "bread",
            "potatoes",
            "tomatoes",
            "onions",
            "carrots",
            "apples",
            "beef",
            "cheese",
            "flour",
            "sugar",
            "oranges",
        #     Utilities
            "shorts",
            "t_shirt",
            "doctor_check",
            "haircut",
            "shampoo",
            "deodorant",
            "toothpaste",
            "toilet",
        )