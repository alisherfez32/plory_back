from rest_framework import serializers

from .models import Rent


class RentSerializer(serializers.ModelSerializer):
    city = serializers.StringRelatedField()
    company = serializers.StringRelatedField()
    status = serializers.StringRelatedField()

    class Meta:
        model = Rent

        fields = (
            "id",
            "city",
            "name",
            "company",
            "status",
            "notes",
            "get_image",
            "url_of_rent",
        )