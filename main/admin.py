from django.contrib import admin
from .models import libro, autor, categoria,navbar
# Register your models here.
class AutorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'nacionalidad')

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre',)

class LibroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'categoria', 'fecha_publicacion')
    list_filter = ('autor', 'categoria')
    search_fields = ('titulo', 'autor__nombre', 'categoria__nombre')

admin.site.register(navbar)
admin.site.register(libro)
admin.site.register(autor)
admin.site.register(categoria)
