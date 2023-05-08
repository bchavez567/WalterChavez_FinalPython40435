from django.shortcuts import render
from App1.models import Contacto , Productos, Curso
from App1.forms import CursoFormulario
from django.http import HttpResponse

# Create your views here.
def inicio(request):
    return render(request, 'App1/inicio.html')
def contacto(request):
    return render(request,'App1/contacto.html')
def productos(request):
    return render(request,'App1/productos.html')
def info(request):
    return render(request,'App1/info.html')
def save(request):
    return render(request,'App1/save.html')

def cursos(request):
    if request.method =='POST':
        miFormulario=CursoFormulario(request.POST)
        print(miFormulario)

        if miFormulario.is_valid:
            informacion=miFormulario.cleaned_data
            curso=Curso(int(informacion['id']),str(informacion['nombre']),int(informacion['curso']))
            curso.save()
            return render(request, 'App1/inicio.html')
    else:
        miFormulario=CursoFormulario()
    return render(request, 'App1/cursos.html', {"miFormulario": miFormulario})

def busquedaCurso(request):
    return render(request,'App1/busquedaCurso.html')

def buscar(request):
    if request.GET['curso']:
        curso = request.GET['curso']
        cursos= Curso.objects.filter(curso__icontains=curso)

        return render(request,'App1/resultadosBusqueda.html', {"cursos":cursos, "comisiones": curso })
    else:
        respuesta= "No enviaste datos"

    return HttpResponse(respuesta)