from django.contrib import admin
from django import forms

from . import models


class profileAdminForm(forms.ModelForm):

    class Meta:
        model = models.profile
        fields = "__all__"


class profileAdmin(admin.ModelAdmin):
    form = profileAdminForm
    list_display = [
        "id",
        "username",
        "MobileNumber",
        "birthday",
        "profileimage",
        "last_updated",
    ]
    readonly_fields = [
        "slug",
        "created",
        "MobileNumber",
        "birthday",
        "profileimage",
        "last_updated",
    ]


admin.site.register(models.profile, profileAdmin)
