from django.contrib import admin
from .models import libro, autor, categoria
# Register your models here.

admin.site.register(libro)
admin.site.register(autor)
admin.site.register(categoria)
