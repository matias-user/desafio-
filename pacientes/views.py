from django.shortcuts import render, get_list_or_404
from django.http import HttpResponseBadRequest

import requests
from rut_chile import rut_chile

from .models import Animal, Paciente

def obtener_pacientes():
    respuesta = requests.get('https://3y1hl3jca0.execute-api.us-east-1.amazonaws.com/pacientes_endpoint')
    pacientes = respuesta.json()
    return pacientes

# Create your views here.
def inicio(request):
    animales = get_list_or_404(Animal)
    return render(request, 'pacientes/index.html', context={'animales':animales} )

def registro(request):

    ''' get a endpoint expuesto en instrucciones
        se obtiene aquí para mandarlo a la plantilla y usarlo en un selection>option
    ''' 
    pacientes = obtener_pacientes()
    if request.method == 'POST':
        apellido_paterno = ""
        nombre = ""
        paciente = None
        rut = request.POST.get('rut')

        ''' 
         Aquí es para obtener el nombre, apellido y uid desde el get. 
        '''
        for paciente in pacientes['results']:
            if paciente.get('uuid') == request.POST.get('paciente'):
                apellido_paterno = paciente.get('apellido_paterno')
                nombre = paciente.get('nombre')
                uid_paciente = paciente.get('uuid')


        try:

            # Verificar si ya esta creado el Paciente
            existe_paciente = Paciente.objects.get(uid=uid_paciente)

            if existe_paciente:
                paciente = existe_paciente
            else:
                paciente = Paciente(nombre= nombre,apellido=apellido_paterno, uid=uid_paciente)
                paciente.save()

            if not rut_chile.is_valid_rut(rut):
                return HttpResponseBadRequest("El rut ingresado no tiene el formato valido.")


            existe_rut_animl = Animal.objects.get(uid=rut)
            if existe_rut_animl:
                return HttpResponseBadRequest("El rut ingresado ya existe.")

        except Paciente.DoesNotExist:
            pass


        except Animal.DoesNotExist:
            pass


        data = {
            'nombre': request.POST.get('nombre'),
            'raza':request.POST.get('raza'),
            'sexo':request.POST.get('sexo'),
            'pais_origen':request.POST.get('origen'),
            'color':request.POST.get('color'),
            'uid':request.POST.get('rut'),
        }
        
        nuevo_animal = Animal(
                paciente=paciente,
                nombre=data['nombre'],
                raza=data['raza'],
                sexo=data['sexo'],
                pais_origen=data['pais_origen'],
                color=data['color'],
                uid=data['uid'],
                )
        nuevo_animal.save()

    return render(request, 'pacientes/registrar.html', { 'pacientes':pacientes } )