from django.db import models

# Create your models here.
class Deporte(models.Model):
    nombre = models.CharField(max_length=50)
    categoría = models.CharField(max_length=50)

    class Meta:
        ordering = ['nombre']

    def __str__(self):
        return f"{self.nombre}"

class Deportista(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()
    edad = models.IntegerField(default=0)

    class Meta:
        ordering = ['apellido']
    def __str__(self):
        return f"{self.apellido}, {self.nombre}"
    
class Entrenador(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()
    fechaAlta = models.DateField()

    class Meta:
        verbose_name = "Entrenador"
        verbose_name_plural = "Entrenadores"
        ordering = ['apellido']
    
    def __str__(self):
        return f"{self.apellido}, {self.nombre}"
        
class Club(models.Model):
    nombre = models.CharField(max_length=50)
    domicilio = models.CharField(max_length=50)
    
    class Meta:
        verbose_name = "Club"
        verbose_name_plural = "Clubes"
        ordering = ['nombre']
    
    def __str__(self):
        return f"{self.nombre}"