from django.db import models

# Create your models here.
<<<<<<< HEAD
class Paciente(models.Model):
    nombre = models.CharField(max_length=45)
    apellido= models.CharField(max_length=45)
    uid = models.CharField(max_length=45)

    def __str__(self) -> str:
        return self.nombre + " " +self.apellido


=======
>>>>>>> 52edec27ff7ecf34696be0b99f85be0fa8aee0b6
class Animal(models.Model):
    nombre = models.CharField(max_length=45)
    raza = models.CharField(max_length=45)
    sexo = models.CharField(max_length=1)
    pais_origen = models.CharField(max_length=45)
    color = models.CharField(max_length=30)
    uid = models.CharField(primary_key=True, max_length=10, unique=True)
<<<<<<< HEAD
=======
    nombre_dueño = models.CharField(max_length=42)
>>>>>>> 52edec27ff7ecf34696be0b99f85be0fa8aee0b6

    def __str__(self) -> str:
        return self.nombre