from django.shortcuts import render
from . import models
from .models import Product

# Create your views here.
def index(request):
    products = models.Product.objects.all()
    for product in products:
        product.image = product.image.url[22:] # type: ignore
    context = {'product':True, 'products':products}
    return render(request, "product/index.html", context)

def search_results(request):
    if 'search' in request.GET:
        search_term = request.GET['search']
        object_list = Product.objects.filter(name__icontains=search_term)
    else:
        object_list = Product.objects.all()
    return render(request, 'product/search_results.html', {'object_list': object_list})
