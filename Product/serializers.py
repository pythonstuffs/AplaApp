from rest_framework import serializers

from . import models


class Product_CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Product_Category
        fields = [
            "last_updated",
            "name",
            "id",
            "created",
            "is_active",
        ]

class Product_SubCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Product_SubCategory
        fields = [
            "is_active",
            "Product_Category",
            "last_updated",
            "created",
            "id",
            "name",
        ]

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Product
        fields = [
            "PName",
            "PSellingPrice",
            "PAvailiblity",
            "PID",
            "PDelivery",
            "PSubCategory",
            "PActualPrice",
            "PCategory",
            "last_updated",
            "PUnit",
            "BID",
            "created",
            "PMargin",
            "POnBoardDate",
            "PImage",
        ]
