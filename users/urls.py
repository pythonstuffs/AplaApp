from django.urls import path, include
from rest_framework import routers

from . import api
from . import views


router = routers.DefaultRouter()
router.register("profile", api.profileViewSet)

urlpatterns = (
    path("api/v1/", include(router.urls)),
    path("users/profile/", views.profileListView.as_view(), name="users_profile_list"),
    path("users/profile/create/", views.profileCreateView.as_view(), name="users_profile_create"),
    path("users/profile/detail/<slug:slug>/", views.profileDetailView.as_view(), name="users_profile_detail"),
    path("users/profile/update/<slug:slug>/", views.profileUpdateView.as_view(), name="users_profile_update"),
    path("users/profile/delete/<slug:slug>/", views.profileDeleteView.as_view(), name="users_profile_delete"),
)
