from django.shortcuts import render, redirect
from django.urls import reverse
from django.db.models import Q
from .models import navbar, libro, autor, categoria
import time

def index(request):
    random_items = list(libro.objects.order_by('?')[:3])
    query = request.GET.get('buscar')
    if query:
        return redirect(reverse('resultados') + f'?buscar={query}')
    else:
        buscar = libro.objects.all()
        template = 'index.html'
        titulo = "Bookers"
        navbars = navbar.objects.all()
        context = {'navbar': navbars, 'Titulo': titulo, 'libros_random': random_items}
        return render(request, template, context)
    
def random(request):
    random_items = list(libro.objects.order_by('?')[:3])
    context = {'libros_random': random_items}
    return render(request, 'random.html', context)
    
def resultados(request):
    query = request.GET.get('buscar')
    if query:
        buscar = libro.objects.filter(
            Q(titulo__icontains=query) |
            Q(autor__nombre__icontains=query) |
            Q(categoria__nombre__icontains=query)
        ).distinct()
        titulo = f"Resultados de la búsqueda: {query}"
    else:
        buscar = list(libro.objects.order_by('?')[:6])
        titulo = "Todos los libros" 
    time.sleep(2)
    navbars = navbar.objects.all()
    return render(request, 'resultado.html', {'buscar': buscar, 'Titulo': titulo, 'navbar': navbars})
    

def libros(request):
    query = request.GET.get('buscar-libro')
    if query:
        buscar_libro = libro.objects.filter(
            Q(titulo__icontains=query) |
            Q(autor__nombre__icontains=query) |
            Q(categoria__nombre__icontains=query)
        ).distinct()
    else:
        buscar_libro = libro.objects.all()
    titulo = "Libros"
    navbars = navbar.objects.all()
    categorias = categoria.objects.all()
    context = {'navbar': navbars, 'Titulo': titulo, 'libro': buscar_libro, 'categorias': categorias}
    return render(request, 'libros.html', context)

def autores(request):
    query = request.GET.get('buscar-autor')
    if query:
        buscar_autor = autor.objects.filter(
            Q(nombre__icontains=query)
        ).distinct()
    else:
        buscar_autor = autor.objects.all()
    titulo = "Autores"
    navbars = navbar.objects.all()
    context = {'navbar': navbars, 'Titulo': titulo, 'autores': buscar_autor}
    return render(request, 'autores.html', context)

def categorias(request):
    query = request.GET.get('buscar-categoria')
    if query:
        buscar_categoria = categoria.objects.filter(
            Q(nombre__icontains=query)
        ).distinct()
    else:
        buscar_categoria = categoria.objects.all()
    titulo = "Categorías"
    navbars = navbar.objects.all()
    context = {'navbar': navbars, 'Titulo': titulo, 'categorias': buscar_categoria}
    return render(request, 'categorias.html', context)
