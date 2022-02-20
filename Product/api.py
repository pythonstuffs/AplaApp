from rest_framework import viewsets, permissions

from . import serializers
from . import models


class Product_CategoryViewSet(viewsets.ModelViewSet):
    """ViewSet for the Product_Category class"""

    queryset = models.Product_Category.objects.all()
    serializer_class = serializers.Product_CategorySerializer
    permission_classes = [permissions.IsAuthenticated]


class Product_SubCategoryViewSet(viewsets.ModelViewSet):
    """ViewSet for the Product_SubCategory class"""

    queryset = models.Product_SubCategory.objects.all()
    serializer_class = serializers.Product_SubCategorySerializer
    permission_classes = [permissions.IsAuthenticated]


class ProductViewSet(viewsets.ModelViewSet):
    """ViewSet for the Product class"""

    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer
    permission_classes = [permissions.IsAuthenticated]
