from rest_framework import viewsets, permissions

from . import serializers
from . import models


class BusinessTypeViewSet(viewsets.ModelViewSet):
    """ViewSet for the BusinessType class"""

    queryset = models.BusinessType.objects.all()
    serializer_class = serializers.BusinessTypeSerializer
    permission_classes = [permissions.IsAuthenticated]


class storeprofileViewSet(viewsets.ModelViewSet):
    """ViewSet for the storeprofile class"""

    queryset = models.storeprofile.objects.all()
    serializer_class = serializers.storeprofileSerializer
    permission_classes = [permissions.IsAuthenticated]


class stroetimingViewSet(viewsets.ModelViewSet):
    """ViewSet for the stroetiming class"""

    queryset = models.stroetiming.objects.all()
    serializer_class = serializers.stroetimingSerializer
    permission_classes = [permissions.IsAuthenticated]
