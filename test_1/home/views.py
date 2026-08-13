from operator import index 
from django.views.generic import  CreateView, ListView

from django.urls import reverse_lazy
from django.views import View
from django.shortcuts import render
from users.models import User, Product 
from .forms import UserForm, ProductForm

class IndexView(View):
    def get(self, request):
        return render(request, "home/index.html")
    
class ContactoView(View):
    def get(self, request):
        return render(request, "home/contacto.html")

class UserCreateView(CreateView):
    model = User 
    form_class = UserForm 
    template_name = "home/usuarios.html"
    success_url = reverse_lazy("usuarios")

class ProductCreateView(CreateView):
    model = Product 
    form_class = ProductForm 
    template_name = "home/productos.html"
    success_url = reverse_lazy("productos")

class InventarioView(ListView):
    model = Product 
    template_name = "home/inventario.html"
    context_object_name = "Inventario"

