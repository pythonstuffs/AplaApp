from rest_framework import viewsets, permissions

from . import serializers
from . import models


class CountryViewSet(viewsets.ModelViewSet):
    """ViewSet for the Country class"""

    queryset = models.Country.objects.all()
    serializer_class = serializers.CountrySerializer
    permission_classes = [permissions.IsAuthenticated]


class StateViewSet(viewsets.ModelViewSet):
    """ViewSet for the State class"""

    queryset = models.State.objects.all()
    serializer_class = serializers.StateSerializer
    permission_classes = [permissions.IsAuthenticated]


class CityViewSet(viewsets.ModelViewSet):
    """ViewSet for the City class"""

    queryset = models.City.objects.all()
    serializer_class = serializers.CitySerializer
    permission_classes = [permissions.IsAuthenticated]


class LocalityViewSet(viewsets.ModelViewSet):
    """ViewSet for the Locality class"""

    queryset = models.Locality.objects.all()
    serializer_class = serializers.LocalitySerializer
    permission_classes = [permissions.IsAuthenticated]
