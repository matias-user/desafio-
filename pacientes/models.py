from django.db import models

# Create your models here.
class Paciente(models.Model):
    nombre = models.CharField(max_length=45)
    apellido= models.CharField(max_length=45)
    uid = models.CharField(max_length=45)

    def __str__(self) -> str:
        return self.nombre + " " +self.apellido


class Animal(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE )
    nombre = models.CharField(max_length=45)
    raza = models.CharField(max_length=45)
    sexo = models.CharField(max_length=1)
    pais_origen = models.CharField(max_length=45)
    color = models.CharField(max_length=30)
    uid = models.CharField(primary_key=True, max_length=10, unique=True)

    def __str__(self) -> str:
        return self.nombre