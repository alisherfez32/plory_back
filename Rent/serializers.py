from rest_framework import serializers

from .models import Rent


class RentSerializer(serializers.ModelSerializer):
    city = serializers.StringRelatedField()
    status = serializers.StringRelatedField()

    class Meta:
        model = Rent

        fields = (
            "id",
            "city",
            "status",
            "name_of_company",
            "get_image",
            "hotel",
            "guest_house",
            "apartment",
            "house"
        )