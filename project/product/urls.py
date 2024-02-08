from django.urls import path

from . import views
from .views import search_results

app_name = "product"

urlpatterns = [
    path("", views.index, name="index"),
    path('search_results', search_results, name='search_results'),
]