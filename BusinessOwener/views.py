from django.views import generic
from django.urls import reverse_lazy
from . import models
from . import forms


class BusinessTypeListView(generic.ListView):
    model = models.BusinessType
    form_class = forms.BusinessTypeForm


class BusinessTypeCreateView(generic.CreateView):
    model = models.BusinessType
    form_class = forms.BusinessTypeForm


class BusinessTypeDetailView(generic.DetailView):
    model = models.BusinessType
    form_class = forms.BusinessTypeForm
    pk_url_kwarg = "id"


class BusinessTypeUpdateView(generic.UpdateView):
    model = models.BusinessType
    form_class = forms.BusinessTypeForm
    pk_url_kwarg = "id"


class BusinessTypeDeleteView(generic.DeleteView):
    model = models.BusinessType
    success_url = reverse_lazy("BusinessOwener_BusinessType_list")


class storeprofileListView(generic.ListView):
    model = models.storeprofile
    form_class = forms.storeprofileForm


class storeprofileCreateView(generic.CreateView):
    model = models.storeprofile
    form_class = forms.storeprofileForm


class storeprofileDetailView(generic.DetailView):
    model = models.storeprofile
    form_class = forms.storeprofileForm
    pk_url_kwarg = "BID"


class storeprofileUpdateView(generic.UpdateView):
    model = models.storeprofile
    form_class = forms.storeprofileForm
    pk_url_kwarg = "BID"


class storeprofileDeleteView(generic.DeleteView):
    model = models.storeprofile
    success_url = reverse_lazy("BusinessOwener_storeprofile_list")


class stroetimingListView(generic.ListView):
    model = models.stroetiming
    form_class = forms.stroetimingForm


class stroetimingCreateView(generic.CreateView):
    model = models.stroetiming
    form_class = forms.stroetimingForm


class stroetimingDetailView(generic.DetailView):
    model = models.stroetiming
    form_class = forms.stroetimingForm


class stroetimingUpdateView(generic.UpdateView):
    model = models.stroetiming
    form_class = forms.stroetimingForm
    pk_url_kwarg = "pk"


class stroetimingDeleteView(generic.DeleteView):
    model = models.stroetiming
    success_url = reverse_lazy("BusinessOwener_stroetiming_list")
