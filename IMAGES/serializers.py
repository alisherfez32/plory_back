from rest_framework import serializers

from .models import Images


class ImageSerializer(serializers.ModelSerializer):
    city = serializers.StringRelatedField()
    country = serializers.StringRelatedField()

    class Meta:
        model = Images

        fields = (
            "id",
            "name",
            "country",
            "city",
            "notes",
            "get_image",
        )
