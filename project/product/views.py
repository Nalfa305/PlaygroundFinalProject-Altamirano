from django.shortcuts import render
from . import models

# Create your views here.
def index(request):
    products = models.Product.objects.all()
    for product in products:
        product.image = product.image.url[22:] # type: ignore
    context = {'product':True, 'products':products}
    return render(request, "product/index.html", context)

