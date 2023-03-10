from django.shortcuts import render, get_list_or_404
from django.http import HttpResponseBadRequest
import requests
from rut_chile import rut_chile

from .models import Animal, Paciente

# Create your views here.
def inicio(request):
    animales = get_list_or_404(Animal)
    return render(request, 'pacientes/index.html', context={'animales':animales} )

def registro(request):

    ''' get a endpoint expuesto en instrucciones
        se obtiene aquí para mandarlo a la plantilla y usarlo en un selection>option
    ''' 
    respuesta = requests.get('https://3y1hl3jca0.execute-api.us-east-1.amazonaws.com/pacientes_endpoint')
    pacientes = respuesta.json()
    
    if request.method == 'POST':
        apellido_paterno = ""
        nombre = ""
        uid_paciente = ""
        nuevo_paciente = None
        rut = request.POST.get('rut')

        ''' 
            Aquí es para obtener el nombre y el apellido paterno desde el get endpoint.   
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
                nuevo_paciente = existe_paciente

            existe_rut = Animal.objects.get(uid=rut)
            if existe_rut:
                return HttpResponseBadRequest("El rut ingresado ya existe.")

                 

            if not rut_chile.is_valid_rut( rut ):
                 return HttpResponseBadRequest("El rut ingresado no es valido")
            
        except Animal.DoesNotExist:
            pass


        except Paciente.DoesNotExist:
                nuevo_paciente = Paciente(nombre= nombre,apellido=apellido_paterno,uid=uid_paciente)
                nuevo_paciente.save()   
                            


        data = {
            'nombre': request.POST.get('nombre'),
            'raza':request.POST.get('raza'),
            'sexo':request.POST.get('sexo'),
            'pais_origen':request.POST.get('origen'),
            'color':request.POST.get('color'),
            'uid':request.POST.get('rut'),
        }
        # Ahora se crea el animal
        nuevo_animal = Animal(
                nombre=data['nombre'],
                paciente=nuevo_paciente,
                raza=data['raza'],
                sexo=data['sexo'],
                pais_origen=data['pais_origen'],
                color=data['color'],
                uid=data['uid']
                )
        nuevo_animal.save()

    return render(request, 'pacientes/registrar.html', { 'pacientes':pacientes } )