from rest_framework import viewsets, permissions

from . import serializers
from . import models


class profileViewSet(viewsets.ModelViewSet):
    """ViewSet for the profile class"""

    queryset = models.profile.objects.all()
    serializer_class = serializers.profileSerializer
    permission_classes = [permissions.IsAuthenticated]
