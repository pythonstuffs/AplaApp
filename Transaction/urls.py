from django.urls import path, include
from rest_framework import routers

from . import api
from . import views


router = routers.DefaultRouter()
router.register("PaymentStatus", api.PaymentStatusViewSet)
router.register("Invoice", api.InvoiceViewSet)
router.register("TransactionMode", api.TransactionModeViewSet)
router.register("TransactionStatus", api.TransactionStatusViewSet)
router.register("Order", api.OrderViewSet)

urlpatterns = (
    path("api/v1/", include(router.urls)),
    path("Transaction/PaymentStatus/", views.PaymentStatusListView.as_view(), name="Transaction_PaymentStatus_list"),
    path("Transaction/PaymentStatus/create/", views.PaymentStatusCreateView.as_view(), name="Transaction_PaymentStatus_create"),
    path("Transaction/PaymentStatus/detail/<int:id>/", views.PaymentStatusDetailView.as_view(), name="Transaction_PaymentStatus_detail"),
    path("Transaction/PaymentStatus/update/<int:id>/", views.PaymentStatusUpdateView.as_view(), name="Transaction_PaymentStatus_update"),
    path("Transaction/PaymentStatus/delete/<int:id>/", views.PaymentStatusDeleteView.as_view(), name="Transaction_PaymentStatus_delete"),
    path("Transaction/Invoice/", views.InvoiceListView.as_view(), name="Transaction_Invoice_list"),
    path("Transaction/Invoice/create/", views.InvoiceCreateView.as_view(), name="Transaction_Invoice_create"),
    path("Transaction/Invoice/detail/<int:TID>/", views.InvoiceDetailView.as_view(), name="Transaction_Invoice_detail"),
    path("Transaction/Invoice/update/<int:TID>/", views.InvoiceUpdateView.as_view(), name="Transaction_Invoice_update"),
    path("Transaction/Invoice/delete/<int:TID>/", views.InvoiceDeleteView.as_view(), name="Transaction_Invoice_delete"),
    path("Transaction/TransactionMode/", views.TransactionModeListView.as_view(), name="Transaction_TransactionMode_list"),
    path("Transaction/TransactionMode/create/", views.TransactionModeCreateView.as_view(), name="Transaction_TransactionMode_create"),
    path("Transaction/TransactionMode/detail/<int:id>/", views.TransactionModeDetailView.as_view(), name="Transaction_TransactionMode_detail"),
    path("Transaction/TransactionMode/update/<int:id>/", views.TransactionModeUpdateView.as_view(), name="Transaction_TransactionMode_update"),
    path("Transaction/TransactionMode/delete/<int:id>/", views.TransactionModeDeleteView.as_view(), name="Transaction_TransactionMode_delete"),
    path("Transaction/TransactionStatus/", views.TransactionStatusListView.as_view(), name="Transaction_TransactionStatus_list"),
    path("Transaction/TransactionStatus/create/", views.TransactionStatusCreateView.as_view(), name="Transaction_TransactionStatus_create"),
    path("Transaction/TransactionStatus/detail/<int:id>/", views.TransactionStatusDetailView.as_view(), name="Transaction_TransactionStatus_detail"),
    path("Transaction/TransactionStatus/update/<int:id>/", views.TransactionStatusUpdateView.as_view(), name="Transaction_TransactionStatus_update"),
    path("Transaction/TransactionStatus/delete/<int:id>/", views.TransactionStatusDeleteView.as_view(), name="Transaction_TransactionStatus_delete"),
    path("Transaction/Order/", views.OrderListView.as_view(), name="Transaction_Order_list"),
    path("Transaction/Order/create/", views.OrderCreateView.as_view(), name="Transaction_Order_create"),
    path("Transaction/Order/detail/<int:OID>/", views.OrderDetailView.as_view(), name="Transaction_Order_detail"),
    path("Transaction/Order/update/<int:OID>/", views.OrderUpdateView.as_view(), name="Transaction_Order_update"),
    path("Transaction/Order/delete/<int:OID>/", views.OrderDeleteView.as_view(), name="Transaction_Order_delete"),
)
