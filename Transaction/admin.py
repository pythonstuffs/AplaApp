from django.contrib import admin
from django import forms

from . import models


class PaymentStatusAdminForm(forms.ModelForm):

    class Meta:
        model = models.PaymentStatus
        fields = "__all__"


class PaymentStatusAdmin(admin.ModelAdmin):
    form = PaymentStatusAdminForm
    list_display = [
        "name",
        "created",
        "id",
        "last_updated",
    ]
    readonly_fields = [
        "name",
        "created",
        "id",
        "last_updated",
    ]


class InvoiceAdminForm(forms.ModelForm):

    class Meta:
        model = models.Invoice
        fields = "__all__"


class InvoiceAdmin(admin.ModelAdmin):
    form = InvoiceAdminForm
    list_display = [
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
    readonly_fields = [
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


class TransactionModeAdminForm(forms.ModelForm):

    class Meta:
        model = models.TransactionMode
        fields = "__all__"


class TransactionModeAdmin(admin.ModelAdmin):
    form = TransactionModeAdminForm
    list_display = [
        "id",
        "created",
        "last_updated",
        "name",
    ]
    readonly_fields = [
        "id",
        "created",
        "last_updated",
        "name",
    ]


class TransactionStatusAdminForm(forms.ModelForm):

    class Meta:
        model = models.TransactionStatus
        fields = "__all__"


class TransactionStatusAdmin(admin.ModelAdmin):
    form = TransactionStatusAdminForm
    list_display = [
        "created",
        "name",
        "last_updated",
        "id",
    ]
    readonly_fields = [
        "created",
        "name",
        "last_updated",
        "id",
    ]


class OrderAdminForm(forms.ModelForm):

    class Meta:
        model = models.Order
        fields = "__all__"


class OrderAdmin(admin.ModelAdmin):
    form = OrderAdminForm
    list_display = [
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
    readonly_fields = [
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


admin.site.register(models.PaymentStatus, PaymentStatusAdmin)
admin.site.register(models.Invoice, InvoiceAdmin)
admin.site.register(models.TransactionMode, TransactionModeAdmin)
admin.site.register(models.TransactionStatus, TransactionStatusAdmin)
admin.site.register(models.Order, OrderAdmin)
