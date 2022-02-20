from django.contrib import admin
from django import forms

from . import models


class BusinessTypeAdminForm(forms.ModelForm):

    class Meta:
        model = models.BusinessType
        fields = "__all__"


class BusinessTypeAdmin(admin.ModelAdmin):
    form = BusinessTypeAdminForm
    list_display = [
        "id",
        "last_updated",
        "name",
        "created",
    ]
    readonly_fields = [
        "id",
        "last_updated",
        "name",
        "created",
    ]


class storeprofileAdminForm(forms.ModelForm):

    class Meta:
        model = models.storeprofile
        fields = "__all__"


class storeprofileAdmin(admin.ModelAdmin):
    form = storeprofileAdminForm
    list_display = [
        "BID",
        "BPinCode",
        "BAddressLine1",
        "last_updated",
        "BAddressLine2",
        "BStoreName",
        "created",
    ]
    readonly_fields = [
        "BID",
        "BPinCode",
        "BAddressLine1",
        "last_updated",
        "BAddressLine2",
        "BStoreName",
        "created",
    ]


class stroetimingAdminForm(forms.ModelForm):

    class Meta:
        model = models.stroetiming
        fields = "__all__"


class stroetimingAdmin(admin.ModelAdmin):
    form = stroetimingAdminForm
    list_display = [
        "created",
        "last_updated",
        "Time",
    ]
    readonly_fields = [
        "created",
        "last_updated",
        "Time",
    ]


admin.site.register(models.BusinessType, BusinessTypeAdmin)
admin.site.register(models.storeprofile, storeprofileAdmin)
admin.site.register(models.stroetiming, stroetimingAdmin)
