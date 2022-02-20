from django.contrib import admin
from django import forms

from . import models


class CountryAdminForm(forms.ModelForm):

    class Meta:
        model = models.Country
        fields = "__all__"


class CountryAdmin(admin.ModelAdmin):
    form = CountryAdminForm
    list_display = [
        "last_updated",
        "id",
        "name",
        "created",
    ]
    readonly_fields = [
        "last_updated",
        "id",
        "name",
        "created",
    ]


class StateAdminForm(forms.ModelForm):

    class Meta:
        model = models.State
        fields = "__all__"


class StateAdmin(admin.ModelAdmin):
    form = StateAdminForm
    list_display = [
        "created",
        "id",
        "last_updated",
        "name",
    ]
    readonly_fields = [
        "created",
        "id",
        "last_updated",
        "name",
    ]


class CityAdminForm(forms.ModelForm):

    class Meta:
        model = models.City
        fields = "__all__"


class CityAdmin(admin.ModelAdmin):
    form = CityAdminForm
    list_display = [
        "name",
        "id",
        "created",
        "last_updated",
    ]
    readonly_fields = [
        "name",
        "id",
        "created",
        "last_updated",
    ]


class LocalityAdminForm(forms.ModelForm):

    class Meta:
        model = models.Locality
        fields = "__all__"


class LocalityAdmin(admin.ModelAdmin):
    form = LocalityAdminForm
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


admin.site.register(models.Country, CountryAdmin)
admin.site.register(models.State, StateAdmin)
admin.site.register(models.City, CityAdmin)
admin.site.register(models.Locality, LocalityAdmin)
