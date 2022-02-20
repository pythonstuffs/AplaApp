from django.urls import path, include
from rest_framework import routers

from . import api
from . import views


router = routers.DefaultRouter()
router.register("BusinessType", api.BusinessTypeViewSet)
router.register("storeprofile", api.storeprofileViewSet)
router.register("stroetiming", api.stroetimingViewSet)

urlpatterns = (
    path("api/v1/", include(router.urls)),
    path("BusinessOwener/BusinessType/", views.BusinessTypeListView.as_view(), name="BusinessOwener_BusinessType_list"),
    path("BusinessOwener/BusinessType/create/", views.BusinessTypeCreateView.as_view(), name="BusinessOwener_BusinessType_create"),
    path("BusinessOwener/BusinessType/detail/<int:id>/", views.BusinessTypeDetailView.as_view(), name="BusinessOwener_BusinessType_detail"),
    path("BusinessOwener/BusinessType/update/<int:id>/", views.BusinessTypeUpdateView.as_view(), name="BusinessOwener_BusinessType_update"),
    path("BusinessOwener/BusinessType/delete/<int:id>/", views.BusinessTypeDeleteView.as_view(), name="BusinessOwener_BusinessType_delete"),
    path("BusinessOwener/storeprofile/", views.storeprofileListView.as_view(), name="BusinessOwener_storeprofile_list"),
    path("BusinessOwener/storeprofile/create/", views.storeprofileCreateView.as_view(), name="BusinessOwener_storeprofile_create"),
    path("BusinessOwener/storeprofile/detail/<int:BID>/", views.storeprofileDetailView.as_view(), name="BusinessOwener_storeprofile_detail"),
    path("BusinessOwener/storeprofile/update/<int:BID>/", views.storeprofileUpdateView.as_view(), name="BusinessOwener_storeprofile_update"),
    path("BusinessOwener/storeprofile/delete/<int:BID>/", views.storeprofileDeleteView.as_view(), name="BusinessOwener_storeprofile_delete"),
    path("BusinessOwener/stroetiming/", views.stroetimingListView.as_view(), name="BusinessOwener_stroetiming_list"),
    path("BusinessOwener/stroetiming/create/", views.stroetimingCreateView.as_view(), name="BusinessOwener_stroetiming_create"),
    path("BusinessOwener/stroetiming/detail/<int:pk>/", views.stroetimingDetailView.as_view(), name="BusinessOwener_stroetiming_detail"),
    path("BusinessOwener/stroetiming/update/<int:pk>/", views.stroetimingUpdateView.as_view(), name="BusinessOwener_stroetiming_update"),
    path("BusinessOwener/stroetiming/delete/<int:pk>/", views.stroetimingDeleteView.as_view(), name="BusinessOwener_stroetiming_delete"),
)
