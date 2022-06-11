from rest_framework import serializers
from .models import MetaTag


class MetaSerializer(serializers.ModelSerializer):
    component = serializers.StringRelatedField()

    class Meta:
        model = MetaTag
        fields = (
            "title", "component", "content"
        )
