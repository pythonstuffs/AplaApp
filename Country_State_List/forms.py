from django import forms
from . import models


class CountryForm(forms.ModelForm):
    class Meta:
        model = models.Country
        fields = "__all__"


class StateForm(forms.ModelForm):
    country =forms.ModelChoiceField(queryset=models.Country.objects.all())
    class Meta:
        model = models.State
        fields = "__all__"


class CityForm(forms.ModelForm):
    class Meta:
        model = models.City
        fields = "__all__"


class LocalityForm(forms.ModelForm):
    class Meta:
        model = models.Locality
        fields = "__all__"
