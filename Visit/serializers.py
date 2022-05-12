from rest_framework import serializers

from .models import Visit


class VisitSerializer(serializers.ModelSerializer):
    city = serializers.StringRelatedField()

    class Meta:
        model = Visit

        fields = (
            "id",
            "city",
            "name",
            "url_on_map",
            "entry_fee",
            "description",
            "get_image",
            "best_time_togo"
        )