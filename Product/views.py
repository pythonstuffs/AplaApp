from django.views import generic
from django.urls import reverse_lazy
from . import models
from . import forms


class Product_CategoryListView(generic.ListView):
    model = models.Product_Category
    form_class = forms.Product_CategoryForm


class Product_CategoryCreateView(generic.CreateView):
    model = models.Product_Category
    form_class = forms.Product_CategoryForm


class Product_CategoryDetailView(generic.DetailView):
    model = models.Product_Category
    form_class = forms.Product_CategoryForm
    pk_url_kwarg = "id"


class Product_CategoryUpdateView(generic.UpdateView):
    model = models.Product_Category
    form_class = forms.Product_CategoryForm
    pk_url_kwarg = "id"


class Product_CategoryDeleteView(generic.DeleteView):
    model = models.Product_Category
    success_url = reverse_lazy("Product_Product_Category_list")


class Product_SubCategoryListView(generic.ListView):
    model = models.Product_SubCategory
    form_class = forms.Product_SubCategoryForm


class Product_SubCategoryCreateView(generic.CreateView):
    model = models.Product_SubCategory
    form_class = forms.Product_SubCategoryForm


class Product_SubCategoryDetailView(generic.DetailView):
    model = models.Product_SubCategory
    form_class = forms.Product_SubCategoryForm
    pk_url_kwarg = "id"


class Product_SubCategoryUpdateView(generic.UpdateView):
    model = models.Product_SubCategory
    form_class = forms.Product_SubCategoryForm
    pk_url_kwarg = "id"


class Product_SubCategoryDeleteView(generic.DeleteView):
    model = models.Product_SubCategory
    success_url = reverse_lazy("Product_Product_SubCategory_list")


class ProductListView(generic.ListView):
    model = models.Product
    form_class = forms.ProductForm


class ProductCreateView(generic.CreateView):
    model = models.Product
    form_class = forms.ProductForm


class ProductDetailView(generic.DetailView):
    model = models.Product
    form_class = forms.ProductForm
    pk_url_kwarg = "PID"


class ProductUpdateView(generic.UpdateView):
    model = models.Product
    form_class = forms.ProductForm
    pk_url_kwarg = "PID"


class ProductDeleteView(generic.DeleteView):
    model = models.Product
    success_url = reverse_lazy("Product_Product_list")
