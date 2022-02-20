from rest_framework import serializers

from . import models


class PaymentStatusSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.PaymentStatus
        fields = [
            "name",
            "created",
            "id",
            "last_updated",
        ]

class InvoiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Invoice
        fields = [
            "TransactionStatus",
            "TID",
            "CID",
            "BID",
            "last_updated",
            "TotalPrice",
            "TransactionDate",
            "BName",
            "PTransactionMode",
            "PaymentStatus",
        ]

class TransactionModeSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.TransactionMode
        fields = [
            "id",
            "created",
            "last_updated",
            "name",
        ]

class TransactionStatusSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.TransactionStatus
        fields = [
            "created",
            "name",
            "last_updated",
            "id",
        ]

class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Order
        fields = [
            "created",
            "PName",
            "OID",
            "PUnit",
            "last_updated",
            "TID",
            "PID",
            "PTotal",
            "PPrice",
            "PTotal",
        ]
