from django.shortcuts import render

# Create your views here.

def index(request):
    titulo = "Home"
    # navbars = Navbar.objects.all()
    # context = {'navbar': navbars, 'Titulo': titulo}
    context = {'Titulo': titulo}
    return render(request, 'index.html', context)

def libros(request):
    titulo = "Libros"
    # navbars = Navbar.objects.all()
    # context = {'navbar': navbars, 'Titulo': titulo}
    context = {'Titulo': titulo}
    return render(request, 'libros.html', context)

def autores(request):
    titulo = "Autores"
    # navbars = Navbar.objects.all()
    # context = {'navbar': navbars, 'Titulo': titulo}
    context = {'Titulo': titulo}
    return render(request, 'autores.html', context)

def categorias(request):
    titulo = "Categorias"
    # navbars = Navbar.objects.all()
    # context = {'navbar': navbars, 'Titulo': titulo}
    context = {'Titulo': titulo}
    return render(request, 'categorias.html', context)