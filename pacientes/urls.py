from django.urls import path
from . import views

app_name= 'pacientes'
urlpatterns = [
    path( '', views.inicio, name='inicio'  ),
    path( 'registrar/', views.registro, name='registrar'  ),
]