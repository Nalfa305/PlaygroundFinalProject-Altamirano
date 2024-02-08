from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from .forms import *
from django.contrib.auth.views import LoginView

def index(request):
    contexto = {"index":True}
    return render(request, "core/index.html",contexto)

def about(request : HttpRequest) -> HttpResponse:
    context = {"about":True}
    return render(request, "core/about.html",context) 

class CustomLoginView(LoginView):
    authentication_form = CustomAuthenticationForm
    template_name = "core/login.html"


def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "core/index.html")
    else:
        form = CustomUserCreationForm()
    return render(request, "core/register.html", {"form": form})