from django.shortcuts import render
from .models import navbar, libro, autor, categoria
# Create your views here.

def index(request):
    titulo = "Bookers"
    navbars = navbar.objects.all()
    context = {'navbar': navbars, 'Titulo': titulo}
    return render(request, 'index.html', context)

def libros(request):
    titulo = "Libros"
    navbars = navbar.objects.all()
    libros = libro.objects.all()
    context = {'navbar': navbars, 'Titulo': titulo, 'libros': libros}
    return render(request, 'libros.html', context)

def autores(request):
    titulo = "Autores"
    navbars = navbar.objects.all()
    autores = autor.objects.all()
    context = {'navbar': navbars, 'Titulo': titulo, 'autores': autores}
    return render(request, 'autores.html', context)

def categorias(request):
    titulo = "Categorias"
    navbars = navbar.objects.all()
    categorias = categoria.objects.all()
    context = {'navbar': navbars, 'Titulo': titulo, 'categorias': categorias}
    return render(request, 'categorias.html', context)