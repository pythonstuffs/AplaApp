from django.views import generic
from django.urls import reverse_lazy
from . import models
from . import forms


class profileListView(generic.ListView):
    model = models.profile
    form_class = forms.profileForm


class profileCreateView(generic.CreateView):
    model = models.profile
    form_class = forms.profileForm
    


class profileDetailView(generic.DetailView):
    model = models.profile
    form_class = forms.profileForm
    slug_url_kwarg = "slug"


class profileUpdateView(generic.UpdateView):
    model = models.profile
    form_class = forms.profileForm
    slug_url_kwarg = "slug"


class profileDeleteView(generic.DeleteView):
    model = models.profile
    success_url = reverse_lazy("users_profile_list")
