from django.contrib import admin
from django import forms

from . import models


class Product_CategoryAdminForm(forms.ModelForm):

    class Meta:
        model = models.Product_Category
        fields = "__all__"


class Product_CategoryAdmin(admin.ModelAdmin):
    form = Product_CategoryAdminForm
    list_display = [
        "last_updated",
        "name",
        "id",
        "created",
        "is_active",
    ]
    readonly_fields = [
        "last_updated",
        "name",
        "id",
        "created",
        "is_active",
    ]


class Product_SubCategoryAdminForm(forms.ModelForm):

    class Meta:
        model = models.Product_SubCategory
        fields = "__all__"


class Product_SubCategoryAdmin(admin.ModelAdmin):
    form = Product_SubCategoryAdminForm
    list_display = [
        "is_active",
        "Product_Category",
        "last_updated",
        "created",
        "id",
        "name",
    ]
    readonly_fields = [
        "is_active",
        "Product_Category",
        "last_updated",
        "created",
        "id",
        "name",
    ]


class ProductAdminForm(forms.ModelForm):

    class Meta:
        model = models.Product
        fields = "__all__"


class ProductAdmin(admin.ModelAdmin):
    form = ProductAdminForm
    list_display = [
        "PName",
        "PSellingPrice",
        "PAvailiblity",
        "PID",
        "PDelivery",
        "PSubCategory",
        "PActualPrice",
        "PCategory",
        "last_updated",
        "PUnit",
        "BID",
        "created",
        "PMargin",
        "PImage",
    ]
    readonly_fields = [
        "PName",
        "PSellingPrice",
        "PAvailiblity",
        "PID",
        "PDelivery",
        "PSubCategory",
        "PActualPrice",
        "PCategory",
        "last_updated",
        "PUnit",
        "BID",
        "created",
        "PMargin",
        "PImage",
    ]


admin.site.register(models.Product_Category, Product_CategoryAdmin)
admin.site.register(models.Product_SubCategory, Product_SubCategoryAdmin)
admin.site.register(models.Product, ProductAdmin)
