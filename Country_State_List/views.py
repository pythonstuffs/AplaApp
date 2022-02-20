from django.views import generic
from django.urls import reverse_lazy
from . import models
from . import forms
from django.shortcuts import render,redirect

class CountryListView(generic.ListView):
    model = models.Country
    form_class = forms.CountryForm


class CountryCreateView(generic.CreateView):
    model = models.Country
    form_class = forms.CountryForm


class CountryDetailView(generic.DetailView):
    model = models.Country
    form_class = forms.CountryForm
    pk_url_kwarg = "id"


class CountryUpdateView(generic.UpdateView):
    model = models.Country
    form_class = forms.CountryForm
    pk_url_kwarg = "id"


class CountryDeleteView(generic.DeleteView):
    model = models.Country
    success_url = reverse_lazy("Country_State_List_Country_list")


class StateListView(generic.ListView):
    model = models.State
    form_class = forms.StateForm


class StateCreateView(generic.CreateView):
    model = models.State
    #form_class = forms.StateForm
    fields="__all__"
    template_name="Country_State_List/state_form.html"
    

class StateDetailView(generic.DetailView):
    model = models.State
    form_class = forms.StateForm
    pk_url_kwarg = "id"


class StateUpdateView(generic.UpdateView):
    model = models.State
    form_class = forms.StateForm
    pk_url_kwarg = "id"


class StateDeleteView(generic.DeleteView):
    model = models.State
    success_url = reverse_lazy("Country_State_List_State_list")


class CityListView(generic.ListView):
    model = models.City
    form_class = forms.CityForm


class CityCreateView(generic.CreateView):
    model = models.City
    form_class = forms.CityForm


class CityDetailView(generic.DetailView):
    model = models.City
    form_class = forms.CityForm
    pk_url_kwarg = "id"


class CityUpdateView(generic.UpdateView):
    model = models.City
    form_class = forms.CityForm
    pk_url_kwarg = "id"


class CityDeleteView(generic.DeleteView):
    model = models.City
    success_url = reverse_lazy("Country_State_List_City_list")


class LocalityListView(generic.ListView):
    model = models.Locality
    form_class = forms.LocalityForm


class LocalityCreateView(generic.CreateView):
    model = models.Locality
    form_class = forms.LocalityForm


class LocalityDetailView(generic.DetailView):
    model = models.Locality
    form_class = forms.LocalityForm
    pk_url_kwarg = "id"


class LocalityUpdateView(generic.UpdateView):
    model = models.Locality
    form_class = forms.LocalityForm
    pk_url_kwarg = "id"


class LocalityDeleteView(generic.DeleteView):
    model = models.Locality
    success_url = reverse_lazy("Country_State_List_Locality_list")
