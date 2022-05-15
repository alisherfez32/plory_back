from rest_framework import serializers

from .models import Score


class ScoreSerializer(serializers.ModelSerializer):
    city = serializers.StringRelatedField()
    status = serializers.StringRelatedField()

    class Meta:
        model = Score

        fields = (
            "city",
            "status",
            "quality_of_life",
            "cost",
            "family_score",
            "internet",
            "fun",
            "temperature",
            "humidity",
            "air_quality",
            "safety",
            "lack_of_racism",
            "education_level",
            "free_wifi",
            "income_level",
            "english_speaking",
            "people_density",
            "walk_ability",
            "peace",
            "traffic_safety",
            "hospitals",
            "happiness",
            "places_towork_from",
            "heating",
            "friendly_to_foreigners",
            "freedom_of_speech",
            "female_frinedly",
            "startup_score",
            "note"
        )