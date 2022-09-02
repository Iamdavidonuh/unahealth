from rest_framework import serializers

from records.models import UserGlucoseLevels


class UserGlucoseLevelsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserGlucoseLevels
        fields = "__all__"
