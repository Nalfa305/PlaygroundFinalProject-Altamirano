from django.shortcuts import render
from django.urls import reverse_lazy
from . import models
from .form import *
from .models import ProductCategory, ProductSubCategory, Product
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)
# Create your views here.
def index(request):
    products = Product.objects.all()
    for product in products:
        product.image = product.image.url[22:] # type: ignore
    context = {'product':True, 'products':products}
    return render(request, "product/index.html", context)

def search_results(request):
    if 'search' in request.GET:
        search_term = request.GET['search']
        object_list = Product.objects.filter(name__icontains=search_term)
        for product in object_list:
            product.image = product.image.url[22:] # type: ignore
    else:
        object_list = []
    return render(request, 'product/search_results.html', {'object_list': object_list})



class ProductCategoryList(ListView):
    model = ProductCategory
    # context_object_name = "object_list"
    # template_name = "producto/productocategoria_list.html"

    def get_queryset(self):
        if self.request.GET.get("Ask"):
            Ask = self.request.GET.get("Ask")
            object_list = ProductCategory.objects.filter(nombre__icontains= Ask)
        else:
            object_list = ProductCategory.objects.all()
        return object_list
    
class ProductSubCategoryList(ListView):
    model = ProductSubCategory
    # context_object_name = "object_list"
    # template_name = "producto/productocategoria_list.html"

    def get_queryset(self):
        if self.request.GET.get("Ask"):
            Ask = self.request.GET.get("Ask")
            object_list = ProductSubCategory.objects.filter(nombre__icontains= Ask)
        else:
            object_list = ProductSubCategory.objects.all()
        return object_list
    
class ProductCategoryCreate(CreateView):
    model = ProductCategory
    form_class = ProductCategoryForm
    success_url = reverse_lazy("product:productcategory_list")

class ProductSubCategoryCreate(CreateView):
    model = ProductSubCategory
    form_class = ProductSubCategoryForm
    success_url = reverse_lazy("product:productsubcategory_list")

class ProductCategoryDetail(DetailView):
    model = ProductCategory

class ProductSubCategoryDetail(DetailView):
    model = ProductSubCategory

class ProductCategoryUpdate(UpdateView):
    model = ProductCategory
    form_class = ProductCategoryForm
    success_url = reverse_lazy("product:productcategory_list")

class ProductSubCategoryUpdate(UpdateView):
    model = ProductSubCategory
    form_class = ProductSubCategoryForm
    success_url = reverse_lazy("product:productsubcategory_list")

class ProductCategoryDelete(DeleteView):
    model = ProductCategory
    success_url = reverse_lazy("product:productcategory_list")

class ProductSubCategoryDelete(DeleteView):
    model = ProductSubCategory
    success_url = reverse_lazy("product:productsubcategory_list")



