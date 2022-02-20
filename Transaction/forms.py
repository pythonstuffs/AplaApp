from django import forms
from . import models


class PaymentStatusForm(forms.ModelForm):
    class Meta:
        model = models.PaymentStatus
        fields = [
            "name",
        ]


class InvoiceForm(forms.ModelForm):
    class Meta:
        model = models.Invoice
        fields = [
            "BID",
            "CID",
            "TransactionStatus",
            "TotalPrice",
            "BName",
            "PTransactionMode",
            "PaymentStatus",
        ]


class TransactionModeForm(forms.ModelForm):
    class Meta:
        model = models.TransactionMode
        fields = [
            "name",
        ]


class TransactionStatusForm(forms.ModelForm):
    class Meta:
        model = models.TransactionStatus
        fields = [
            "name",
        ]


class OrderForm(forms.ModelForm):
    class Meta:
        model = models.Order
        fields = [
            "TID",
            "PID",
            "PName",
            "PUnit",
            "PPrice",
            "PTotal",
        ]
