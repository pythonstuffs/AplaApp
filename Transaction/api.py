from rest_framework import viewsets, permissions

from . import serializers
from . import models


class PaymentStatusViewSet(viewsets.ModelViewSet):
    """ViewSet for the PaymentStatus class"""

    queryset = models.PaymentStatus.objects.all()
    serializer_class = serializers.PaymentStatusSerializer
    permission_classes = [permissions.IsAuthenticated]


class InvoiceViewSet(viewsets.ModelViewSet):
    """ViewSet for the Invoice class"""

    queryset = models.Invoice.objects.all()
    serializer_class = serializers.InvoiceSerializer
    permission_classes = [permissions.IsAuthenticated]


class TransactionModeViewSet(viewsets.ModelViewSet):
    """ViewSet for the TransactionMode class"""

    queryset = models.TransactionMode.objects.all()
    serializer_class = serializers.TransactionModeSerializer
    permission_classes = [permissions.IsAuthenticated]


class TransactionStatusViewSet(viewsets.ModelViewSet):
    """ViewSet for the TransactionStatus class"""

    queryset = models.TransactionStatus.objects.all()
    serializer_class = serializers.TransactionStatusSerializer
    permission_classes = [permissions.IsAuthenticated]


class OrderViewSet(viewsets.ModelViewSet):
    """ViewSet for the Order class"""

    queryset = models.Order.objects.all()
    serializer_class = serializers.OrderSerializer
    permission_classes = [permissions.IsAuthenticated]
