from rest_framework import serializers

from . import models


class profileSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.profile
        fields = [
            "slug",
            "created",
            "MobileNumber",
            "birthday",
            "profileimage",
            "last_updated",
        ]
