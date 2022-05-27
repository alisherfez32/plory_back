from rest_framework import serializers

from .models import Transport


class TransportsSerializer(serializers.ModelSerializer):
    country = serializers.StringRelatedField()
    status = serializers.StringRelatedField()

    class Meta:
        model = Transport

        fields = (
            "id",
            "country",
            "name",
            "status",
            "description",
            "get_image",
            # "book"
        )