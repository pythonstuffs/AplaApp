from rest_framework import serializers

from . import models


class CountrySerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Country
        fields = [
            "last_updated",
            "id",
            "name",
            "created",
        ]

class StateSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.State
        fields = [
            "created",
            "id",
            "last_updated",
            "name",
        ]

class CitySerializer(serializers.ModelSerializer):

    class Meta:
        model = models.City
        fields = [
            "name",
            "id",
            "created",
            "last_updated",
        ]

class LocalitySerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Locality
        fields = [
            "id",
            "created",
            "last_updated",
            "name",
        ]
