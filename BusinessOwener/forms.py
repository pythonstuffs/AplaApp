from django import forms
from . import models


class BusinessTypeForm(forms.ModelForm):
    class Meta:
        model = models.BusinessType
        fields = [
            "name",
        ]


class storeprofileForm(forms.ModelForm):
    class Meta:
        model = models.storeprofile
        fields = "__all__"


class stroetimingForm(forms.ModelForm):
    class Meta:
        model = models.stroetiming
        fields = [
            "Time",
        ]
