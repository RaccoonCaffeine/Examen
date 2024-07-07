from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views as main

urlpatterns = [
    path('', main.index, name='index'),
    path('libros/', main.libros, name='libros'),
    path('autores/', main.autores, name='autores'),
    path('categorias/', main.categorias, name='categorias'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)