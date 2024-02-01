from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

def index(request):
    contexto = {"index":True}
    return render(request, "core/index.html",contexto)

def about(request : HttpRequest) -> HttpResponse:
    context = {"about":True}
    return render(request, "core/about.html",context) 