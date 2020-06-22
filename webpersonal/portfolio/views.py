from django.shortcuts import render
from .models import Project

# Create your views here.
def portfolio(request):
    projects = Project.objects.all() #gx:objects se crea en tiempo de ejecución #all devuelve todos los objetos que son Project
    return render(request, 'portfolio/portfolio.html', {'projects':projects})