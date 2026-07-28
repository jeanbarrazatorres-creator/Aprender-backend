from operator import index

from django.views import View
from django.shortcuts import render

class IndexView(View):
    def get(self, request):
        return render(request, "home/index.html")
    
class ContactoView(View):
    def get(self, request):
        return render(request, "home/contacto.html")

    