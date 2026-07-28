from django.urls import path
from .views import IndexView, ContactoView

urlpatterns = [
    path("", IndexView.as_view(), name = "home"),
    path("contacto/", ContactoView.as_view(), name = "contacto"),
]