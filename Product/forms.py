from django import forms
from . import models


class Product_CategoryForm(forms.ModelForm):
    class Meta:
        model = models.Product_Category
        fields = [
            "name",
            "is_active",
        ]


class Product_SubCategoryForm(forms.ModelForm):
    class Meta:
        model = models.Product_SubCategory
        fields = [
            "is_active",
            "Product_Category",
            "name",
        ]


class ProductForm(forms.ModelForm):
    class Meta:
        model = models.Product
        fields = [
            "BID",
            "PName",
            "PSellingPrice",
            "PAvailiblity",
            "PDelivery",
            "PSubCategory",
            "PActualPrice",
            "PCategory",
            "PUnit",
            "PMargin",
            "PImage",
        ]
