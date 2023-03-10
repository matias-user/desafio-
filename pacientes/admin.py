from django.contrib import admin
from .models import Paciente, Animal

# Register your models here.
admin.site.register(Paciente)
admin.site.register(Animal)