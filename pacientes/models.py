from django.db import models

# Create your models here.
class Animal(models.Model):
    nombre = models.CharField(max_length=45)
    raza = models.CharField(max_length=45)
    sexo = models.CharField(max_length=1)
    pais_origen = models.CharField(max_length=45)
    color = models.CharField(max_length=30)
    uid = models.CharField(primary_key=True, max_length=10, unique=True)
    nombre_dueño = models.CharField(max_length=42)

    def __str__(self) -> str:
        return self.nombre