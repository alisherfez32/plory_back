from rest_framework import serializers

from .models import Visit


class VisitSerializer(serializers.ModelSerializer):
    city = serializers.StringRelatedField()
    district = serializers.StringRelatedField()

    class Meta:
        model = Visit

        fields = (
            "id",
            "city",
            "district",
            "name",
            "url_on_map",
            "entry_fee",
            "description",
            "get_image",
        )