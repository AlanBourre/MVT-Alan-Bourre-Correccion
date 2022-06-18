from django.shortcuts import render

from .models import Familiares

# Create your views here.

def index(request):
    familiares = Familiares.objects.all()
    contexto = {"familiares": familiares} 
    return render(request, "AppCoder/index.html", contexto)
