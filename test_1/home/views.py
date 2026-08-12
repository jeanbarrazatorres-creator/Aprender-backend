from operator import index 
from django.views.generic import  CreateView
from django.urls import reverse_lazy
from django.views import View
from django.shortcuts import render
from users.models import User 
from .forms import UserForm 

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
    success_url = reverse_lazy("home:index")
