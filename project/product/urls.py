from django.urls import path

from . import views
from .views import search_results

app_name = "product"

urlpatterns = [
    path("", views.index, name="index"),
    path('search_results', search_results, name='search_results'),
    path("productcategory/list/", views.ProductCategoryList.as_view(), name="productcategory_list"),
    path("productcategory/create/", views.ProductCategoryCreate.as_view(), name="productcategory_create"),
    path("productcategory/detail/<int:pk>", views.ProductCategoryDetail.as_view(), name="productcategory_detail"),
    path("productcategory/update/<int:pk>", views.ProductCategoryUpdate.as_view(), name="productcategory_update"),
    path("productcategory/delete/<int:pk>", views.ProductCategoryDelete.as_view(), name="productcategory_delete"),
    path("productsubcategory/list/", views.ProductSubCategoryList.as_view(), name="productsubcategory_list"),
    path("productsubcategory/create/", views.ProductSubCategoryCreate.as_view(), name="productsubcategory_create"),
    path("productsubcategory/detail/<int:pk>", views.ProductSubCategoryDetail.as_view(), name="productsubcategory_detail"),
    path("productsubcategory/update/<int:pk>", views.ProductSubCategoryUpdate.as_view(), name="productsubcategory_update"),
    path("productsubcategory/delete/<int:pk>", views.ProductSubCategoryDelete.as_view(), name="productsubcategory_delete"),
]