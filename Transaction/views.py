from django.views import generic
from django.urls import reverse_lazy
from . import models
from . import forms


class PaymentStatusListView(generic.ListView):
    model = models.PaymentStatus
    form_class = forms.PaymentStatusForm


class PaymentStatusCreateView(generic.CreateView):
    model = models.PaymentStatus
    form_class = forms.PaymentStatusForm


class PaymentStatusDetailView(generic.DetailView):
    model = models.PaymentStatus
    form_class = forms.PaymentStatusForm
    pk_url_kwarg = "id"


class PaymentStatusUpdateView(generic.UpdateView):
    model = models.PaymentStatus
    form_class = forms.PaymentStatusForm
    pk_url_kwarg = "id"


class PaymentStatusDeleteView(generic.DeleteView):
    model = models.PaymentStatus
    success_url = reverse_lazy("Transaction_PaymentStatus_list")


class InvoiceListView(generic.ListView):
    model = models.Invoice
    form_class = forms.InvoiceForm


class InvoiceCreateView(generic.CreateView):
    model = models.Invoice
    form_class = forms.InvoiceForm


class InvoiceDetailView(generic.DetailView):
    model = models.Invoice
    form_class = forms.InvoiceForm
    pk_url_kwarg = "TID"


class InvoiceUpdateView(generic.UpdateView):
    model = models.Invoice
    form_class = forms.InvoiceForm
    pk_url_kwarg = "TID"


class InvoiceDeleteView(generic.DeleteView):
    model = models.Invoice
    success_url = reverse_lazy("Transaction_Invoice_list")


class TransactionModeListView(generic.ListView):
    model = models.TransactionMode
    form_class = forms.TransactionModeForm


class TransactionModeCreateView(generic.CreateView):
    model = models.TransactionMode
    form_class = forms.TransactionModeForm


class TransactionModeDetailView(generic.DetailView):
    model = models.TransactionMode
    form_class = forms.TransactionModeForm
    pk_url_kwarg = "id"


class TransactionModeUpdateView(generic.UpdateView):
    model = models.TransactionMode
    form_class = forms.TransactionModeForm
    pk_url_kwarg = "id"


class TransactionModeDeleteView(generic.DeleteView):
    model = models.TransactionMode
    success_url = reverse_lazy("Transaction_TransactionMode_list")


class TransactionStatusListView(generic.ListView):
    model = models.TransactionStatus
    form_class = forms.TransactionStatusForm


class TransactionStatusCreateView(generic.CreateView):
    model = models.TransactionStatus
    form_class = forms.TransactionStatusForm


class TransactionStatusDetailView(generic.DetailView):
    model = models.TransactionStatus
    form_class = forms.TransactionStatusForm
    pk_url_kwarg = "id"


class TransactionStatusUpdateView(generic.UpdateView):
    model = models.TransactionStatus
    form_class = forms.TransactionStatusForm
    pk_url_kwarg = "id"


class TransactionStatusDeleteView(generic.DeleteView):
    model = models.TransactionStatus
    success_url = reverse_lazy("Transaction_TransactionStatus_list")


class OrderListView(generic.ListView):
    model = models.Order
    form_class = forms.OrderForm


class OrderCreateView(generic.CreateView):
    model = models.Order
    form_class = forms.OrderForm


class OrderDetailView(generic.DetailView):
    model = models.Order
    form_class = forms.OrderForm
    pk_url_kwarg = "OID"


class OrderUpdateView(generic.UpdateView):
    model = models.Order
    form_class = forms.OrderForm
    pk_url_kwarg = "OID"


class OrderDeleteView(generic.DeleteView):
    model = models.Order
    success_url = reverse_lazy("Transaction_Order_list")
