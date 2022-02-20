from django.urls import path, include
from rest_framework import routers

from . import api
from . import views


router = routers.DefaultRouter()
router.register("Country", api.CountryViewSet)
router.register("State", api.StateViewSet)
router.register("City", api.CityViewSet)
router.register("Locality", api.LocalityViewSet)

urlpatterns = (
    path("api/v1/", include(router.urls)),
    path("Country_State_List/Country/", views.CountryListView.as_view(), name="Country_State_List_Country_list"),
    path("Country_State_List/Country/create/", views.CountryCreateView.as_view(), name="Country_State_List_Country_create"),
    path("Country_State_List/Country/detail/<int:id>/", views.CountryDetailView.as_view(), name="Country_State_List_Country_detail"),
    path("Country_State_List/Country/update/<int:id>/", views.CountryUpdateView.as_view(), name="Country_State_List_Country_update"),
    path("Country_State_List/Country/delete/<int:id>/", views.CountryDeleteView.as_view(), name="Country_State_List_Country_delete"),
    path("Country_State_List/State/", views.StateListView.as_view(), name="Country_State_List_State_list"),
    path("Country_State_List/State/create/", views.StateCreateView.as_view(), name="Country_State_List_State_create"),
    path("Country_State_List/State/detail/<int:id>/", views.StateDetailView.as_view(), name="Country_State_List_State_detail"),
    path("Country_State_List/State/update/<int:id>/", views.StateUpdateView.as_view(), name="Country_State_List_State_update"),
    path("Country_State_List/State/delete/<int:id>/", views.StateDeleteView.as_view(), name="Country_State_List_State_delete"),
    path("Country_State_List/City/", views.CityListView.as_view(), name="Country_State_List_City_list"),
    path("Country_State_List/City/create/", views.CityCreateView.as_view(), name="Country_State_List_City_create"),
    path("Country_State_List/City/detail/<int:id>/", views.CityDetailView.as_view(), name="Country_State_List_City_detail"),
    path("Country_State_List/City/update/<int:id>/", views.CityUpdateView.as_view(), name="Country_State_List_City_update"),
    path("Country_State_List/City/delete/<int:id>/", views.CityDeleteView.as_view(), name="Country_State_List_City_delete"),
    path("Country_State_List/Locality/", views.LocalityListView.as_view(), name="Country_State_List_Locality_list"),
    path("Country_State_List/Locality/create/", views.LocalityCreateView.as_view(), name="Country_State_List_Locality_create"),
    path("Country_State_List/Locality/detail/<int:id>/", views.LocalityDetailView.as_view(), name="Country_State_List_Locality_detail"),
    path("Country_State_List/Locality/update/<int:id>/", views.LocalityUpdateView.as_view(), name="Country_State_List_Locality_update"),
    path("Country_State_List/Locality/delete/<int:id>/", views.LocalityDeleteView.as_view(), name="Country_State_List_Locality_delete"),
)
