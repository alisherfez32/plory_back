from rest_framework import serializers

from .models import CommonApps, Filters


class FilterSerializer(serializers.ModelSerializer):

    class Meta:
        model = Filters
        fields = (
            "id",
            "name",
            "used"
        )


class AppSerializer(serializers.ModelSerializer):
    filter_by = FilterSerializer(many=True)

    class Meta:
        model = CommonApps

        fields = (
            "id",
            "name",
            "url",
            "ios_url",
            "android_url",
            "description",
            "get_image",
            "filter_by"
        )

