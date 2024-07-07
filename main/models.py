from django.db import models

# Create your models here.

class navbar(models.Model):
    nombre = models.CharField(max_length=50)
    url = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre
    
class autor(models.Model):
    id = models.AutoField(primary_key=True)
    nacionalidad = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre
    
class categoria(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class libro(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=50)
    autor = models.ForeignKey(autor, on_delete=models.CASCADE)
    categoria = models.ForeignKey(categoria, on_delete=models.CASCADE)
    fecha_publicacion = models.DateField()
    descripcion = models.TextField()
    img = models.ImageField(upload_to='libros', null=False, blank=False)
    link = models.URLField()

    def __str__(self):
        return self.titulo