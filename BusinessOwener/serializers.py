from rest_framework import serializers

from . import models


class BusinessTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.BusinessType
        fields = [
            "id",
            "last_updated",
            "name",
            "created",
        ]

class storeprofileSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.storeprofile
        fields = [
            "BID",
            "BPinCode",
            "BAddressLine1",
            "last_updated",
            "BAddressLine2",
            "BStoreName",
            "created",
        ]

class stroetimingSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.stroetiming
        fields = [
            "created",
            "last_updated",
            "Time",
        ]
