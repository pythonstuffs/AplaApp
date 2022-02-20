from django.urls import path, include
from rest_framework import routers

from . import api
from . import views


router = routers.DefaultRouter()
router.register("Product_Category", api.Product_CategoryViewSet)
router.register("Product_SubCategory", api.Product_SubCategoryViewSet)
router.register("Product", api.ProductViewSet)

urlpatterns = (
    path("api/v1/", include(router.urls)),
    path("Product/Product_Category/", views.Product_CategoryListView.as_view(), name="Product_Product_Category_list"),
    path("Product/Product_Category/create/", views.Product_CategoryCreateView.as_view(), name="Product_Product_Category_create"),
    path("Product/Product_Category/detail/<int:id>/", views.Product_CategoryDetailView.as_view(), name="Product_Product_Category_detail"),
    path("Product/Product_Category/update/<int:id>/", views.Product_CategoryUpdateView.as_view(), name="Product_Product_Category_update"),
    path("Product/Product_Category/delete/<int:id>/", views.Product_CategoryDeleteView.as_view(), name="Product_Product_Category_delete"),
    path("Product/Product_SubCategory/", views.Product_SubCategoryListView.as_view(), name="Product_Product_SubCategory_list"),
    path("Product/Product_SubCategory/create/", views.Product_SubCategoryCreateView.as_view(), name="Product_Product_SubCategory_create"),
    path("Product/Product_SubCategory/detail/<int:id>/", views.Product_SubCategoryDetailView.as_view(), name="Product_Product_SubCategory_detail"),
    path("Product/Product_SubCategory/update/<int:id>/", views.Product_SubCategoryUpdateView.as_view(), name="Product_Product_SubCategory_update"),
    path("Product/Product_SubCategory/delete/<int:id>/", views.Product_SubCategoryDeleteView.as_view(), name="Product_Product_SubCategory_delete"),
    path("Product/Product/", views.ProductListView.as_view(), name="Product_Product_list"),
    path("Product/Product/create/", views.ProductCreateView.as_view(), name="Product_Product_create"),
    path("Product/Product/detail/<int:PID>/", views.ProductDetailView.as_view(), name="Product_Product_detail"),
    path("Product/Product/update/<int:PID>/", views.ProductUpdateView.as_view(), name="Product_Product_update"),
    path("Product/Product/delete/<int:PID>/", views.ProductDeleteView.as_view(), name="Product_Product_delete"),
)
