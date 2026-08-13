from django.urls import path
from .views import IndexView, ContactoView, UserCreateView, ProductCreateView, InventarioView 

urlpatterns = [
    path("", IndexView.as_view(), name = "home"),
    path("contacto/", ContactoView.as_view(), name = "contacto"),
    path("usuarios/", UserCreateView.as_view(), name = "usuarios"),
    path("productos/", ProductCreateView.as_view(), name = "productos"),
    path("inventario/", InventarioView.as_view(), name = "inventario")
]