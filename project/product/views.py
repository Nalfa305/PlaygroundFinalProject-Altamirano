from django.shortcuts import render

# Create your views here.
def index(request):
    context = {'product':True}
    return render(request, "product/index.html", context)