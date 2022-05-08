from rest_framework import serializers

from .models import CommonApps, CountryApps


class CommonAppSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommonApps

        fields = (
            "id",
            "name",
            "url",
            "description",
            "get_image",
        )


class CountryAppSerializer(serializers.ModelSerializer):
    country = serializers.StringRelatedField()
    apps_and_websites = CommonAppSerializer(many=True)

    class Meta:
        model = CountryApps

        fields = (
            "id",
            "country",
            "apps_for_what",
            "apps_and_websites"
        )