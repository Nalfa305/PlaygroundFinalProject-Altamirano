from django.shortcuts import render

# Create your views here.

def index(request):
    clientes = Cliente.object.all()
    return render(request, "Clients/index.html", {"Clientes": clientes})